def count_cal(word,temprory,count):
	
	if len(temprory) == count:
		print(temprory)
		return
	
	for i in word:
		count_cal(word, temprory + i, count)


word = input("Enter the value: ").split()
count = int(input("Enter the count: "))

count_cal(word, "",count)