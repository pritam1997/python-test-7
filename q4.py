n = int(input("Enter no. : "))
sum =0
if n>0:
	for i in range(1,n+1):
		sum += i/(i+1)
else:
	print("Number must be greater than 0")
print(round(sum,2))