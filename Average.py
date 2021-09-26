n=int(input())
total=0
inp=input()
num=inp.split()
for x in num:
    number=int(x)
    total=total+number
#print(total/n)
avg=total/n
#print('%.2f'%avg) 
#print(round(avg,2))
print ("{0:.2f}".format(avg)) 