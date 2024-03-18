import config

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

if config.is_gpu:
    torch.set_default_device("cuda")
else:
    torch.set_default_device("cpu")

model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", 
                                             torch_dtype="auto",
                                             trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

def _get_completion(prompt, dummy_response=None):
    if config.is_dry_run:
        return dummy_response

    inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=False)

    outputs = model.generate(**inputs, max_length=2048)
    text = tokenizer.batch_decode(outputs)[0]
    return text

def send_prompt(prompt, dummy_response = None):
    if config.is_debug:
        print("=== INPUT ===")
        print(prompt)

    response = _get_completion(prompt, dummy_response=dummy_response)

    if config.is_debug:
        print("=== RESPONSE ===")
        print(response)

    return response
