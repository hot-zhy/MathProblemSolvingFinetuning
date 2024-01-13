#!/bin/bash

# conda activate myconda

export PYTHONPATH="${PYTHONPATH}:./code"

python code/main.py \
    --batch_size 32 \
    --max_input_tokens 2048 \
    --max_new_tokens 2048 \
    --val_dataset_path ./dataset/AAAI/TAL-SAQ6K-EN.jsonl \
    --answers_path ./submission/aaai/prompts.json \
    --model /data/home/scv9619/archive/chatglm3-6b-base \
    --tokenizer /data/home/scv9619/archive/chatglm3-6b-base/ \
    --lora_path /data/home/scv9619/run/chatglm3-6b-base-model/code/finetune_basemodel_lora/scripts/output/text-20231219-203121-1e-4/pytorch_model.pt
    