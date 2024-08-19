t = int(input())
for i in range(t):
    n=int(input())
    string=input()
    print(string, n)
                                             #abc   bac          abcd b    a  cd       a cd        bacd
    ans=""
    right=""
    left = ""
    for j in range(n):
        if j == n//2:
            ans+=string[j]
            print(ans)
            for k in range(n//2):
                right+=string[k]
                print(right)
                

