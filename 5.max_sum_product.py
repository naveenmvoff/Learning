def max_sum_product(input1, input2):
    
    
    max_pro = 0
    arr = input2
    res = []
    for i in range(input1 - 1):
        for j in range(i+1, input1):
            if arr[i] + arr[j] == 18:
                temp = arr[i] * arr[j]
                if temp >= max_pro:
                    max_pro = temp
                    res = sorted([arr[i], arr[j]], reverse = True)
    return res


input1 = int(input("Enter the number: "))
input2 = list(map(int, input("Enter the list of number: ").split()))

result = max_sum_product(input1, input2)
print(result)