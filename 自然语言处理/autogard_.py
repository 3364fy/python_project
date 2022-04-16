#在整个Pytorch中，所有的神经网络本质上都是一个autogard package包（自动求导工具包）
#autogard package提供了一个对Tensor上所有的操作进行自动微分的功能
import torch

x1=torch.ones(3,3)
print(x1)
x=torch.ones(2,2,requires_grad=True)
print(x)

y=x+2
print(y)
#打印Tensor的grad_fn属性
print(x.grad_fn)
print(y.grad_fn)

z=y*y*3
out=z.mean()
print(z,out)