#统计字符
def get_count(s,ch):
    count=0
    for item in s:
        if ch.upper()==item or ch.lower()==item:
            count+=1
    return count
if __name__ == '__main__':
    s='kdxjnvcxjnvx,m xkn kcn kxjn kx'
    for item in s:
        print(item,end='')
    print()
    ch=input('请输入要统计的字符:\n')
    count=get_count(s,ch)
    print(f'{ch}在字符{s}中出现的次数为:{count}')

