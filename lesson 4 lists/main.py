
name=["dion","peter","james","jaimy"]

print(name)
print(name[-2])
name.append("diony")
print(name)
print(len(name))
name.pop()
print(name)
name.pop(1)
print(name)

#2d list

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print("Number of rows : ", len(matrix))
print("Number of columns :", len(matrix[0]))
print(matrix[1][1])
print(matrix[2][0])

#print 2d list matrix
for i in range(3) :
    for j in range(3):
        #"" for a gap
        print(matrix[i][j], end= " ")
        #print new line
    print("\n")

row=int(input("how many rows do you want?"))
colum=int(input("how many colums do you want?"))

matrix1 = [] #hold all the vallues
for i in range(row):
    temp = [] #hold elements in row wise
    for j in range(colum):
        x = int(input("enter the element :"))
        temp.append(x)
    matrix1.append(temp)

for i in range(row):
    for j in range(colum):
        print(matrix1[i][j], end= " ")
    print("\n")

n=int(input("enter the dimensions of the matrix!"))
matrix2 = []
for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("enter the element :"))
        temp.append(x)
    matrix2.append(temp)

for i in range(n):
    for j in range(n):
        print(matrix2[i][j], end=" ")
    print("\n")

#to print diagnal elements
for i in range(n):
    print(matrix2[i][i])

#maatrix addition
matrixa=[[1,2,3],[4,5,6]]
matrixb=[[7,8,9],[10,11,12]]

result=[[0,0,0],[0,0,0]]
for i in range(2):
    for j in range(3):
        result[i][j]=matrixa[i][j]+matrixb[i][j]


for i in range(2):
    for j in range(3):
        print(result[i][j], end= " ")
    print("\n")
#matrix subtraction
result2=[[0,0,0],[0,0,0]]

for i in range(2):
    for j in range(3):
        result2[i][j]=matrixa[i][j]-matrixb[i][j]

for i in range(2):
    for j in range(3):
        print(result2[i][j], end= " ")
    print("\n")


