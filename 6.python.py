def fibonacci(input1):
    
    res = [0]*(input1 + 1)
    res[0] = 1
    res[1] = 1
    for i in range (2, input1 + 1):
        res[i] = res[i -1] * res[i - 1] + res[i - 2] * res[i - 2]
    return res[input1]

input1 = int(input())

result = fibonacci(input1)
print(result)