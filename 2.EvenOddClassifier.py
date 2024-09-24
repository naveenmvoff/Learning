def check_value(val, mini):
    limit = min(mini, len(val))
    store = []
    try:
        for i in range(limit):
            if i % 2 == 0:
                store.append("even")
            else:
                store.append("odd")
    except Exception as e:
        print(f"An error occurred: {e}")  

    return " ".join(store)  

value = input("Enter: ").split()
minimum = int(input("Enter: "))

result = check_value(value, minimum)  
print(result)
