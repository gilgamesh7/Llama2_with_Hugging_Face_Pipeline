# Benchmarking (on M1 Max, 10-core CPU, 24-core GPU)

# With CPU
import torch
import timeit

device = torch.device('cpu')
x = torch.rand((10000, 10000), dtype=torch.float32)
y = torch.rand((10000, 10000), dtype=torch.float32)
x = x.to(device)
y = y.to(device)

start = timeit.default_timer()
x * y
time_using_cpu = timeit.default_timer() - start
print(f"Time using CPU : {time_using_cpu}")

# With GPU
device = torch.device('mps')
start = timeit.default_timer()
x * y
time_using_gpu = timeit.default_timer() - start
print(f"Time using GPU : {time_using_gpu}")

print(f"GPU is faster than CPU by {time_using_cpu / time_using_gpu} times")