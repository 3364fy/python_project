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

#关于方法.requires_grad_():该方法可以原地改变Tensor的属性.requires_grad的值，如果没有主动设定默认为False
a=torch.rand(2,2)
a=((a*3)/(a-1))
print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b=(a*a).sum()
print(b.grad_fn)

#关于梯度（Gradients）
#在Pytorch中，反向传播是依靠.backward()实现的
out.backward()
print(x.grad)

#关于自动求导的属性设置：可以通过设置.require_grad=True来执行自动求导，也可以通过代码块的·限制来停止自动求导
print(x.requires_grad)
print((x**2).requires_grad)

with torch.no_grad():
    print((x**2).requires_grad)

#可以通过.detach()获得一个新的Tensor，拥有相同的内容但不需要自动求导
print(x.requires_grad)
y=x.detach()
print(y.requires_grad)
print(x.eq(y).all())