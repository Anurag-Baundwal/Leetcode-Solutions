# Problem title: 1647 Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # accounts [i][j] - i is the customer number and j is the bank number
        
        # METHOD 1
        # max_wealth = 0
        # for customer in accounts:
        #     wealth = sum(customer)
        #     if wealth >= max_wealth:
        #         max_wealth = wealth
            
        # return max_money

        # METHOD 2
        wealths = [sum(accounts[i]) for i in range(len(accounts))]
        return max(wealths)
