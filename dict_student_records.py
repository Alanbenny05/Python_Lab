students={"Anu":[85,90,78],"Gowri":[72,88,91],"Vishnu":[95,80,85]}
for name,marks in students.items():
    total=sum(marks)
    avg=total/len(marks)
    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Total Marks: {total}")
    print("."*20)