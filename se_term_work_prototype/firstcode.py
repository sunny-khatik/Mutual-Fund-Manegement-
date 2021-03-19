t=int(input())
for _ in range(t):
    s=input()
    x, y=0,0
    for i in s:
        if "x" == s[i]:
            x+=1
        elif 'y' == s[i]:
            y+=1
    if( x >= y):
        print(y)
    else:
        print(x)

