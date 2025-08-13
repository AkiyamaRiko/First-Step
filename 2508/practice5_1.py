xfile=open('D:/PyCharm/Projects/Practice/2508/1.txt','r') #打开文件 #注意：路径要用正斜杠！
a=0
for line in xfile:
    a=a+1
    print(a,' ',line)
inp=xfile.read()  #这一步读取了文件，然后把它作为字符串赋值给了inp。
print('Length:',len(inp))   #输出了inp的长度，也就是文件的字数。
for line in xfile:
    if line.startswith('Parsley'):
        print(line)
    else:
        print ('------')