def det(mx, mul):
    width = len(mx)
    if width == 1:
        return mul * mx[0][0]
    else:
        sign = -1
        ans = 0
        for i in range(width):
            mx1 = []
            for j in range(1, width):
                temp = []
                for k in range(width):
                    if k != i:
                        temp.append(mx[j][k])
                mx1.append(temp)
            sign *= -1
            ans += mul * det(mx1, sign * mx[0][i])
        return ans



matrix = [[1,28,87],[4,58,4],[1,2,3]]
width = len(matrix)
for l in range(0,width):
    if len(matrix[l])!= width:
        print("Not a square matrix")
        flag=0
        break
    else:
        flag=1
        pass
if (flag==1):
    print(det(matrix, 1))
else:
    pass   







#     def solve(matrix, mul):
#     width = len(matrix)
#     if width == 1:
#         return mul * matrix[0][0]
#     else:
#         sign = -1
#         total = 0
#         for i in range(width):
#             m = []
#             for j in range(1, width):
#                 buff = []
#                 for k in range(width):
#                     if k != i:
#                         buff.append(matrix[j][k])
#                 m.append(buff)
#             sign *= -1
#             total += mul * solve(m, sign * matrix[0][i])
#         return total

# matrix = [[1,-2,3],[0,-3,-4],[0,0,-3]]
# print(solve(matrix, 1))