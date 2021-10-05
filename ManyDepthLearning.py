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
    def getValueAt(self, rowNum, colNum):
        return self.info[rowNum][colNum]
    def getResultForRow(self, rowNum):
        return self.info[rowNum][len(self.info[rowNum]) - 1]


class AI():

    def __init__(self, weightDepth, middleLayerSize):
        self.learningRate = 0.05
        self.data = []
        self.listOfWeights = [[]]

        for depth in range(weightDepth):
            self.listOfWeights.append([])
            for place in range(middleLayerSize):
                weight = random.random()
                self.listOfWeights[depth+1].append(weight)

        print(self.listOfWeights)


    def learn(self, numberOfTests):

        for cycle in range(numberOfTests):
            print("\nCycle: %i" % cycle)

            for rowNum in range(self.data.getRows()):
                print("\nCycle: %i" % cycle)

                for rowNum in range(self.data.getRows()):
                    sum = 0.0

                    for colNum in range(self.data.getColumns() - 1): # layer0 always have this many
                        sum = sum + self.listOfWeights[0][colNum] * self.data.getValueAt(rowNum, colNum)

                    for layer in range(len(self.listOfWeights) - 1): # 3 
                        layerSize = len(self.listOfWeights[layer]) # 2
                        sums = [sum] * layerSize
                        for layerWidthCount in range(layerSize):
                            sums[layerWidthCount] = sums[layerWidthCount] * self.listOfWeights[layer][layerWidthCount]
                        sum = sums[0] + sums[1]
                        
                    try:
                        sum = math.sqrt(sum)
                    except:
                        sum = -(math.sqrt(-sum))
                    target = self.data.getResultForRow(rowNum) #* len(self.listOfWeights)
                    dif = sum - target
                    # error = (1/2) * (dif **2)

                    for layer in range(len(self.listOfWeights)):
                        for weightIdx in range(len(self.listOfWeights[layer])):
                            self.listOfWeights[layer][weightIdx] = self.listOfWeights[layer][weightIdx] - self.learningRate * (dif * self.data.getValueAt(rowNum, colNum))



            self.printWeights()
                

    def predictRow(self, row):
        sum = 0.0

        for colNum in range(self.data.getColumns() - 1):
            sum = sum + self.listOfWeights[0][colNum]

        for layer in range(len(self.listOfWeights) - 1): # 3 
            layerSize = len(self.listOfWeights[layer]) # 2
            sums = [sum] * layerSize
            for layerWidthCount in range(layerSize):
                sums[layerWidthCount] = sums[layerWidthCount] * self.listOfWeights[layer][layerWidthCount]
            sum = sums[0] + sums[1]
        
        value = round(sum)
        print("Sum: %f" % sum)
        print("Value: %i" % value)
        return value
            
    def printWeights(self):
        for layer in range(len(self.listOfWeights)):
            print("\nlayer%i: " % layer, end="")
            for colNum in range(len(self.listOfWeights[layer])):
                print("%.3f " % self.listOfWeights[layer][colNum], end="")
        print("\n")

    def setData(self, data):
        self.data = data
        self.listOfWeights[0] = []
        for colNum in range(self.data.getColumns() - 1):
            weight = random.random()
            self.listOfWeights[0].append(weight)
        print(self.listOfWeights)
    def getData(self):
        return self.data


def main():

    ai = AI(3, 2)
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
    print("\n\nFinal Weights")
    ai.printWeights()

    row = [1, 0, 1, 0] # should be 1
    print("\n\nTrying to predict the result if this was the data: ")
    print(row)
    print("\nPrediction: ")
    ai.predictRow(row)

main()