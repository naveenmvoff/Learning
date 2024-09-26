def diffrent(in1, in2):
    
    s = 0
    x = 0
    arr = input2
    for i in range(input1):
        if i % 2 == 0:
            x = x^arr[i]
        else:
            s += arr[i]
    return s - x

input1 = int(input())
input2 = list(map(int, input().split()))

result = diffrent(input1, input2)
print(result)