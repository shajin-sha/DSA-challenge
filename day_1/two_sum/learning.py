codes = [1,2,3,4]
target = 7

for i in range(len(codes)):
    for j in range(i):
        # print(codes[i],codes[j])
        if(codes[i]+codes[j]==target):
            print(j,i)
        else:
            continue;