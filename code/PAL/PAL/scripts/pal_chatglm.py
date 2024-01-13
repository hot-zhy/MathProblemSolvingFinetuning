import copy
import json
import argparse
import tqdm
import os

from pal import interface
from pal.prompt import math_prompts,pal_prompt,cluster_10_PAL_prompt,cluster_9_PAL_prompt,cluster_6_PAL_prompt,cluster_13_PAL_prompt,cluster_5_PAL_prompt,cluster_12_PAL_prompt,cluster_7_PAL_prompt,cluster_8_PAL_prompt
parser = argparse.ArgumentParser()
parser.add_argument('--append', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument(
    '--dataset', default='../../../dataset/KMeanscluster_7.jsonl', type=str)
parser.add_argument('--model', default='chatglm3-6b-base', type=str)
parser.add_argument('--temperature', default=0.0, type=float)
parser.add_argument('--top_p', default=1.0, type=float)
parser.add_argument('--max_tokens', default=4096, type=int)
args = parser.parse_args()

DATA_PATH = f'../../../dataset/KMeanscluster_7.jsonl'
OUTPUT_PATH = f'../scripts/eval_results/PAL/cluster_7_PAL_answers.jsonl'
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

examples = list(map(json.loads, open(DATA_PATH, encoding='utf-8')))


itf = interface.ProgramChatInterface(
    stop=None,
    get_answer_expr='solution()',
    model=args.model,
    verbose=args.verbose,
    system_message=cluster_7_PAL_prompt.MATH_CHAT_BETA_SYSTEM_MESSAGE,
)
args.append=True
if args.append:
    lines = open(OUTPUT_PATH).readlines()
    num_skip_exps = len(lines)
else:
    num_skip_exps = 0

with open(OUTPUT_PATH, 'a' if args.append else 'w', encoding='utf-8') as f:
    pbar = tqdm.tqdm(examples[num_skip_exps:],
                     initial=num_skip_exps, total=len(examples))
    for x in pbar:
        if 'problem' not in x or x['problem'] is None:
            continue
        question = x['problem']
        result = copy.copy(x)

        try:
            ans = itf.run(
                cluster_7_PAL_prompt.MATH_CHAT_BETA_PROMPT+question,
                temperature=args.temperature,
                top_p=args.top_p,
                max_tokens=args.max_tokens
            )
            ans = float(ans)
        except Exception as e:
            print(e)
            ans = ''

        result['answer'] = ans
        result['generation'] = itf.history
        f.write(json.dumps(result, ensure_ascii=False) + '\n')

        itf.clear_history()
        f.flush()
