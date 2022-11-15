#лаба4-задание4
#Даны три числа. Найти сумму двух наибольших из них.
a=int(input())
b=int(input())
c=int(input())
#находим наименьшее
m=a if a<b else b 
m=m if m<c else c 
summa=a+b+c-m
print(summa)

