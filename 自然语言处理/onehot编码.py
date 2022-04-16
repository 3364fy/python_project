#导入用于对象保存与加载的joblib
import joblib
#词汇映射器
from keras.preprocessing.text import Tokenizer

vocab={'周杰伦','陈奕迅','王力宏','李宗盛','吴亦凡','鹿晗'}
t=Tokenizer(num_words=None,char_level=False)
t.fit_on_texts(vocab)

for token in vocab:
    zero_list=[0]*len(vocab)
    #使用映射器转化现有的文本数据，每个词汇对应从开始的自然数
    #返回样式如[[2]],取出其中的数据需要使用[0][0]
    token_index=t.texts_to_sequences([token])[0][0]-1
    zero_list[token_index]=1
    print(f'{token}的one-hot编码为：{zero_list}')
#使用joblib工具保存映射，以便之后使用
tokenizer_path='./Tokenizer'
joblib.dump(t,tokenizer_path)
