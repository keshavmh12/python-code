row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where you want hide your money?")
row_position=int(position[0])
col_position=int(position[1])
selected_row=matrix[row_position-1]
selected_row[col_position-1]=0
print(f"{row1}\n{row2}\n{row3}")