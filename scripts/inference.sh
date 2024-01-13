#!/bin/bash

# conda activate myconda

export PYTHONPATH="${PYTHONPATH}:./src"

python code/inference.py \
    --pt-checkpoint /mnt/chatGLM3-base/chatglm3-6b-base-model/ptuning-20231115-201054-128-2e-3/ \
    --model_path /mnt/chatGLM3-base/chatglm3-6b-base-model/chatglm3-6b-base/ \
    --tokenizer_path /mnt/chatGLM3-base/chatglm3-6b-base-model/chatglm3-6b-base/ \
    --share_gradio False