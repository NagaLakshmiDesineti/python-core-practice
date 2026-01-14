num=int(input("enter a number:"))
sum_digits=0
while num>0:
  sum_digits+=num%10
  num=num//10
print("sum of the digits:",sum_digits)
