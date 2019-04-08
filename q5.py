n = int(input("Enter no. : "))
f=[]
for i in range(1,n+2):
	f.append(i)
print(f)

if n>0:
	f[n] = f[n-1] + 100
	print(f[n])
else:
	print("Number must be greater than 0")