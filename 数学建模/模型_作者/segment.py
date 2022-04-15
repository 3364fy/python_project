import os
import jieba
from tool import savefile, readfile

'all_poets/dynastys/authors/poets'
def corpus_segment(poets_path, seg_path):
    '''
    poets_path是未分词全诗集路径
    seg_path是分词后全诗集存储路径
    '''
    dynastys = os.listdir(poets_path)  # 获取poets_path下的所有子目录
    #print(dynastys)
    for dynasty in dynastys:
        # 获取每个朝代下所有的诗作
        poets = os.listdir(poets_path+'/'+dynasty)
        #获得每个诗人的所有诗作
        for poet in poets:
            #print(poet)
            poet_path = f'{poets_path}/{dynasty}/{poet}'
            #print(poet_path)
            seg_dir = f'{seg_path}/{dynasty}/'
            #print(seg_dir)
            if not os.path.exists(seg_dir):
                os.makedirs(seg_dir)

            poetname = poet_path
            content = readfile(poetname)
            for junk in ["\n"," ", "。", "，", "[", "]", "《", "》", "（", "）", "〖", "〗", "『", "』", "：", "「", "」", "、", "{", "}", "/", "=", "？", "1", "2", "3", "4", "5", "6", "7", "8", "9",] :
                content = content.replace(f'{junk}'.encode('utf-8'), ''.encode('utf-8')).strip()
            content_seg = jieba.cut(content)  # 为文件内容分词
            savefile(seg_dir+poet, ' '.join(content_seg).encode('utf-8'))  # 将处理后的文件保存到分词后语料目录

if __name__ == "__main__":
    #对训练集进行分词
    _poets_path = "训练诗集"  # 未分词分类语料库路径
    seg_path = "训练集分词"  # 分词后分类语料库路径
    corpus_segment(_poets_path,seg_path)

    _poets_path = "测试诗集"  # 未分词分类语料库路径
    seg_path = "测试集分词"  # 分词后分类语料库路径
    corpus_segment(_poets_path, seg_path)
