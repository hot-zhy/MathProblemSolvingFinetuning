import json
import re

answers = {}

answers_path = '../eval_results/arithmetic_answer.json'
processed_path = '../eval_results/all_answer_simpliy.json'


def find_last_number(input_string):
    match = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", input_string)
    if match:
        return float(match[-1])
    else:
        return "no answer"


with open(answers_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    for key, value in data.items():
        print(value)
        answer = find_last_number(value)
        answers[key] = answer

with open(processed_path, 'w', encoding='utf-8') as file:
    json.dump(answers, file, indent=4)
