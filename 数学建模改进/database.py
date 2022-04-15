import pymysql
import json
import os


def poet(path,dynasty):
    database = pymysql.connect(host="localhost", user="root", password="33649464", database="math", charset='utf8mb4')
    # 初始化指针
    cursor = database.cursor()
    files=os.listdir(path)
    id=64298
    for file in files:
        with open(f'{path}/{file}','r',encoding='utf-8') as fp:
            json_data=json.load(fp)
        for item in json_data:
            title=item['title']
            author=item['author']
            content_list=item['paragraphs']
            content=''.join(content_list)
            #sql = "insert into poet (id,dynasty,authors,contents) values ('%s','%s','%s','%s')" % (ids,dynastys,authors,contents)
            sql = f"insert into poet (id,dynasty,title,author,content) values ('{id}','{dynasty}','{title}','{author}','{content}')"
            cursor.execute(sql)
            database.commit()
            id+=1
    database.close()

if __name__ == '__main__':
    pass
    # path1 = r'E:\math\唐诗'
    # poet(path1,'唐')
    # path2=r'E:\math\宋诗'
    # poet(path2, '宋')






