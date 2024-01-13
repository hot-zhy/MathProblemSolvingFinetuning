import json

# 所有的
with open('../eval_results/all_answer_simpliy.json', 'r', encoding='utf-8') as file:
    test1_data = json.load(file)


with open('../eval_results/arithmetic_answer.json', 'r', encoding='utf-8') as file:
    test2_data = json.load(file)

count=1
for key, value in test2_data.items():
    if key in test1_data:
        if value!="":
            print(value)
            count+=1
            test1_data[key] = value
print('count:')
print(count)

with open('../eval_results/merge.json', 'w', encoding='utf-8') as file:
    json.dump(test1_data, file, indent=4)
