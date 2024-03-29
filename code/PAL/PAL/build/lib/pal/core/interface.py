import io
import signal
from contextlib import redirect_stdout
from typing import Any, Callable, List, Optional
from collections import Counter

from .runtime import GenericRuntime
from .backend import call_chat_glm
import re


class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def timeout_handler(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.timeout_handler)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


class ProgramInterface:

    def __init__(
        self,
        model: str = 'code-davinci-002',
        runtime: Optional[Any] = None,
        stop: str = '\n\n',
        get_answer_symbol: Optional[str] = None,
        get_answer_expr: Optional[str] = None,
        get_answer_from_stdout: bool = False,
        verbose: bool = False
    ) -> None:

        self.model = model
        self.runtime = runtime if runtime else GenericRuntime()
        self.history = []
        self.stop = stop
        self.answer_symbol = get_answer_symbol
        self.answer_expr = get_answer_expr
        self.get_answer_from_stdout = get_answer_from_stdout
        self.verbose = verbose
    def clear_history(self):
        self.history = []
    def execute(self, code: Optional[List[str]] = None):
        code = code if code else self.code
        if self.get_answer_from_stdout:
            program_io = io.StringIO()
            with redirect_stdout(program_io):
                self.runtime.exec_code('\n'.join(code))
            program_io.seek(0)
            return program_io.readlines()[-1]
        elif self.answer_symbol:
            self.runtime.exec_code('\n'.join(code))
            return self.runtime._global_vars[self.answer_symbol]
        elif self.answer_expr:
            self.runtime.exec_code('\n'.join(code))
            return self.runtime.eval_code(self.answer_expr)
        else:
            self.runtime.exec_code('\n'.join(code[:-1]))
            return self.runtime.eval_code(code[-1])

SYSTEM_MESSAGES = 'You are a helpful python programmer.'


class ProgramChatInterface(ProgramInterface):
    def __init__(self, *args, system_message: str = SYSTEM_MESSAGES, **kwargs):
        super().__init__(*args, **kwargs)
        self.system_message = system_message
        print(system_message)

    def generate(self, prompt: str, temperature: float = 0, top_p: float = 1, max_tokens: int = 4096):
        messages = [{'role': 'system', 'content': self.system_message}, {
            'role': 'user', 'content': prompt}]
        gen = call_chat_glm(messages, model=self.model, stop=self.stop,
                            temperature=temperature, top_p=top_p, max_tokens=max_tokens)
        if self.verbose:
            print(gen)
        self.history.append(gen)

        return self.process_generation_to_code(gen)

    def process_generation_to_code(self, gens: str):
        # print(gens)
        # 找到最后一个代码对
        match = re.findall(r'```(.*?)```', gens, re.DOTALL)
        gens = match[-1] if match else ""
        if '```python' in gens:
            gens = gens.split('```python')[1].split('```')[0]
        elif '```' in gens:
            gens = gens.split('```')[1].split('```')[0]

        # print(gens)
        return gens.split('\n')

    def run(self, prompt: str, time_out: float = 10, temperature: float = 0, top_p: float = 1, max_tokens: int = 4096):
        code = self.generate(prompt, temperature=temperature,
                             top_p=top_p, max_tokens=max_tokens)
        with timeout(time_out):
            try:
                exec_result = self.execute(code)
            except Exception as e:
                print(e)
        return exec_result
