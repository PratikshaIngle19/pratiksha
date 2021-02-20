# nested_list = [[1,2,3], [4,5,6], [7,8,9]]

# num1 = nested_list[0][1]

# num2 = nested_list[2][2]
# num3 = nested_list[-2][-1]
# num4 = nested_list[-2][-2]
# print(num1)
# print(num2)
# print(num3)
# print(num4) 


#program 1 of nested list using for loop without LC
# nested_list = [[1,2,3], [4,5,6], [7,8,9]]

# for num in nested_list:
    
#     print(num)


#program 1 of nested list using for loop without LC
# nested_list = [[1,2,3], [4,5,6], [7,8,9]]

# for num in nested_list:
#     for val in num:
#         print(val)


#program of nested list uding LIST COMPREHENSION
# nested_list = [[1,2,3], [4,5,6], [7,8,9]]
# [[print(val) for val in num]for num in nested_list]

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)


board = [['X'] for num in range(1,4)]
print(board)

#tiktakto = [["X" if val %2 != 0 else "O" for val in range(1,4)]for num in range(1,4)]
#print(tiktakto)


