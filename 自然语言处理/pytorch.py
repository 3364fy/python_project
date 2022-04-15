from __future__ import print_function
import torch
import numpy as np

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

#将Torch Tensor转换为Numpy array
b=a.numpy()
print(b)

#对其中一个进行加法操作。另一个也随之被改变
a.add_(1)
print(a,b)

#将Numpy array转换为Torch Tensor
a=np.ones(5)
b=torch.from_numpy(a)
np.add(a,1,out=a)
print(a,b)

#所有在CPU上的Tensor，除了CharTensor，都可以转换为Numpy array 并可以反向转换
#关于CharTensor，Tensor可以用.to()方法来将其移动到任意设备上

#如果服务器上已经安装了GPU和CUDA
if torch.cuda.is_available():
    #定义一个设备对象，这里指定成CUDA，即使用GPU
    device=torch.device('cuda')
    #直接在GPU上创建一个Tensor
    y=torch.ones_like(x,device=device)
    #将在CPU上面的x张量移动到GPU上面
    x=x.to(device)
    #x和y都在GPU上，才能支持加法运算
    z=x+y
    #此时的张量z在GPU上
    print(z)
    #也可以将z转移到CPU上面，并同时指定张量元素的数据类型
    print(z.to('cpu',torch.double))



