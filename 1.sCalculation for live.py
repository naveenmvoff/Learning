def sweets_required(coco,eat,day):
     
    sweets_required = eat*day

    if sweets_required >= coco:
        return "no, Survival is impossible"
    elif sweets_required < coco:
        return "Yes, Survival is possible"
    
coconut_count = int(input("Coconut Required: "))
eat = int(input("Food required: "))
days = int(input("Days to alive: "))

Value = sweets_required(coconut_count,eat,days)
print(Value)
