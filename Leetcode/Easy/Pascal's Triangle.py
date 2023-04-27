class Solution(object):
    def generate(self, numRows):
        ret = [[1]]
        for i in range(1, numRows):
            temp = [0] + ret[-1] + [0]
            newRow = []
            for j in range(len(temp) - 1):
                newRow.append(temp[j] + temp[j + 1])
            ret.append(newRow)
        return ret
