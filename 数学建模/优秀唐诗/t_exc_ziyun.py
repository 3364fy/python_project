from wordcloud import WordCloud
import matplotlib.pyplot as plt
# 生成词云
def create_word_cloud():
    frequencies = {}
    for line in open("t_exc_zipin.txt", encoding='utf-8'):
        arr = line.split("\t")
        frequencies[arr[0]] = float(arr[-1].split('\n')[0])
    # 支持中文, SimHei.ttf可从以下地址下载：https://github.com/cystanford/word_cloud
    wc = WordCloud(
        font_path="../word_cloud-master/SimHei.ttf",
        max_words=100,
        width=2000,
        height=1200,
    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("t_exc_ziyun.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()
# 根据词频生成词云
create_word_cloud()