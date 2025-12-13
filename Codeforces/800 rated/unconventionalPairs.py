print((200+200+300+500+600+600)//6)
exit()
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    m = float('-inf')
    for j in range(0,len(arr)-1,2):
        if arr[j] - arr[j+1] > m:
            m = arr[j]-arr[j+1]
    print(m)        