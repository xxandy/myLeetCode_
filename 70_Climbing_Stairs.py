def climbStairs(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return climbStairs(n-1)+climbStairs(n-2)

#再帰アルゴリズムではフィボナッチの時間複雑度がO((1+√5)/2)
#動的計画法っぽく書いてみる
