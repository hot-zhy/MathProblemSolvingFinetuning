import json

# 所有的
with open('../eval_results/processed_test.json', 'r', encoding='utf-8') as file:
    test1_data = json.load(file)
    
for key, value in test1_data.items():
    test1_data[key] = str(value)


with open('../eval_results/merge_string_fraction.json', 'w', encoding='utf-8') as file:
    json.dump(test1_data, file, indent=4)
