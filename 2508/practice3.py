#搜索字符串
s='dabcabc'
x=s.find('c') #查找
print(x) #查找第一个'c'并返回位置

y=s.replace('a','x') #替换
print(y) #输出的是替换过后的结果

s=' dabcabc '
a=s.lstrip() #删掉左边的空格和其他不可见字符，以下同理
b=s.rstrip() #删掉右边的空格
c=s.strip() #删掉两边的空格
print(a)
print(b)
print(c)

s='dabcabc'
a=s.startswith('d')
b=s.startswith('g')
print(a)
print(b)


