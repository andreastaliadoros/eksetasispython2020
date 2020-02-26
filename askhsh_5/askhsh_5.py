f=open("file.txt","r")
grami=f.readline().strip()
j=1
leksi=""
while grami!="":
	for j in range (len(grami)-1):
		leksi=leksi+grami[j]
		if (grami[j]==" "):
			if (len(leksi)>3):
				leksi=leksi[0:len(leksi)-1]+leksi[0]+"ay"
				leksi=leksi[1:len(leksi)]
				print(leksi)
				leksi=""
			else:
				print(leksi)
				leksi=""
	grami=f.readline().strip()
if (len(leksi)>3):
	leksi=leksi+leksi[0]+"ay"
	leksi=leksi[1:len(leksi)]
	print(leksi)
else:
	print(leksi)