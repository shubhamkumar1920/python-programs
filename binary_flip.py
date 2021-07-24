n=list(input("Enter the binary string :").strip())
l=[]
for ele in range(0,len(n),2):
    if n[ele]=='0':
        n[ele]='1'
    elif n[ele]=='1':
        n[ele]='0'
for ele in n:
    l.append(ele)
t="".join(map(str,l))
print(f"After fliping the alternate digits, the string is : {t}")