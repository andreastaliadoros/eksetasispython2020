num=input("Enter num: ")
telikonum=num
sum=15
while sum>9:
	sum=0
	telikonum=telikonum*3+1
	while telikonum!=0:
		sum=sum+telikonum%10
		telikonum=telikonum/10
	if telikonum==0:
		telikonum=sum
print(sum)