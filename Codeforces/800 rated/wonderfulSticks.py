t = int(input())
for k in range(t):
    n = int(input())
    s = input()
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    for i in range(len(s)):
        if s[i] == "<" and arr[i+1] > arr[i]:
            arr[i:] = arr[i:][::-1]
        elif s[i] == ">" and arr[i+1] < arr[i]:
            arr[i:] = arr[i:][::-1]
        else:
            pass
    for a in range(len(arr)):
        print(arr[a], end=" ")       
    print("")         