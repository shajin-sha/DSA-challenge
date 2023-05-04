# Inputs 

list_one = [2,4,3]
list_two = [5,6,4]

carry = 0

outputs = []


for i in range(len(list_one)):
    # outputs.append(list_one[i]+list_two[i])
    result = list_one[i]+list_two[i]
    if(len(str(result)) == 2):
        carry = result[1]
        outputs.append(list_one[i][0]+list_two[i])
        result = 0
    else:
        print(result)
        result = 0

print(outputs)