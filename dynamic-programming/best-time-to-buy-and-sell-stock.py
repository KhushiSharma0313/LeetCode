class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        n = len(prices)
        maxP = 0
        profit = 0

        #until sell is not out of bounds
        while sell< n:
            profit = prices[sell] - prices[buy]
            #that's when it's not profitable 
            if prices[buy] > prices[sell]:
                buy +=1
            elif profit > maxP:
                maxP = profit 
            else:
                sell +=1
        return maxP



        # #time = O(n)
        # # space = O(1)
        # # price i is price on ith day 
        # # max prodit = day to buy stock and day to sell stock 
        # # return max profit or 0 

        # # example 
        # # 7,1,5,3,6,4
        # # buying stock = min 
        # # selling stock = max 
        # # order matters, so sorting won't work 
        # # keep track of min, and then choose next stock, calc it's profit
        # # then move to next stock and see if profit is more or less
        # # if profit is more than before, than swtich to this stock 
        # #do this for both buy and sell stock 
        # #start from left and right
        # #move inwards whenever the profit is more than before 

        # n = len(prices)
        # buy, sell = 0, 1 #two pointers starting in edges or list 
        # maxP = 0 
        # profit = 0

        # #while it's sell is in bounds 
        # while sell < n:
        #     #basic formula of profit
        #     profit = prices[sell] - prices[buy]

        #     #if it's value is in nagative or if its loss, we move buy 
        #     if prices[sell] < prices[buy]:
        #         # buy +=1
        #         #instead of moving it by one, move it to buy price, since it's lower 
        #         buy = sell
            
        #     #if current is more than max, then assign max to current 
        #     elif profit > maxP:
        #         maxP = profit
        #     #if profit is not more than prev, move to diff sell value 
        #     else:
        #         sell +=1
        # return maxP




        