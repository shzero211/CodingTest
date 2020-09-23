input_data=input()
row=int(input_data[1])
colum=int(ord(input_data[0]))-int(ord('a'))+1

move=[(2,1),(-2,-1),(2,-1),(-2,1),(1,2),(-1,-2),(1,-2),(-1,2)]

result=0
for moving in move:
    next_row=row+moving[0]
    next_colum=colum+moving[1]
    if next_row>=1and next_row<=8and next_colum>=1 and next_colum<=8:
        result+=1
print(result)
