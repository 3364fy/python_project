from __future__ import print_function
import torch

x=torch.empty(5,3)
print(x)
#高斯分布，均值为零，方差为一
#初始化5行三列的张量
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

x.copy_(y)
print(x)

print(x[:,1])

x=torch.rand(4,4)
#torch.view()操作需要保证数据元素的总数量不变
y=x.view(16)
#-1代表自动匹配个数
z=x.view(-1,8)
print(x.size(),y.size(),z.size())

#如果张量中只有一个元素，可以用.item()将值取出，作为一个python number
x=torch.rand(1)
print(x)
print(x.item())

a=torch.ones(5)
print(a)



