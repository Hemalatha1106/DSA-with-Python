s = "bbcd" # input string 
turn = 0
total = 0
for i in s:
    if i in 'aeiou':
        total += 1
s = list(s)
if total == 0:
    print(False)
    exit()
change = True
while change:
    curr_count = 0
    change = False
    if turn == 0:
        for i in range(len(s)):
            if s[i] in 'aeiou':
                curr_count += 1 
            if total%2 == 0 and curr_count == total - 1:
                s = s[i+1:]
                print(s)
                change = True
                turn = 1
                break
            elif curr_count == total:
                s = s[i+1:]
                print(s)
                change = True
                turn = 1
                break
    else:
        for j in range(len(s)):
            if s[j] in 'aeiou':
                curr_count += 1
            if curr_count%2 == 0:
                s = s[j+1:]
                print(s)
                turn = 1
                change = True
                break
if turn == 1:
    print(True)
elif turn == 0:
    print(False)

