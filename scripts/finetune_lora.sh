#! /usr/bin/env bash

export PYTHONPATH="${PYTHONPATH}:/data/home/scv9619/run/chatglm3-6b-base-model/code/finetune_basemodel_lora"

set -ex

LR=1e-4
NUM_GPUS=1
LORA_RANK=8
LORA_ALPHA=32
LORA_DROUPOUT=0.1

MAX_SOURCE_LEN=512
MAX_TARGET_LEN=1024
DEV_BATCH_SIZE=2
GRAD_ACCUMULARION_STEPS=10
MAX_STEP=4000
SAVE_INTERVAL=2000
MAX_SEQ_LEN=1024

RUN_NAME=cluster_finetune_2.8w_no_prompt
BASE_MODEL_PATH=../chatglm3-6b-base-model/chatglm3-6b-base/
DATASET_PATH=../dataset/finetune/1wCal.json
DATESTR=`date +%Y%m%d-%H%M%S`
OUTPUT_DIR=../chatglm3-6b-base-model/ChatGLM3/finetune_basemodel_lora/scripts/output/${RUN_NAME}-${DATESTR}-${LR}
MASTER_PORT=$(shuf -n 1 -i 10000-65535)

mkdir -p $OUTPUT_DIR

python finetune.py \
    --train_format input-output \
    --train_file $DATASET_PATH \
    --lora_rank $LORA_RANK \
    --lora_alpha $LORA_ALPHA \
    --lora_dropout $LORA_DROUPOUT \
    --max_seq_length $MAX_SEQ_LEN \
    --preprocessing_num_workers 1 \
    --model_name_or_path $BASE_MODEL_PATH \
    --output_dir $OUTPUT_DIR \
    --per_device_train_batch_size $DEV_BATCH_SIZE \
    --gradient_accumulation_steps $GRAD_ACCUMULARION_STEPS \
    --max_steps $MAX_STEP \
    --logging_steps 1 \
    --save_steps $SAVE_INTERVAL \
    --fp16 \
    --learning_rate $LR  2>&1 | tee ${OUTPUT_DIR}/train.log \