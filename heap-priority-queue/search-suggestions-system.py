class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # we want to use 2 pointer approach 
        l, r = 0, len(products) - 1
        res = []

        #sort the product alphabetically 
        products.sort()

        #iterate through words 
        for i in range(len(searchWord)):
            #keep track of word in search word 
            search = searchWord[i]
            # check for both left pointer and right pointer
            #check if the word has prefix, if not move the pointer 
            while l <= r and (len(products[l]) <= i or products[l][i] != search ):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != search ):
                r -= 1

            #length of valid words 
            valid = r - l + 1 
            if valid >= 3:
                res.append([products[l], products[l+1], products[l+2]])
            elif valid == 2:
                res.append([products[l], products[l+1]])
            elif valid == 1:
                res.append([products[l]])
            else:
                res.append([])
        return res

            


        