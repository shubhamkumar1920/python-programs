size=int(input("Enter the size of the array :").strip())
l=list(map(int,input("Enter the list elements by space - separated sequence :").strip().split()))[:size]
y=sorted(set(l))
y.sort()
x=(y[-2]+y[1])
print(f"The summation is : {x}")