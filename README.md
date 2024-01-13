# ChatGLM3 automatically solves math problems——Track 2——Fine-Tuning

This repo provides the code, prompts, and our answers solved for the [AAAI2024 Global Competition on Math Problem Solving and Reasoning](https://ai4ed.cc/competitions/aaai2024competition)

Our final submission of the answer file is in:

```
/submission/TAL_SAQ6K_EN_prediction.json
```

In the end we get the result file as:`{"TAL_SAQ6K_EN_Public_Acc": 45.28, "TAL_SAQ6K_EN_Private_Acc": 46.52}`

This README document is organized in the following order.

1. **Methods:** The main methods used in the competition and the procedures used to obtain the final results.
2. **Final Submission:** Location for submitting answer results
3. **Setup:** Preparation before running the code
4. **Usage Demo:** Steps to run the code quickly

## Methods

1. We first reason with the `chatGLM-6b-base` model using the following prompt, which yields the result：41.96

2. We then conducted the following experiment:

   where the `1w calculation questions` in the table refer to the 1w passes in the data set of `MathGLM_Arithemetic`：[THUDM/MathGLM: Official Pytorch Implementation for MathGLM (github.com)](https://github.com/THUDM/MathGLM)】

   ``8k inference`` means 8k tracts in the GSM8K dataset：[openai/grade-school-math (github.com)](https://github.com/openai/grade-school-math)

   The `2w goat` is the 2w tract in the GOAT dataset:[liutiedong/goat: a Fine-tuned LLaMA that is Good at Arithmetic Tasks (github.com)](https://github.com/liutiedong/goat)

  ![image-20240113123950956](https://github.com/hot-zhy/MathProblemSolvingFinetuning/assets/100272100/0fbaea4b-b5c7-4196-a6d3-c474296b48e8)


   Based on the results of the fine-tuned reasoning in the table, we vote on the answer corresponding to the data in the table and the answer corresponding to `41.96` obtained in the first step above, i.e., for the same question solved multiple times, the answer with the `most number `of times of occurrence of the answer is chosen as the final answer chosen.

   After this voting process, the final answer is `43.19`.

3. In addition to this, we use code solving (Program-Aided Program, `PAL`, [reasoning-machines/pal: PaL: Program-Aided Language Models (ICML 2023) (github.com)](https:// github.com/reasoning-machines/pal)) for solving the problem:

   We first divided the dataset into the following 14 classes using the `KMeans` algorithm, and then we solved for 5, 6, 7, 8, 9, 10, 12, and 13 of them that were suitable to be solved by the code with answer substitutions on the answer of `43.19`

4. 经过上述步骤，我们得到的最终结果为：`{"TAL_SAQ6K_EN_Public_Acc": 45.28, "TAL_SAQ6K_EN_Private_Acc": 46.52}`

## Final Submission

After the above methods, we finally submitted the answer file in:

```
/submission/TAL_SAQ6K_EN_prediction.json
```

## Setup

1. Pull the code repository

2. Go to `/chatglm3-6b-base-model` and pull the `ChatGLM-6b-base `model from ModelScope or Huggingface

3. Execute the following code file to reason with `ChatGLM-6b-base `and our prompt (remember to modify the relevant input and output files)

   ```
   /code/main.py
   ```
4. Run the code for voting for different models:
   
   ```
   /code/vote/vote.py
   ```

4. If you want to use the Program-Aided Program approach to solving, just execute the following code file (remember to modify the relevant input and output files).

   ```
   /code/PAL/PAL/scripts/pal_chatglm.py
   ```
