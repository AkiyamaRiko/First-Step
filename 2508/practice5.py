xfile=open('D:/PyCharm/Projects/Practice/2508/1.txt','r') #打开文件 #注意：路径要用正斜杠！
a=0
for line in xfile:
    a=a+1
    print(a,' ',line)  #统计行数

xfile=open('D:/PyCharm/Projects/Practice/2508/1.txt','r')
inp=xfile.read()  #这一步读取了文件，然后把它作为字符串赋值给了inp。
print('Length:',len(inp))   #输出了inp的长度，也就是文件的字数。

xfile=open('D:/PyCharm/Projects/Practice/2508/1.txt','r')
for line in xfile:
    if line.startswith('Parsley'):
        print(line.rstrip())  #print一行字的时候，会自动空行。用rstrip可以删掉后面的空行。
    else:
        print ('------------')
#每操作一次要重新读一次文件

xfile=open('D:/PyCharm/Projects/Practice/2508/1.txt','r')
inp=xfile.read() 
s=inp.split()
print(len(s))