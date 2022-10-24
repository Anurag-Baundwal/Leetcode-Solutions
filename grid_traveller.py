def grid_traveller (m: int, n: int, memo: dict):
    key = str(m) + ',' + str(n)
    if key in memo: return memo[key]
    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0
    memo[key] = grid_traveller(m-1,n, memo) + grid_traveller(m, n-1, memo)
    return memo[key]

    #return grid_traveller(m-1,n) + grid_traveller(m, n-1)


print(grid_traveller(499,499, {}))