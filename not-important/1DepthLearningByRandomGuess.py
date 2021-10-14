import random


class Data():

    def __init__(self, info):
        self.info = info

    def readInInfo(self, fname):
        print("not done yet")
    def getInfo(self):
        return self.info
    def getRows(self): # how many tall
        return len(self.info)
    def getColumns(self): # how many on wide
        return len(self.info[0])
    def getValueAt(self, rowNum, colNum):
        return self.info[rowNum][colNum]
    def getResultForRow(self, rowNum):
        return self.info[rowNum][len(self.info[rowNum]) - 1]




class AI():

    def __init__(self):
        self.data = []
        self.VeryBestWeights = []
        self.VeryBestValueDifAvg = 1.0

    def learn(self, numberOfTests):
        bestWeights = []
        bestValueDifAvg = 1.0

        for testNum in range(numberOfTests):
            weights = []
            print("\n\nTest Number: %i" % testNum)
            for colNum in range(self.data.getColumns() - 1):
                weight = random.random()
                weights.append(weight)
                print(" %f" % weight, end="")
            print("")
            totalValueDif = 0.0
            for rowNum in range(self.data.getRows()):
                sum = 0.0
                for colNum in range(self.data.getColumns() - 1):
                    sum = sum + weights[colNum] * self.data.getValueAt(rowNum, colNum)
                print("sum: %f" % sum)
                print("want: %i" % self.data.getResultForRow(rowNum))
                valueDif = abs(sum - self.data.getResultForRow(rowNum))
                print("dif: %f" % valueDif)
                totalValueDif = totalValueDif + valueDif
            valueDifAvg = totalValueDif / (self.data.getColumns() - 1)
            print("Average dif: %f" % valueDifAvg)
            if valueDifAvg < bestValueDifAvg:
                bestValueDifAvg = valueDifAvg
                bestWeights = weights
        
        if bestValueDifAvg < self.VeryBestValueDifAvg:
            self.VeryBestValueDifAvg = bestValueDifAvg
            self.VeryBestWeights = bestWeights

        print("\n\n\nlearning finished!")

    def predictRow(self, row):
        sum = 0
        for colNum in range(self.data.getColumns() - 1):
            sum = sum + self.VeryBestWeights[colNum] * row[colNum]
        value = round(sum)
        print("Sum: %f" % sum)
        print("Value: %i" % value)
        return value
            
    def printBestWeights(self):
        print("Best dif: %.3f with weights:" % self.VeryBestValueDifAvg)
        for colNum in range(self.data.getColumns() - 1):
            print("%.2f" % self.VeryBestWeights[colNum]) 
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data


def main():

    ai = AI()
    info = [
        [1, 0, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0]
    ]
    data = Data(info)
    ai.setData(data)
    ai.learn(999999)
    ai.printBestWeights()

    # row = [1, 0, 1, 0, 0]
    # print("")
    # ai.predictRow(row)

main()