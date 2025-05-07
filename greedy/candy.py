class Solution:
    def candy(self, ratings: List[int]) -> int:
        #base case everyone has one candy 
        arr = [1] *len(ratings)

        #left to right
        #skipping 1st element, since it does not have a left neighbour
        for i in range(1,len(ratings)):
            #if left neigbour has less rating, curr gets 1more candy 
            if ratings[i] > ratings[i-1]:
                arr[i] = 1 + arr[i-1]
        #right to left 
        for i in range(len(ratings) -2, -1, -1):
            #if right neigbour has less candy, curr gets 1 more candy if it's min with before candy 
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i], 1+ arr[i+1])
        
        #return sum of all the candies 
        return sum(arr)


# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         #child in line 
#         # rating value in array ratings 
#         # req - each child one candy 
#         # child with high rating than neghbour gets more candy 
#         # min number of candies 

#         #brute force would be checking each elements neighbour, then comparing if larger count of candy is increased
#         # for each element compare with its neighbours, then come back to left to fixmistakes
#         # so time = O(n^2) 
#         #
#         # first go from left to right and only check elements left neigbour and give candy accordingly 
#         # then go right to left, but check elements right neigbour and give candy if needed (if neigbour has more rating but not more candy)
#         # so time = O(n) and meory = O(1)

#         # for candy 
#         arr = [1]* len(ratings)

#         #first pass - comparing left neighbour, and going left to right 
#         for i in range(1, len(ratings)):
#             if ratings[i] > ratings[i-1]:
#                 arr[i] = 1 + arr[i-1]
        
#         #second pass, going right to left, comparing right neigbours
#         for i in range(len(ratings)-2, -1, -1):
#             if ratings[i] > ratings[i+1]:
#                 arr[i] = max(arr[i], 1 + arr[i+1])

#         #return sum of the candies 
#         return sum(arr)
        