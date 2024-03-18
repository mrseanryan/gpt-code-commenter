import config

from llama_cpp import Llama

model = "./models/phi-2.Q5_K_S.gguf" # phi-2.Q4_K_M.gguf  # Download the model file first

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama(
  model_path=model,
  n_ctx=2048,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)


def _get_completion(prompt, dummy_response=None):
    if config.is_dry_run:
        return dummy_response

    output = llm(
    f"Instruct: {prompt}\nOutput:\n", # Prompt
    max_tokens=512,  # Generate up to 512 tokens
    stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
    echo=False        # Whether to echo the prompt
    )

    print(output)

    output_text = output['choices'][0]['text']

    return output_text

def send_prompt(prompt, dummy_response = None):
    if config.is_debug:
        print("=== INPUT ===")
        print(prompt)

    response = _get_completion(prompt, dummy_response=dummy_response)

    if config.is_debug:
        print("=== RESPONSE ===")
        print(response)

    return response
