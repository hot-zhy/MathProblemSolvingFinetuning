import re
import json


def latex_to_plain_text(latex_str):
    # 替换基本的数学符号
    replacements = {
        r'\\times': '*',      # 乘号
        r'\\div': '/',        # 除号
        r'\\cdot': '*',       # 点乘号
        r'\\pm': '±',         # 正负号
        r'\\mp': '∓',         # 负正号
        r'\\leq': '≤',        # 小于等于
        r'\\geq': '≥',        # 大于等于
        r'\\neq': '≠',        # 不等于
        r'\\approx': '≈',     # 约等于
        r'\\infty': '∞',      # 无穷大
        r'\\alpha': 'α',      # 希腊字母alpha
        r'\\beta': 'β',       # 希腊字母beta
        # 更多的符号可以根据需要添加
    }

    # 进行替换
    for latex, plain in replacements.items():
        latex_str = re.sub(latex, plain, latex_str)

     # 处理分数 \frac{...}{...}
    latex_str = re.sub(
        r'\\frac\{?\{?([^}]+)\}?\}?\{?\{?([^}]+)\}?\}?', r'(\1)/(\2)', latex_str)

    # 处理乘方 a^b
    latex_str = re.sub(r'(\w+)\^(\w+)', r'\1^\2', latex_str)

    # 处理上标和下标
    latex_str = re.sub(r'\{([^\}]+)\}', r'(\1)', latex_str)  # 大括号
    latex_str = re.sub(r'\^', '^', latex_str)               # 上标
    latex_str = re.sub(r'_', '_', latex_str)                # 下标

    # 去除多余的LaTeX符号
    latex_str = re.sub(r'\\', '', latex_str)  # 移除反斜杠
    latex_str = re.sub(r'\$', '', latex_str)  # 移除美元符号

    return latex_str


# 示例使用
latex_example = r"$$\frac{a}{b} \times \pi \pm \sqrt{x} \leq \infty$$"
plain_text = latex_to_plain_text(latex_example)
print(plain_text)


def process_jsonl_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file_in, open(output_file, 'a', encoding='utf-8') as file_out:
        for line in file_in:
            # 解析JSONL行
            json_obj = json.loads(line)

            # 处理每个键值对中的LaTeX字符串
            for key, value in json_obj.items():
                if isinstance(value, str):
                    json_obj[key] = latex_to_plain_text(value)+'='

            # 将处理后的对象追加到输出文件
            json.dump(json_obj, file_out, ensure_ascii=False)
            file_out.write('\n')


# 示例使用
input_jsonl = './calculation_questions.jsonl'  # 输入文件路径
output_jsonl = './calculation_questions_extract.jsonl'  # 输出文件路径
process_jsonl_file(input_jsonl, output_jsonl)
