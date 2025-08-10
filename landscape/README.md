Pytorch Landscape map together open source projects hosted by PyTorch or member companies. For example in MLOps, there is Accelerate from huggingface. Acclerate (install with uv pip install accelerate), enables distributed training of any type of training setup.

running `accelearete env` will environtment of your machine.

```md
(Downloads) PS C:\Users\fadzw\Downloads> accelerate env

Copy-and-paste the text below in your GitHub issue

- `Accelerate` version: 1.10.0
- Platform: Windows-11-10.0.26100-SP0
- `accelerate` bash location: C:\Users\fadzw\Downloads\.venv\Scripts\accelerate.exe
- Python version: 3.13.6
- Numpy version: 2.2.4
- PyTorch version: 2.8.0+cpu
- PyTorch accelerator: N/A
- System RAM: 31.37 GB
- `Accelerate` default config:
        Not found
```

with no GPU detected and no any setup made. Do `accelerate config`, or you can quickly run this which is a barebones conf that does not include options such as DeepSpeed configuration.
`python -c "from accelerate.utils import write_basic_config; write_basic_config(mixed_precision='fp16')"`