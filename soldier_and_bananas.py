k,n,w=map(int,input().split())
if 1<=k and w<=1000 and 0<=n<=10**9:
    w_price=0
    for i in range(w):
        w_price+=((i+1)*k)
    if n<=w_price:
        print(w_price-n)
    else:
        print("0")