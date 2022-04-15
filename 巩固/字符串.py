s='hello,world'
print(s.isidentifier())
print('hello'.isidentifier())#判断是否为合法字符
print('\t'.isspace())#判断是否由空白字符组成（）
print('abc'.isalpha())
print('张三'.isalpha())#判断是否由字母组成
print('123'.isdecimal())#判断是否为十进制数字
print('1562'.isnumeric())
print('3135六'.isnumeric())#判断是否由数字组成
print('asda4'.isalnum())#是否全部由字母或数字组成
a=input('请输入支付密码：\n')
print('支付数据合法' if a.isdigit() else '支付数据不合法')