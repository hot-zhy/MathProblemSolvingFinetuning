import json
import re
from fractions import Fraction


def to_nearest_fraction(number_str, tolerance=1e-5):
    try:
        # 将字符串转换为浮点数
        number = float(number_str)
    except ValueError:
        # 如果输入无法转换为浮点数，返回错误信息
        return "Invalid input. Please enter a valid number."

    # 将数字转换为最接近的分数
    fraction = Fraction(number).limit_denominator()

    # 如果分数足够接近整数，则返回该整数
    if abs(fraction - round(fraction)) <= tolerance:
        return round(fraction)

    return str(fraction)


def convert_jsonl_to_json(jsonl_file_path, json_file_path):
    result = {}
    with open(jsonl_file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                data = json.loads(line, strict=False)
                queId = data.get('queId')
                answer = data.get('answer')
                # result[queId] = answer
                # if data['pal_answer'] == "":
                #     pal_answer = str(data['pal_generation'])
                #     number3_match = re.findall(
                #         r"[-+]?\d*\.\d+|[-+]?\d+", pal_answer)
                #     if number3_match:
                #         pal_answer = float(number3_match[-1])
                #         result[queId] = pal_answer
                # else:
                #     pal_answer = data['pal_answer']
                #     result[queId] = pal_answer
                # answer = str(data.get('choose-answer'))

                # answer = to_nearest_fraction(answer)
                # # 匹配时间
                # # 正则表达式匹配 08:30 或 8:30 格式的时间
                # # time_pattern = r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\s*(?:a\.?m\.?|p\.?m\.?)\b'
                # time_matches = re.findall(time_pattern, answer, re.IGNORECASE)
                # answer_match = re.search(r'Answer:\s*(.*)', answer)
                # if answer_match:
                #     answer = answer_match.group(1)
                number_match = re.findall(
                    r"[-+]?\d*\.\d+|[-+]?\d+", answer)
                if number_match:
                    answer = float(number_match[-1])
                    result[queId] = answer
                # else:
                #     number_match = re.findall(
                #         r"[-+]?\d*\.\d+|[-+]?\d+", answer)
                #     if number_match:
                #         answer = float(number_match[-1])
            except json.JSONDecodeError as e:
                print(e)
                print(queId)

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4)


# 调用函数
# for i in range(14):
# convert_jsonl_to_json(
#     '../cluster_answers/difficulty_classification/problems_difficulty_2_COT.jsonl', f'../cluster_answers/difficulty_classification/difficulty_submission/problems_difficulty_2_COT.json')

convert_jsonl_to_json(
    './calculation_answers_extract.jsonl', f'./calculation_answers_extract_simpy.json')
