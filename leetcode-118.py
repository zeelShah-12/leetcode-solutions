class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        outerArray = []
        for i in range(1,numRows+1):
            tempArray = [1]*i
            for j in range(1,i-1):
                tempArray[j] = outerArray[i - 2][j-1] + outerArray[i - 2][j]
            outerArray.append(tempArray)
        return outerArray