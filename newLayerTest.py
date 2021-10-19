import random
import math


class Data():

    def __init__(self, info):
        self.info = info # Info inital data

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
    def __init__(self, layers):
        self.layers = layers # Layers is a list of list of layer classes
        self.learningRate = 0.05
        self.weights = self.layers[0]

    def learn(self, numOfTests, data):
        info = data.getInfo()
        for testNum in range(numOfTests):
            print("Test Num: %i" % testNum)
            for row in range(len(info)):
                # for layer in self.layers:
                    # weights = layer.getWeights()
                    # expectedVals = layer.getExpectedVals()
                    # predictedVals = layer.getPredictedVals()
                    # biasVals = layer.getBiasVals()
                for layer in self.layers:
                    predictedVals = layer.calcLayer(row)
                    weights = layer.getWeights()
                    for i in range(len(weights)):
                        # print("Weight:", weights[i])
                        # print("row:", row)
                        # print("Predicted Vals:", predictedVals)
                        weights[i] = weights[i] + self.learningRate * (data.getResultForRow(row) - layer.predictedVals[row])
                    layer.setWeights(weights)
                    self.weights = weights
                print("Expected Val: %f" % data.getResultForRow(row))
                print("predictedVals: %f" % predictedVals[row])
            print()


    def displayFinalValue(self, expectedValue, prediction):
        print("Prediction: %f" % prediction)
        print("Expected Value: %f" % expectedValue)

    def predictRow(self, data, rowNum):
        layer = self.layers[len(self.layers) - 1]
        print("Data:", data.info[rowNum])
        print("Weights:", layer.getWeights())
        print("Expected:", data.getResultForRow(rowNum))
        print("Prediction:", layer.predictedVals[rowNum])


class Layer():
    def __init__(self, inPoints, outPoints, biasVal, layerNum):
        "outPoints is num of points the layer spits out, inPoints is the num of data points going into the layer"
        self.inPoints = inPoints
        self.outPoints = outPoints
        self.weights = []
        self.data = [] # List of lists
        self.predictedVals = [0, 0, 0, 0, 0, 0] # Lists of lists
        # self.biasVals = biasVals
        for i in range(inPoints):
            randVal = random.random()
            self.weights.append(randVal)

    def setData(self, data):
        self.data = data

    def getWeights(self):
        return self.weights

    def setWeights(self, weights):
        self.weights = weights

    def getExpectedVals(self):
        expectedVals = []
        for row in range(len(self.data.getInfo())):
            expectedVals.append(self.data.getResultForRow(row))

        return expectedVals

    def getPredictedVals(self):
        return self.predictedVals

    # def getBiasVal(self):
        # return self.biasVals

    def calcLayer(self, rowNum): # Predicts the outcome of the data
        data = self.data.getInfo()
        sum = 0
        for i in range(len(data[rowNum]) - 1): # i is a data point
            sum = sum + data[rowNum][i] * self.weights[i]
        try:
            sum = math.sqrt(sum)
        except:
            sum = -(math.sqrt(-sum))

        # sum = sum - self.data.getResultForRow(rowNum)
        self.predictedVals[rowNum] = sum
        return self.predictedVals

def main():
    info = [
        [1, 0, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0]
    ]
    data = Data(info)
    layer1 = Layer(4, 1, 1, 0)
    layer2 = Layer(4, 1, 1, 0)
    layers = [layer1, layer2]
    # tempData = info[0]
    tempData = info[2]
    layer1.setData(data)
    layer2.setData(data)
    ai = AI(layers)
    print("Initial Weights: \n %f \n %f \n %f \n %f \n" % (layer1.weights[0], layer1.weights[1], layer1.weights[2], layer1.weights[3]))
    print("\n", data.getInfo())
    tempInput = input("Press 'ENTER' to start: ")
    ai.learn(99, data)
    ai.predictRow(data, 2)
    # ai.displayFinalValue(data.getValueAt(), layer1.predictedVals[0])


main()
