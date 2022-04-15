import os
filename='student.txt'
def main():
    while True:
        menu()
        a=int(input('请选择'))
        if a in [1,2,3,4,5,6,7,8]:
            if a == 1:
                insert()
            elif a == 2:
                search()
            elif a == 3:
                delete()
            elif a == 4:
                modify()
            elif a == 5:
                sort()
            elif a == 6:
                total()
            elif a == 7:
                show()
            elif a == 8:
                answer=input('你确定要退出系统吗？y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用')
                    break
                else:continue
def menu():
    print('============================学生系统===============================')
    print('-------------------------1.录入学生信息-----------------------------')
    print('-------------------------2.csv.查找学生信息-----------------------------')
    print('-------------------------3.删除学生信息-----------------------------')
    print('-------------------------4.修改学生信息-----------------------------')
    print('-------------------------5.学生成绩排名-----------------------------')
    print('-------------------------6.统计学生总人数----------------------------')
    print('-------------------------7.显示全部学生信息--------------------------')
    print('-------------------------8.退出------------------------------------')
    print('==================================================================')
def insert():
    student_list=[]
    while True:
        id = input('请输入id：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = float(input('请输入英语成绩'))
            python = float(input('请输入python成绩'))
            k3=float(input('请输入k3成绩'))
        except:
            print('无效，请重新输入')
            continue
        #将录入的学生信息保存到字典
        student={'id':id,'name':name,'english':english,'python':python,'k3':k3}
        student_list.append(student)
        answer=input('是否继续添加？y/n\n')
        if answer=='y':
            continue
        else:
            break
    #调用save()方法函数
    save(student_list)
    print('学生信息录入完毕')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    student_query=[]
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as cfile:
            student_old = cfile.readlines()
    else:
        return
    student_id = input('请输入要查找的学生id')
    for item in student_old:
        d = dict(eval(item))  # 将字符串转成字典
        if d['id'] == student_id:
            student_query.append(d)
    show_student(student_query)
    answer = input('是否继续查找？y/n\n')
    if answer == 'y':
        search()
def delete():
    while True:
        student_id=input('请输入要删除的学生id')
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:student_old=[]
            flag=False #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item)) #将字符串转成字典
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show() #删除后要重新显示学生信息
            answer=input('是否继续删除？y/n\n')
            if answer=='y':
                continue
            else:
                break
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改的学生id')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))  # 将字符串转成字典
            if d['id'] == student_id:
                print('找到学生信息，可以修改')
                while True:
                    try:
                        d['name']=input('请输入姓名')
                        d['english'] = input('请输入英语成绩')
                        d['python'] = input('请输入python成绩')
                        d['k3'] = input('请输入k3成绩')
                    except:
                        print('输入有误，请重新输入')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改？y/n\n')
        if answer=='y':
           modify()
def sort():
    show()
    with open(filename,'r',encoding='utf-8') as rfile:
        student_list=rfile.readlines()
    student_new=[]
    for item in student_list:
        d=dict(eval(item))
        student_new.append(d)
    asc_or_desc=input('请选择升序0或者降序1\n')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode=input('请选择排序方式（1.按英语成绩排序）（2.csv.按python成绩排序）（3.按k3成绩排序）（4.按总成绩排序）')
    if mode=='1':
        student_new.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2.csv':
        student_new.sort(key=lambda x:int(x['python']),reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x:int(x['k3']),reverse=asc_or_desc_bool)
    elif mode=='4':
        student_new.sort(key=lambda x:int(x['english'])+int(x['python'])+int(x['k3']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_number = rfile.readlines()
        if student_number:
                print('一共有{}名学生'.format(len(student_number)))
    else:
        return
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('id', '姓名', '英语成绩', 'python成绩', 'k3成绩', '总成绩'))
    # 定义内容显示格式
    format_dada = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_dada.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('k3'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('k3'))))
def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_show = rfile.readlines()
        for item in student_show:
            student_list.append(eval(item))
        if student_list:
            show_student(student_list)
    else:
        print('暂未保存数据信息')
if __name__ == '__main__':
    main()