nums=list(map(int,input("Enter integer seperated by space:").split()))
result=["over" if n>100 else n for n in nums]
print("Processed list",result)