# Print all possible coordinates (i,j,k), i + j + k != n
# where 0<i<x , 0<j<y , 0<k<z

x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            kordinat = []
            sum = i + j + k
            if sum != n:
                kordinat.append(i)
                kordinat.append(j)
                kordinat.append(k)
                coordinates.append(kordinat)

print(coordinates)

