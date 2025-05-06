class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # after each word, it should check prefix in the words and then sort alphabetically 
        # with prefix, once we have words with searchWord[0] = those are the only words we'll need
        # two pointer 
        # start at first positon, and last position
        # keep checing if it was prefix 
        # if does great! 
        # if it does not, move the pointer 
        # in those valid words choose top 3 

        products.sort()

        l, r = 0, len(products) -1
        res =[]

        for i in range(len(searchWord)):
            #if left pointer word doesn't match prefix 
            while l <= r and (len(products[l])<= i or products[l][i] != searchWord[i]):
                l +=1

            while l <= r and (len(products[r])<= i or products[r][i] != searchWord[i]):
                r -=1
                # if right pointer word doesn't match prefix
                
                # pick top 3 
            words = r - l +1

            if words > 3:
                res.append([products[l],products[l+1], products[l+2]])
            elif words ==2:
                res.append([products[l], products[l+1]])
            elif words ==1:
                res.append([products[l]])
        
        return res



# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         # we want to use 2 pointer approach 
#         l, r = 0, len(products) - 1
#         res = []

#         #sort the product alphabetically 
#         products.sort()

#         #iterate through words 
#         for i in range(len(searchWord)):
#             #keep track of word in search word 
#             search = searchWord[i]
#             #check for both left pointer and right pointer
#             #check if the word has prefix, if not move the pointer 
#             while l <= r and (len(products[l]) <= i or products[l][i] != search ):
#                 l += 1
#             while l <= r and (len(products[r]) <= i or products[r][i] != search ):
#                 r -= 1

#             #length of valid words 
#             valid = r - l + 1 
#             if valid >= 3:
#                 res.append([products[l], products[l+1], products[l+2]])
#             elif valid == 2:
#                 res.append([products[l], products[l+1]])
#             elif valid == 1:
#                 res.append([products[l]])
#             else:
#                 res.append([])
#         return res

            


        