class Solution:
    def slope(self,x,y):
        if (x[0]-y[0]==0):
            return 0
        return (float(y[1]-x[1])/(y[0]-x[0]))
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        gslope = self.slope(coordinates[0],coordinates[1])
        print(gslope)
        i=2
        for i in range(2,len(coordinates)):
            slop = self.slope(coordinates[0],coordinates[i])
            if slop!=gslope:
                return False
        return True
