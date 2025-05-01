class ParkingSystem:

    # three types of spaces = b, m, s
    #fixed slots 
    #number of slots in constructor 
    # carType => b-> 1, m -> 2, s -> 3
    # [[1,1,0], [1], [2], [3], [1]]
    # so first car is big, it goes to [0] index
    # so 1 car goes to [1-1] or [ carType -1]
    def __init__(self, big: int, medium: int, small: int):
        # declaring spaces 
        self.spaces = [big, medium, small]
        
    def addCar(self, carType: int) -> bool:
        if len(self.spaces) == 0:
            return False
        if self.spaces[carType - 1]: 
            self.spaces[carType -1] -=1 
            return True 
        return False

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)