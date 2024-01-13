import argparse
import os
import json
from tqdm import tqdm
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig, AutoModel
from peft import get_peft_model, LoraConfig, TaskType, prepare_model_for_kbit_training


def main(args):
    # Check if CUDA is available and set the device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Model and Tokenizer Configuration
    tokenizer = AutoTokenizer.from_pretrained(
        args.tokenizer, trust_remote_code=True)
    model = AutoModel.from_pretrained(
        args.model, load_in_8bit=False, trust_remote_code=True).to(device)

    # LoRA Model Configuration
    if args.lora_path != None:
        peft_config = LoraConfig(
            task_type=TaskType.CAUSAL_LM, inference_mode=True,
            target_modules=['query_key_value'],
            r=args.lora_rank, lora_alpha=args.lora_alpha, lora_dropout=args.lora_dropout
        )
        model = get_peft_model(model, peft_config)
        if os.path.exists(args.lora_path):
            # Specify the map_location to load the model on the available device
            model.load_state_dict(torch.load(
                args.lora_path, map_location=device), strict=False)

    # instruction_template = (
    #     "Solve the following problem. Return the answer as a number.\n"
    #     "You should add The answer is xxx, where xxx is the answer number at the end of your answer.\n\n"
    #     "The problem is:\n{problem}\n\n"
    #     "Let's think step by step."
    # )
    instruction_template = (
        "Solve the following problem. First, make sure you understand the requirements and conditions of the problem.\n"
        "Consider different methods to solve it and choose the most appropriate one.\n"
        "Show your calculation step by step to make the logic clear.\n"
        "After solving the problem, think about how you can verify the correctness of your answer.\n"
        "Finally, return the answer as a number with 'Answer: xxx', where xxx is the answer number.\n\n"
        "The problem is:\n{problem}\n\n"
        "Note that if you haven't finished generating your answers, don't stop there!"
        "Let's first understand the problem, extract relevant variables and their corresponding numerals, and devise a plan. Then, let's carry out the plan, calcuate intermediate results(pay attention to calculation and common sense), solve the problem step by step, and show the answer."
        "Let's think step by step."
    )
    # instruction_template = (
    #     "{problem}"
    # )

    # Read the dataset
    with open(args.val_dataset_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines = lines[:args.max_samples]

    pro_id_list = []

    try:
        with open(args.answers_path, 'r', encoding='utf-8-sig') as output_file:
            data = output_file.readlines()
            for line_number, line in enumerate(data, start=1):
                pro_id_list.append(json.loads(line)['queId'])
    except FileNotFoundError:
        print("No existing answer file found. Starting from scratch.")
    except Exception as e:
        print(f"An error occurred while reading the answer file: {str(e)}")

    # Process the questions in batches and generate answers
    answers_list = []
    with open(args.answers_path, 'a', encoding='utf-8') as json_file:
        for i in tqdm(range(0, len(lines), args.batch_size)):
            batch = lines[i:i + args.batch_size]
            formatted_problems = [
                instruction_template.format(
                    problem=json.loads(line)['problem'])
                for line in batch
            ]

            # Check if queId already exists in the list of generated answers
            queIds = [json.loads(line)['queId'] for line in batch]
            queIds_to_process = [q for q in queIds if q not in pro_id_list]

            # If all queIds are already generated, skip to the next batch of questions
            if not queIds_to_process:
                continue

            # Tokenize the problems
            inputs = tokenizer(formatted_problems, return_tensors='pt', padding=True, truncation=True,
                               max_length=args.max_input_tokens)
            # Move the inputs to the GPU if available
            inputs = {key: tensor.to(device) for key, tensor in inputs.items()}

            # Generate answers using the model
            with torch.no_grad():
                outputs = model.generate(
                    input_ids=inputs['input_ids'],
                    max_length=inputs["input_ids"].shape[-1] +
                    args.max_new_tokens
                )

            # Decode the generated answers
            # outputs = outputs[0, inputs['input_ids'].shape[-1]:]
            batch_answers = tokenizer.batch_decode(
                outputs, skip_special_tokens=True)

            # Extend the answers_list with the new answers
            for queId, formatted_problem, generated_text in zip(queIds, formatted_problems, batch_answers):
                if queId in pro_id_list:
                    continue

                answers_list.append({
                    'queId': queId,
                    'problem': formatted_problem,
                    'answer': generated_text
                })

                # Save the generated answer to the JSON file
                json.dump(answers_list[-1], json_file, ensure_ascii=False)
                json_file.write('\n')

                # Add the queId to the list of generated answers
                pro_id_list.append(queId)

    print(f"The answers have been saved to {args.answers_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Evaluate mathematical problems using the MetaMath model.')

    # data
    parser.add_argument('--batch_size', type=int, default=8,
                        help='Batch size for processing questions.')
    parser.add_argument('--max_samples', type=int, default=None,
                        help='Maximum number of samples to process.')
    parser.add_argument('--val_dataset_path', type=str,
                        default='../dataset/AAAI/TAL-SAQ6K-EN.jsonl', help='Path to the validation dataset.')
    parser.add_argument('--answers_path', type=str,
                        default='../submission/answers.jsonl', help='Path to save the answers.')
    # model
    parser.add_argument("--model", type=str, default=None,
                        help="The directory of the model")
    parser.add_argument("--tokenizer", type=str,
                        default=None, help="Tokenizer path")
    parser.add_argument("--lora_path", type=str, default=None,
                        help="Path to the LoRA model checkpoint")
    parser.add_argument('--max_input_tokens', type=int,
                        default=512, help="Maximum input tokens for generation")
    parser.add_argument("--max_new_tokens", type=int,
                        default=512, help="Maximum new tokens for generation")
    parser.add_argument("--lora_alpha", type=float,
                        default=32, help="LoRA alpha")
    parser.add_argument("--lora_rank", type=int, default=8, help="LoRA r")
    parser.add_argument("--lora_dropout", type=float,
                        default=0.1, help="LoRA dropout")
    args = parser.parse_args()

    try:
        main(args)
    except Exception as e:
        print(f"An error occurred:{str(e)}")
