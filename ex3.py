
print('\n\n\n--------------- homework:4-3 ---------------')
start=int(input('請輸入起始值:'))
end=int(input('請輸入終止值:'))
sum =0
for i in range(start,end+1) :sum += i # sum = sum + i
print('總和=',sum)

print('\n\n\n--------------- homework:4-4 ---------------')
n=int(input('輸入購買商品數量:'))
sum = 0
for i in range(n) : sum+=int(input(f'請輸入第{i+1}樣商品價格:'))

print(f'總共花了{sum}元')

print('\n\n\n--------------- homework:4-5 ---------------')
n=int(input('請輸入一個整數:'))
for i in range(1,n+1) :
    if i % 5 ==0 : print(i)

print('\n\n\n--------------- homework:4-6 ---------------')
sumOdd =0
sumEven =0
n=int(input('請輸入一個整數:'))
for i in range(1,n+1) :
    if i % 2 : sumOdd += i
    else : sumEven += i
print(f'奇數總和為{sumOdd}\n偶數總和為{sumEven}')


print('\n\n\n--------------- homework:plus ---------------')
import sys

n=int(input('請輸入要輸入幾個數字:'))
max = -sys.maxsize-1 #;print(max)

for i in range(n) : 
    x=int(input(f'請輸入第{i+1}個數字:')) 
    if max < x : max = x

print('最大值是',max)
