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
    # return x  * ((1 + math.exp(-1)) ** -1)
    return 1 / (1 + math.exp(-x))

class Layer():

    def __init__(self, inPoints, outPoints, layerNum):
        self.outPoints = outPoints
        self.inPoints = inPoints
        self.layerNum = layerNum
        self.weights = []
        for points in range(self.outPoints):
            temp = []
            for weight in range(self.inPoints):
                w = random.random()
                temp.append(w)
            self.weights.append(temp)

    def calcLayer(self, inputs):
        sums = []
        for outPoint in range(self.outPoints):
            sum = 0
            for point in range(len(inputs)):
                sum = sum + self.weights[outPoint][point] * inputs[point]
            # sum = swish(sum) # ACTIVATE
            sums.append(sum)
        return sums

    def updateWeights(self, learningRate, dif, target):
        for points in range(self.outPoints):
            for weight in range(self.inPoints):
                updateVal = learningRate * (dif * target)
                self.weights[points][weight] = self.weights[points][weight] - updateVal
            print("Update by: %.5f" % (-updateVal))

    def printWeights(self):
        title = "layer%i  :  (%i in, %i out)\n" % (self.layerNum, self.inPoints, self.outPoints)
        weightsString = ""
        for point in range(self.outPoints):
            for weight in range(self.inPoints):
                weightsString  = "%s%.3f " % (weightsString, self.weights[point][weight])
            weightsString = weightsString + "\n"
        finalString = title + weightsString
        print(finalString)
        return finalString
            


class AI():

    def __init__(self, layers):
        self.learningRate = 0.05
        self.data = []
        self.layers = layers

    def learn(self, numberOfTests):

        for cycle in range(numberOfTests):
            print("\nCycle: %i" % cycle)

            for rowNum in range(self.data.getRows()):
                inputs = []
                for colNum in range(self.data.getColumns() - 1):
                    inputs.append(self.data.getValueAt(rowNum, colNum))
                for layer in self.layers:
                    inputs = layer.calcLayer(inputs)
                sum = inputs[0]

                # WHY IS THIS NEEDED???
                try:
                    sum = math.sqrt(sum)
                except:
                    sum = -(math.sqrt(-sum))

                dif = sum - self.data.getResultForRow(rowNum)
                print("DIF: %f" % dif)
                if dif > 0.5:
                    print("LARGE ISSUE !!!!!!!!!!!!!")
                for layer in self.layers:
                    layer.updateWeights(self.learningRate, dif, self.data.getResultForRow(rowNum))

            self.printWeights()
                

    def predictRow(self, row):
        inputs = []
        for colNum in range(self.data.getColumns() - 1):
            inputs.append(row[colNum])
        for layer in self.layers:
            inputs = layer.calcLayer(inputs)
        sum = inputs[0]
        
        value = round(sum)
        print("Sum: %f" % sum)
        print("Value: %i" % value)
        return value
            
    def printWeights(self):
        for layer in self.layers:
            layer.printWeights()
        print("\n")

    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data


def main():

    # l0 = Layer(4, 6, 0)
    # l1 = Layer(6, 7, 1)
    # l2 = Layer(7, 1, 2)
    # l3 = Layer(3, 1, 0)
    # layers = [l0, l1, l2]#, l3]
    layers = [Layer(4, 1, 0)]
    ai = AI(layers)
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
    ai.learn(9)
    print("\n\nFinal Weights")
    ai.printWeights()

    row = [1, 0, 1, 0] # should be 1
    row2 = [0, 0, 1, 1]
    print("\n\nTrying to predict the result if this was the data: ")
    print(row)
    print("\nPrediction: ")
    ai.predictRow(row)
    print("Should be 1")
    ai.predictRow(row2)
    print("Should be 0")

    
main()