class Solution(object):
    global ret
    ret = [[1]]
    for i in range(1, 34):
        temp = [0] + ret[-1] + [0]
        newRow = []
        for j in range(len(temp) - 1):
            newRow.append(temp[j] + temp[j + 1])
        ret.append(newRow)

    def getRow(self, rowIndex):
        return ret[rowIndex]
