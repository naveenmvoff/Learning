N = input("Enter the number only: ").split()
output = []
for i in N:
	try:
			if int(i) % 2 == 0:
				output.append("even")
			else:
				output.append("odd")
	except:
		continue
print(" ".join(output))