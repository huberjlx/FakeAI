import random
import math

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
    # def getValueAt(self, rowNum, colNum):
    #     return self.sigmoid(self.info[rowNum][colNum])
    # def getResultForRow(self, rowNum):
    #     return self.sigmoid(self.info[rowNum][len(self.info[rowNum]) - 1])
    
    # def sigmoid(self, x):
    #     # print(1 / (1 + math.exp(-x)))
    #     return 1 / (1 + math.exp(-x))
    def getValueAt(self, rowNum, colNum):
        return self.info[rowNum][colNum]
    def getResultForRow(self, rowNum):
        return self.info[rowNum][len(self.info[rowNum]) - 1]

def sigmoid(x):
        # print(1 / (1 + math.exp(-x)))
        return 1 / (1 + math.exp(-x))


class AI():

    def __init__(self):
        self.learningRate = 0.05
        self.data = []
        self.weights = []

    def learn(self, numberOfTests):

        weights = self.weights
        print("")

        for cycle in range(numberOfTests):
            print("\n\nCycle: %i" % cycle)
            for colNum in range(self.data.getColumns() - 1):
                print(" %f" % weights[colNum])
            for rowNum in range(self.data.getRows()):
                # print("")
                sum = 0.0
                for colNum in range(self.data.getColumns() - 1):
                    sum = sum + weights[colNum] * self.data.getValueAt(rowNum, colNum)
                try:
                    sum = math.sqrt(sum)
                except:
                    sum = -(math.sqrt(-sum))

                sum = sigmoid(sum)
                dif = sum - self.data.getResultForRow(rowNum)
                # error = (1/2) * (dif **2)

                for colNum in range(self.data.getColumns() - 1):
                    weights[colNum] = weights[colNum] - self.learningRate * (dif * self.data.getValueAt(rowNum, colNum))

        self.weights = weights
        print("\n\n\nLearning Finished!")


    def predictRow(self, row):
        sum = 0
        for colNum in range(self.data.getColumns() - 1):
            sum = sum + self.weights[colNum] * row[colNum]
        sum = sigmoid(sum)
        value = round(sum)
        print("Sum: %f" % sum)
        print("Value: %i" % value)
        return value
            
    def printWeights(self):
        print("Weights:")
        for colNum in range(self.data.getColumns() - 1):
            print("%f" % self.weights[colNum]) 
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
    ai.learn(9999)
    ai.printWeights()

    row = [1, 0, 1, 0]
    print("\n\nTrying to predict the result if this was the data: ")
    print(row)
    print("\nPrediction: ")
    ai.predictRow(row)

main()