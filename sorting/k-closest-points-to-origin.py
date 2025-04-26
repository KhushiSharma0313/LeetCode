class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # point = xi, yi 
        # distance from origin formula is given 
        # k is integer, number of points 
        # can there be same distance, if yes which comes first 

        #input is list of lists 
        # output is list of lists 

        # distance array  = stores the dist of each coordinate from origin, also store the coordinates 
        # we sort the dist based on dist descending order, so that last one can just pop out
        # based on k, we return that many coordinates 

        # declaring arrays 
        distance = []
        res = []

        # iterating through points 
        for x, y in points:
            dist = sqrt(x**2 + y**2) # distance from origin formula
            distance.append([dist, x, y]) #adding distance and coordinates 

        #sort 
        distance.sort(key=lambda x: (-x[0]))

        #based on k 
        while k >0:
            dist, x, y = distance.pop() #getting last positoon data, meaning min data 
            res.append([x,y])
            k -=1
            
        return res 




        