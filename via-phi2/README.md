# gpt-code-commenter

## Set up

### For phi2 (local LLM) [UNIX not Windows] [MORE DIFFICULT TO INSTALL]

```shell
cd via-phi2
```

At time of writing, phi2 depends on a dev build of transformers, so it can be tricky to install.

See the (model card)[https://huggingface.co/microsoft/phi-2] for details.

```shell
python -m pipenv run pip install transformers==4.38.2
```

OR if that does not work, try the latest dev version:

```shell
python -m pipenv run pip install git+https://github.com/huggingface/transformers
```

```shell
python -m pipenv run pip install cornsnake==0.0.46 packaging==24.0
```

#### WITHOUT GPU:

Install torch (without CUDA) - please check the [PyTorch site](https://pytorch.org/get-started/locally/#windows-pip) for your system.

```shell
python -m pipenv run pip install torch==2.2.1 torchvision==0.17.1
```

Edit `config.py` and set is_gpu to False.

#### WITH GPU:

Install CUDA to match your NVIDIA GPU - see [NVIDIA site](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html).

Install torch (with CUDA) - please check the [PyTorch site](https://pytorch.org/get-started/locally/#windows-pip) for your system.

- example installing torch with CUDA v12.1:

```shell
python -m pipenv run pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

Install ninja, to speed up compile of flash-attn:

```shell
python -m pipenv run pip install ninja
ninja --version
```

Install flash-attn: [does NOT really work on Windows due to build issues]

```shell
python -m pipenv run pip install flash-attn --no-build-isolation
```

Edit `config.py` and set is_gpu to True.

### Test phi2

(cd via-phi2)

```shell
test-phi2.sh
```

or

(cd via-phi2)

```shell
cd via-phi2
pipenv run python via-phi2 ../test-resources/util_json.py
```
