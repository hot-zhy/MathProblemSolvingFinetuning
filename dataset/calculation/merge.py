import json

result = {}
with open('../../code/vote/final_answer.json', 'r', encoding='utf-8') as file:
    test1_data = json.load(file)
    result = test1_data


with open('./calculation_answers_extract_simpy.json', 'r', encoding='utf-8') as file:
    test2_data = json.load(file)


for key, value in test2_data.items():
    if key in test1_data:
        try:
            float_value = float(value)
            if float_value.is_integer():
                result[key] = float_value
                print(float_value)
            else:
                int_part, decimal_part = str(float_value).split('.')
                if len(decimal_part) < 7:
                    result[key] = float_value
                    print(float_value)
        except ValueError:
            result[key] = test1_data[key]

with open('./TAL_SAQ6K_EN_prediction.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4)
