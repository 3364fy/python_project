import os
import pickle

import os
import pickle

from sklearn.datasets._base import Bunch
from tool import readfile


def corpus2Bunch(wordbag_path, seg_path):
    catelist = os.listdir(seg_path)  # 获取seg_path下的所有子目录，也就是分类信息
    # 创建一个Bunch实例
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)
    '''
    extend(addlist)是python list中的函数，意思是用新的list（addlist）去扩充
    原来的list
    '''
    # 获取每个目录下所有的文件
    for mydir in catelist:
        class_path = seg_path + mydir + "/"  # 拼出分类子目录的路径
        file_list = os.listdir(class_path)  # 获取class_path下的所有文件
        for file_path in file_list:  # 遍历类别目录下文件
            fullname = class_path + file_path  # 拼出文件名全路径
            bunch.label.append(mydir)
            bunch.filenames.append(fullname)
            bunch.contents.append(readfile(fullname))  # 读取文件内容
            '''append(element)是python list中的函数，意思是向原来的list中添加element，注意与extend()函数的区别'''
    # 将bunch存储到wordbag_path路径中
    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print("构建文本对象结束！！！")

if __name__ == "__main__":
    #对训练集进行Bunch化操作：
    _Bunch_path = "训练Bunch/bunch.dat"  # Bunch存储路径
    seg_path = "训练集分词/"  # 分词后分类语料库路径
    corpus2Bunch(_Bunch_path, seg_path)

    _Bunch_path = "测试Bunch/bunch.dat"  # Bunch存储路径
    seg_path = "测试集分词/"  # 分词后分类语料库路径
    corpus2Bunch(_Bunch_path, seg_path)
