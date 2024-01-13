import json
from fractions import Fraction


def convert_decimal_to_fraction(value):
    try:
        # 只处理小数点后大于4位的小数
        if len(str(value).split('.')[1]) > 7:
            return str(Fraction(value).limit_denominator())
        else:
            return value
    except (ValueError, IndexError):
        # 如果转换失败或者不是小数，返回原始值
        return value


def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 处理数据中的每个值
    processed_data = {key: convert_decimal_to_fraction(
        value) for key, value in data.items()}

    # 将处理后的数据写入新文件
    with open('../eval_results/processed_test.json', 'w', encoding='utf-8') as file:
        json.dump(processed_data, file, indent=4)


# 调用函数处理文件
process_json_file(
    '../eval_results/merge.json')
