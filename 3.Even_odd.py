def counting(a,b):

    limit = min(b, len(a))

    store = []

    for i in range(limit):
        if i % 2 ==0:
            store.append("Even")
        else:
            store.append("Odd")
    return " ".join(store)



input1 = list(map(int, input().split()))
input2 = int(input())

result = counting(input1, input2)
print(result)