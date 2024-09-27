def reverse_product_value(input1, input2):
    
    x = input1[::-1]
    return sum([x[i] for i in range(input2) if i%2==0])

    # x = input1[::-1]
    # store = 0
    # for i in range(input2):
    #     if i % 2 == 0:
    #         store += i
        
    # return store

input1 = list(map(int, input("Enter the value: ").split()))
input2 = int(input())

result = reverse_product_value(input1, input2)

print(result)