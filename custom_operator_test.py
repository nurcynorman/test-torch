import torch
from torch.library import Library, custom_op, opcheck
import uuid

# Generate unique names
unique_id = uuid.uuid4().hex[:6]
libname = f"mylib_{unique_id}"
opname = f"my_add_{unique_id}"
print(f"Using library: {libname}, op: {opname}")

# Step 1: Create library
my_lib = Library(libname, "FRAGMENT")

# Step 2: Register op
@custom_op(f"{libname}::{opname}", mutates_args=[])
def my_add(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    return x + y

# Step 3: Meta impl
def meta_fn(x, y):
    return torch.empty_like(x)

my_lib.impl(opname, meta_fn, dispatch_key="Meta")

# Step 4: Autograd impl
def autograd_fn(x, y):
    return x + y

my_lib.impl(opname, autograd_fn, dispatch_key="Autograd")

# Step 5: Test
a = torch.randn(2, 2, requires_grad=True)
b = torch.randn(2, 2, requires_grad=True)

result = opcheck(getattr(getattr(torch.ops, libname), opname), (a, b))
print(result)


# we create a unique custom pytorch operator inside a unniquely named library then register its implementations withh that library to extend pytorch's fuunctionality
# pytorch internal registry persist across python runs in the same interpreter session does not allow re-registering the same op+dispatch_key combination cuasing a runtime error when trying to register an op with the same or dispatch key again
