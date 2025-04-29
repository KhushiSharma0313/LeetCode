class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp - boundless knapsack approach
        #since amount is changing, let's make a 1d array of amount
        #we start at 0, with 0 amount - base case
        #then end at last elemnt of array with number  of coins 
        #since we want to find min number of coins, let's declare it to be max 

        dp = [amount+1]*(amount+1) #the values and size both are amount +1 
        dp[0] = 0 #since 0 coins equals 0 money 

        for a in range(1,amount+1):
            for c in coins:
                if a-c >=0:
                    dp[a] = min(dp[a], 1+dp[a-c]) #here 1 is amount of coin, and a-c is remaining amount 
        
        if(dp[amount] == amount+1): #if it remains to default, there's no coins that can fulfill req and so -1
            return -1
        
        return dp[amount]


        # for each coin, we have 2 choices, do we add it or leave it 
        # if we add it, it affects our total, but doesn't afect coins, since we have infinite
        # if we don't add it, it doesnt affect anything and we move to next coin 

        #brute force is going down this decision tree of adding and not adding of each coin
        #each coin will have n choices(len of coins) and some choices are getting repated
        #so instead of going down this tree through dfs and recursion, let's check another approach 
        