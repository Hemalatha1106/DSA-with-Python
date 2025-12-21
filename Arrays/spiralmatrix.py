matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
row = len(matrix)
col = len(matrix[0])
top = 0
bot = row-1
left = 0
right = col-1
res = []
while top <= bot and left <= right:
    #left->right
    for n in range(left,right+1):
        res.append(matrix[top][n])
    top += 1
    for n in range(top,bot+1):
        res.append(matrix[n][right])
    right -= 1
    if top <= bot: 
        for n in range(right,left-1,-1):
            res.append(matrix[bot][n])
        bot -= 1
    if left <= right:
        for n in range(bot,top-1,-1):
            res.append(matrix[n][left])
        left += 1
print(res)                    