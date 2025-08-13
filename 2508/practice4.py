s='My favourite Hardcore music is Grievous Lady'
x=s.find('e')
print(x)
y=s.find('G',x)   #从x的位置开始往后找'G'
print(y)
gl=s[y:y+14]
print(gl)