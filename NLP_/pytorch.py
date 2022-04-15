from __future__ import print_function
import torch

x=torch.empty(5,3)
print(x)
#高斯分布，均值为零，方差为一
x2=torch.rand(5,3)
print(x2)

x3=torch.zeros(5,3,dtype=torch.int)
print(x3)

x4=torch.tensor([2.5,3.5])
print(x4)

x=x.new_ones(5,3,dtype=torch.double)
print(x,x.size())
y=torch.randn_like(x,dtype=torch.float)
print(y)

print(x+y)

print(torch.add(x,y))

result=torch.empty(5,3)
torch.add(x,y,out=result)
print(result)

y.add_(x)
print(y)

y.sub_(x)
print(y)

