import random
import math
# NOTE: DEPTH IS NOT ACTUALLY DEPTH, ITS SECTIONS!!! This whole thing is 2 linear depth

class Data():

    def __init__(self, info):
        self.info = info

    def readInInfo(self, fname):
        print("not done yet")
    def getInfo(self):
        return self.info
    def getRows(self): # total # how many tall
        return len(self.info)
    def getColumns(self): # rows # how many on wide
        return len(self.info[0])
    def getValueAt(self, rowNum, colNum):
        return self.info[rowNum][colNum]
    def getResultForRow(self, rowNum):
        return self.info[rowNum][len(self.info[rowNum]) - 1]


class AI():

    def __init__(self, weightDepth):
        self.learningRate = 0.05
        self.data = []
        self.listOfweights = [[], []]
        for depth in range(weightDepth):
            weight = random.random()
            self.listOfweights[1].append(weight)


    def learn(self, numberOfTests):
        totalDepth = len(self.listOfweights[1])

        for cycle in range(numberOfTests):
            print("\nCycle: %i" % cycle)
            
            for rowNum in range(self.data.getRows()):
                grandSum = 0.0
                for depth in range(totalDepth):
                    sum = 0.0
                    for colNum in range( int(((self.data.getColumns() - 1)/totalDepth) * depth), int(((self.data.getColumns() - 1)/totalDepth) * (depth + 1)) ):
                        sum = sum + self.listOfweights[0][colNum] * self.data.getValueAt(rowNum, colNum)
                    sum = sum * self.listOfweights[1][depth]
                    grandSum = grandSum + sum

                try:
                    grandSum = math.sqrt(grandSum)
                except:
                    grandSum = -(math.sqrt(-grandSum))

                dif = grandSum - self.data.getResultForRow(rowNum)
                error = (1/2) * (dif **2)

                for colNum in range(self.data.getColumns() - 1):
                    self.listOfweights[0][colNum] = self.listOfweights[0][colNum] - self.learningRate * (dif * self.data.getValueAt(rowNum, colNum))
                for depth in range(totalDepth):
                    self.listOfweights[1][depth] = self.listOfweights[1][depth] - self.learningRate * (dif * self.data.getValueAt(rowNum, colNum))

            self.printWeights()
                


    def predictRow(self, row):
        totalDepth = len(self.listOfweights[1])
        grandSum = 0.0
        for depth in range(totalDepth):
            sum = 0.0
            for colNum in range( int(((self.data.getColumns() - 1)/totalDepth) * depth), int(((self.data.getColumns() - 1)/totalDepth) * (depth + 1)) ):
                sum = sum + self.listOfweights[0][colNum] * row[colNum]
            sum = sum * self.listOfweights[1][depth]
            grandSum = grandSum + sum
        value = round(grandSum)
        print("Sum: %f" % grandSum)
        print("Value: %i" % value)
        return value
            
    def printWeights(self):
        print("layer1: ", end="")
        for colNum in range(self.data.getColumns() - 1):
            print("%.3f " % self.listOfweights[0][colNum], end="")
        print("\nlayer2: ", end="")
        for depth in range(len(self.listOfweights[1])):
            print("%.3f " % self.listOfweights[1][depth], end="")
        print("")

    def setData(self, data):
        self.data = data
        self.listOfweights[0] = []
        for colNum in range(self.data.getColumns() - 1):
            weight = random.random()
            self.listOfweights[0].append(weight)
    def getData(self):
        return self.data


def main():

    ai = AI(2)
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
    ai.printWeights()
    temp = input("Press [enter] to start learning: ")
    ai.learn(999)
    print("\n\nFinal Weights")
    ai.printWeights()

    row = [1, 0, 1, 0]
    print("\n\nTrying to predict the result if this was the data: ")
    print(row)
    print("\nPrediction: ")
    ai.predictRow(row)

main()