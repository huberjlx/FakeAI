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


def swish(x):
    return x  * ((1 + math.exp(-1)) ** -1)

class AI():

    def __init__(self):
        self.learningRate = 0.05
        self.data = []
        self.listOfWeights = []


    def learn(self, numberOfTests):

        for cycle in range(numberOfTests):
            print("\nCycle: %i" % cycle)

            for rowNum in range(self.data.getRows()):
                sum = 0.0
                inputs = []
                for colNum in range(self.data.getColumns() - 1):
                    inputs.append(self.data.getValueAt(rowNum, colNum))

                for layer in range(len(self.listOfWeights)): # 3
                    sums = [0] * len(self.listOfWeights[layer]) # 3
                    for point in range(len(self.listOfWeights[layer])):
                        for weight in range(len(self.listOfWeights[layer][point])):
                            sums[point] = sums[point] + self.listOfWeights[layer][point][weight] * inputs[weight]
                            # print(sums)
                    inputs = sums
                    for idx in range(len(inputs)):
                        inputs[idx] = swish(inputs[idx])

                sum = sums[0]
                # this doesnt work (rest of function from here down)
                # sum = swish(sum)
                dif = sum - self.data.getResultForRow(rowNum)
                print("Dif: %4f  :  %4f" % (dif, dif * self.learningRate))
                for layer in range(len(self.listOfWeights)):
                    for point in range(len(self.listOfWeights[layer])):
                        for weight in range(len(self.listOfWeights[layer][point])):
                            self.listOfWeights[layer][point][weight] = self.listOfWeights[layer][point][weight] - self.learningRate * dif
                            


            self.printWeights()
                

    def predictRow(self, row):
        sum = 0.0
        inputs = []
        for colNum in range(self.data.getColumns() - 1):
            inputs.append(row[colNum])

        for layer in range(len(self.listOfWeights)): # 3
            sums = [0] * len(self.listOfWeights[layer]) # 3
            for point in range(len(self.listOfWeights[layer])):
                for weight in range(len(self.listOfWeights[layer][point])):
                    sums[point] = sums[point] + self.listOfWeights[layer][point][weight] * inputs[weight]
                    # print(sums)
            inputs = sums


        sum = sums[0]
        
        value = round(sum)
        print("Sum: %f" % sum)
        print("Value: %i" % value)
        return value
            
    def printWeights(self):
        for layer in range(len(self.listOfWeights)):
            print("layer%i:" % layer)
            for point in range(len(self.listOfWeights[layer])):
                for weight in range(len(self.listOfWeights[layer][point])):
                    print("%.3f " % self.listOfWeights[layer][point][weight], end="")
                print("")
        print("\n")

    def setData(self, data):
        self.data = data
        self.listOfWeights = []

        count = self.data.getColumns() - 1
        while count > 1:
            layer = []
            for i in range(count - 1):
                temp = []
                for j in range(count):
                    temp.append(random.random())
                layer.append(temp)
            self.listOfWeights.append(layer)
            count = count - 1

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
        # [1, 0, 1, 0, 0]
    ]
    data = Data(info)
    ai.setData(data)
    ai.printWeights()
    temp = input("Press [enter] to start learning: ")
    ai.learn(999)
    print("\n\nFinal Weights")
    ai.printWeights()

    row = [1, 0, 1, 0] # should be 1
    print("\n\nTrying to predict the result if this was the data: ")
    print(row)
    print("\nPrediction: ")
    ai.predictRow(row)

main()