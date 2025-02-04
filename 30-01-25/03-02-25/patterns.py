#number pyramid
print("number pyramid")
for i in range(0,4):
    num=1
    for j in range(0,4):
        if i>=j :
            print(num,end=" ")
            num+=1
    print()
#zeros and ones triangle
print("zeros and ones triangle")
n=4
for i in range(n):
    start=i%2
    for j in range(i+1):
        print(1-((start+j)%2),end=" ")
    print()
#rhombus pyramid
print("rhombus pyramid")
for i in range(0,5):
    print(" " * i + "* "*5)