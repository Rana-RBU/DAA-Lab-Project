# SETUP
demand = [0, 5, 10, 7]  # 0-padding for 1-based indexing
order_cost = 50
hold_cost = 2

N = len(demand) - 1
dp = [0.0] * (N + 2)  # dp[i] = min cost from period i to N
plan = [0] * (N + 2)  # plan[i] = best 'j' (order until) for period i

# SOLUTION (Dynamic Programming)
for i in range(N, 0, -1):  # Loop backward from N down to 1
    min_cost = float('inf')
    best_j = i

    for j in range(i, N + 1):  # Test policies: Order in 'i' to cover 'i' thru 'j'

        # Calculate holding cost
        units_ordered = sum(demand[i:j + 1])
        leftover = units_ordered
        holding = 0.0
        for k in range(i, j + 1):
            leftover -= demand[k]
            holding += leftover * hold_cost

        cost = order_cost + holding + dp[j + 1]

        if cost < min_cost:
            min_cost = cost
            best_j = j

    dp[i] = min_cost
    plan[i] = best_j  # Store the best decision

# RESULTS
print(f"Problem Setup")
print(f"Demand:       {demand[1:]}")
print(f"Order Cost:   ${order_cost}")
print(f"Holding Cost: ${hold_cost}\n")

print(f"--- Optimal Cost ---")
print(f"Minimum Total Inventory Cost: ${dp[1]:.2f}\n")

print(f"--- Optimal Ordering Plan ---")
current_period = 1
inventory = 0
total_cost = 0

while current_period <= N:

    order_until_period = plan[current_period]
    units_to_order = sum(demand[current_period: order_until_period + 1])

    print(f"Period {current_period}:")
    print(f"  -> Place an Order for {units_to_order} units.")
    print(f"     (Covers demand for periods {current_period} to {order_until_period})")

    inventory += units_to_order
    total_cost += order_cost

    # Simulate the periods covered by this order
    for p in range(current_period, order_until_period + 1):
        inventory -= demand[p]
        period_hold_cost = inventory * hold_cost
        total_cost += period_hold_cost

        print(f"    - P{p} Demand: {demand[p]:<3} | Inv. End: {inventory:<3} | Hold Cost: ${period_hold_cost:<4.2f}")

    current_period = order_until_period + 1
    print("")

print(f"Plan complete. Total verified cost: ${total_cost:.2f}")
