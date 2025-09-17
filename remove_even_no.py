nums=list(map(int,input("Enter integers separated by space:").split()))
filtered=[n for n in nums if n % 2 !=0]
print("List after removing even numbers:",filtered)