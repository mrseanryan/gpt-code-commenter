from openai import OpenAI

import config

client = OpenAI()

def _get_completion(prompt, model=config.model, temperature=config.temperature, messages=None, dummy_response=None, max_tokens=config.max_tokens):
    if config.is_dry_run:
        return dummy_response

    if messages is None:
        messages = [{"role": "user", "content": prompt}]

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
        max_tokens=max_tokens,
        # Temperature is the degree of randomness of the model's output
        # 0 would be same each time. 0.7 or 1 would be difference each time, and less likely words can be used:
        temperature=temperature
    )
    generated = ""
    for chunk in stream:
        next_text = chunk.choices[0].delta.content or ""
        print(next_text, end="")
        generated += next_text

    return generated

def send_prompt(prompt, dummy_response = None):
    if config.is_debug:
        print("=== INPUT ===")
        print(prompt)

    response = _get_completion(prompt, temperature=config.temperature, dummy_response=dummy_response)

    if config.is_debug:
        print("=== RESPONSE ===")
        print(response)

    return response
