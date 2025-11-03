demand = [0,5,10,7]
N = len(demand)-1
order_cost = 50
hold_cost = 2

dp = [0]*(N+2)  # dp[i] = min cost from period i to N

for i in range(N,0,-1):
    min_cost = float('inf')
    for j in range(i,N+1):
        units_ordered = sum(demand[i:j+1])
        leftover = units_ordered
        holding = 0
        for k in range(i,j+1):
            leftover -= demand[k]
            holding += leftover * hold_cost
        cost = order_cost + holding + dp[j+1]
        if cost < min_cost:
            min_cost = cost
    dp[i] = min_cost

print("Minimum Total Inventory Cost:", dp[1])
