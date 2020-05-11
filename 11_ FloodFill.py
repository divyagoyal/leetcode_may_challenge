class Solution:
    def floodFillRecursive(self,image, sr: int, sc: int, prevColor: int, newColor: int, m: int, n: int,mat):
        if sr < 0 or sr >= m or sc < 0 or sc >= n:
            return
        if image[sr][sc] != prevColor:
            return
        if mat[sr][sc]==-1:
            image[sr][sc] = newColor
            mat[sr][sc]=1
            self.floodFillRecursive(image, sr, sc - 1, prevColor, newColor, m, n, mat)
            self.floodFillRecursive(image, sr, sc + 1, prevColor, newColor, m, n, mat)
            self.floodFillRecursive(image, sr - 1, sc, prevColor, newColor, m, n, mat)
            self.floodFillRecursive(image, sr + 1, sc, prevColor, newColor, m, n,mat)
        else:
            return

    def floodFill(self, image, sr: int, sc: int, newColor: int):
        m = len(image)
        n = len(image[0])
        prevColor = image[sr][sc]
        mat = [[-1 for x in range(n)] for y in range(m)]
        self.floodFillRecursive(image, sr, sc, prevColor, newColor, m, n,mat)
        return image
    

        
        
