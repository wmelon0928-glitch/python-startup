a=int(input('請輸入第一個邊長'))
b=int(input('請輸入第二個邊長'))
c=int(input('請輸入第三個邊長'))
if a+b>c and a+c>b and b+c>a :
    if a==b and b==c :
        print('正三角形')
    elif a==b or b==c or a==c :
        print('等腰三角形')
    else :
        print('一般三角形')
else :
    print('無法構成三角形')