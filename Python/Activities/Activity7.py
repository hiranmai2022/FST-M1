numbrs=list(input("enter numbers seperated with comma:").split(", "))
sum=0
for num in numbrs:
    sum+= int(num)
    if(sum==10):
        exit
    print(sum)


