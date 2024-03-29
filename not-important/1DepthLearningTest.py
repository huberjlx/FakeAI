import random
import math
# import numpy as np

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

    def __init__(self):
        self.learningRate = 0.05
        self.data = []
        self.weights = []
        self.error = -1.0

    def learn(self, numberOfTests):

        weights = self.weights
        dif = 1000
        print("")

        for cycle in range(numberOfTests):
            print("\n\nCycle: %i" % cycle)
            totalError = 0.0
            for colNum in range(self.data.getColumns() - 1):
                print(" %.2f" % weights[colNum])
            for rowNum in range(self.data.getRows()):
                # print("")
                sum = 0.0
                for colNum in range(self.data.getColumns() - 1):
                    sum = sum + weights[colNum] * self.data.getValueAt(rowNum, colNum)
                try:
                    sum = math.sqrt(sum)
                except:
                    sum = -(math.sqrt(-sum))

                dif = sum - self.data.getResultForRow(rowNum)
                error = (1/2) * (dif **2)
                totalError = totalError + error

                for colNum in range(self.data.getColumns() - 1):
                    weights[colNum] = weights[colNum] - self.learningRate * (dif * self.data.getValueAt(rowNum, colNum))

                # print("Sum: %.3f" % sum)
                # print("Target: %i" % self.data.getResultForRow(rowNum))
                # print("Dif: %.3f" % dif)

            avgError = totalError / (self.data.getColumns() - 1)
            print("\nAverage Error: %.3f" % avgError)

        self.weights = weights
        self.error = avgError

        print("\n\n\nLearning Finished!")

    def sigmoid(self, x):
        # print(1 / (1 + math.exp(-x)))
        return 1 / (1 + math.exp(-x))

    def updateWeights(self, weights, derivative):
        sum = 0.0
        for colNum in range(self.data.getColumns() - 1):
            sum = sum + weights[colNum]
        for colNum in range(self.data.getColumns() - 1):
            weights[colNum] = weights[colNum] - (derivative * (weights[colNum]/sum))
        return weights

        # npWeights = np.array(weights)
        # npWeights = npWeights - derivative
        # weights = npWeights.tolist()
        # return weights


    def predictRow(self, row):
        sum = 0
        for colNum in range(self.data.getColumns() - 1):
            sum = sum + self.weights[colNum] * row[colNum]
        value = round(sum)
        print("Sum: %f" % sum)
        print("Value: %i" % value)
        return value
            
    def printWeights(self):
        print("error: %.3f with weights:" % self.error)
        for colNum in range(self.data.getColumns() - 1):
            print("%.2f" % self.weights[colNum]) 
    def setData(self, data):
        self.data = data
        for colNum in range(self.data.getColumns() - 1):
            weight = random.random()
            self.weights.append(weight)
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
    ai.printWeights()
    temp = input("Press [enter] to start learning: ")
    ai.learn(999)
    ai.printWeights()

    row = [1, 0, 1, 0]
    print("\n\nTrying to predict the result if this was the data: ")
    print(row)
    print("\nPrediction: ")
    ai.predictRow(row)

main()







# mse = (1/2) * ((target - output) ** 2)