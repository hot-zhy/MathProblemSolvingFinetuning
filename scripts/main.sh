#!/bin/bash

# conda activate myconda

export PYTHONPATH="${PYTHONPATH}:./code"

python code/main.py \
    --batch_size 32 \
    --max_input_tokens 2048 \
    --max_new_tokens 2048 \
    --val_dataset_path ../dataset/AAAI/TAL-SAQ6K-EN.jsonl \
    --answers_path ../submission/aaai/prompts.json \
    --model ../chatglm3-6b-base-model/chatglm3-6b-base \
    --tokenizer ../chatglm3-6b-base-model/chatglm3-6b-base \
    # --lora_path ../chatglm3-6b-base-model/ChatGLM3/finetune_basemodel_lora/scripts/output/../pytorch_model.pt
    