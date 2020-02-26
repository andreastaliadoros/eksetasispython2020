f=open("input1.txt","r")
grammi="b"
i=0
c1=0
c2=0
while line!="":
		grammi=f.readline().strip()
		for i in range (len(grammi)):
			if ((grammi[i]=="f") or (grammi[i]=="c") or (grammi[i]=="k") or (grammi[i]=="r")):
				c1=c1+1			
			else:
				c2=c2+1
				if (grammi[i]==" "):
					if (c1>c2-1):
						print("BAD")
						c1=0
						c2=0
					else:
						print("GOOD")
						c1=0
						c2=0
if (c1<=c2):
	print("Good")
else:
	print("Bad")