import torch
from torch.library import Library, custom_op, opcheck
import uuid

# Generate a unique op name
unique_op = f"my_add_{uuid.uuid4().hex[:6]}"
print(f"Using op: {unique_op}")

my_lib = Library("mylib", "FRAGMENT")

@custom_op(f"mylib::{unique_op}", mutates_args=[])
def my_add(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    return x + y

def meta_fn(x, y):
    return torch.empty_like(x)

my_lib.impl(unique_op, meta_fn, dispatch_key="Meta")

def autograd_fn(x, y):
    return x + y

my_lib.impl(unique_op, autograd_fn, dispatch_key="Autograd")

# Test it
a = torch.randn(2, 2, requires_grad=True)
b = torch.randn(2, 2, requires_grad=True)

result = opcheck(getattr(torch.ops.mylib, unique_op), (a, b))
print(result)
