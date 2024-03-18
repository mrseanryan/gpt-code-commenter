# gpt-code-commenter

## Set up

ref - https://huggingface.co/TheBloke/phi-2-GGUF

### For phi2 (local LLM) [UNIX not Windows] [MORE DIFFICULT TO INSTALL]

```shell
cd via-phi2-the-bloke
```

Run one of the following, depending on your system:

```
# Base ctransformers with no GPU acceleration
pip install llama-cpp-python
# With NVidia CUDA acceleration
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
# Or with OpenBLAS acceleration
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
# Or with CLBLast acceleration
CMAKE_ARGS="-DLLAMA_CLBLAST=on" pip install llama-cpp-python
# Or with AMD ROCm GPU acceleration (Linux only)
CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python
# Or with Metal GPU acceleration for macOS systems only
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python

# In windows, to set the variables CMAKE_ARGS in PowerShell, follow this format:
$env:CMAKE_ARGS = "-DLLAMA_OPENBLAS=on"
pip install llama-cpp-python
```

```shell
python -m pipenv run pip install llama-cpp-python cornsnake
```

Download the model from here: https://huggingface.co/TheBloke/phi-2-GGUF/blob/main/phi-2.Q5_K_S.gguf

Place it under the models folder.

## Test

```
./test-phi2.sh
```

OR

```
python -m pipenv run python via-phi2/test-via-llama_cpp.py
```

## Usage

```
python -m pipenv run python via-phi2
```
