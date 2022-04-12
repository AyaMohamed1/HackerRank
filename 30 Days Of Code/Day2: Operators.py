def solve(meal_cost, tip_percent, tax_percent):
    total_cost = (tax_percent + tip_percent + 100) * meal_cost / 100
    print(round(total_cost))

solve(12, 8, 20)