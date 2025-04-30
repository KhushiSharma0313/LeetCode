class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # price i is price on ith day 
        # max prodit = day to buy stock and day to sell stock 
        # return max profit or 0 

        # example 
        # 7,1,5,3,6,4
        # buying stock = min 
        # selling stock = max 
        # order matters, so sorting won't work 
        # keep track of min, and then choose next stock, calc it's profit
        # then move to next stock and see if profit is more or less
        # if profit is more than before, than swtich to this stock 
        #do this for both buy and sell stock 
        #start from left and right
        #move inwards whenever the profit is more than before 

        n = len(prices)
        buy, sell = 0, 1 #two pointers starting in edges or list 
        profit = 0 
        temp = 0

        for i in range(n):
            if sell< n:
                if sell < buy:
                    buy +=1
                    sell +=1
                temp = prices[sell] - prices[buy]
                if temp > profit:
                    profit = temp 
                else:
                    buy +=1
                    sell +=1
        return profit




        