import json
import torch
from transformers import AutoModelForCausalLM,AutoTokenizer,AutoConfig

MODEL_PATH="/home/zhy/chatglm3-base-6b-generation/chatglm3-6b-base-model/chatglm3-6b-base"
TOKENIZER_PATH="/home/zhy/chatglm3-base-6b-generation/chatglm3-6b-base-model/chatglm3-6b-base"

# Loading Models and Splitters
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
config = AutoConfig.from_pretrained(MODEL_PATH, trust_remote_code=True)
glm_model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, config=config, trust_remote_code=True)

# Move the model to the GPU (if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
glm_model.to(device)

def call_chat_glm(messages, model='chatglm3-6b-base', stop=None, temperature=0., top_p=1.0, max_tokens=128):
    formatted_input = messages[0]['role']+':'+messages[0]['content']+'\n'+messages[1]['role']+':'+messages[1]['content']
    print(len(messages))

    # tokenize
    inputs = tokenizer(formatted_input, return_tensors='pt', padding=True, truncation=True, max_length=max_tokens)

    # Move inputs to the same device (GPU or CPU)
    inputs = {key: tensor.to(device) for key, tensor in inputs.items()}

    # Using models to generate responses
    with torch.no_grad():
        outputs = glm_model.generate(**inputs, max_length=max_tokens)

    # Decode generated responses into readable text
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    print(reply)

    return reply
