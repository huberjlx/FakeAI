import random
import math
# https://realpython.com/python-ai-neural-network/

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
        self.data = []
        self.weights = []
        self.mse = 0

    def learn(self, numberOfTests):

        weights = self.weights
        dif = 1000

        for colNum in range(self.data.getColumns() - 1):
            weight = random.random()
            weights.append(weight)
            # print(" %f" % weight, end="")
        print("")

        for cycle in range(numberOfTests):
            print("\n\nCycle: %i" % cycle)
            totalDerivative = 0
            for colNum in range(self.data.getColumns() - 1):
                print(" %.2f" % weights[colNum])
            for rowNum in range(self.data.getRows()):
                print("")
                sum = 0.0
                for colNum in range(self.data.getColumns() - 1):
                    sum = sum + weights[colNum] * self.data.getValueAt(rowNum, colNum)
                try:
                    sum = math.sqrt(sum)
                except:
                    sum = -(math.sqrt(-sum))
                sum = self.sigmoid(sum)
                dif = sum - self.data.getResultForRow(rowNum)
                mse = dif ** 2
                derivative = 2 * dif
                totalDerivative = totalDerivative + derivative

                print("Sum: %.3f" % sum)
                print("Target: %i" % self.data.getResultForRow(rowNum))
                print("mse: %.3f" % mse)
                print("Der: %.3f" % derivative)

            avgDerivative = totalDerivative / self.data.getRows()
            print("Avg Der: %.3f" % avgDerivative)
            weights = self.updateWeights(weights, avgDerivative)


        self.weights = weights
        self.mse = mse


        print("\n\n\nlearning finished!")

    def sigmoid(self, x):
        print(1 / (1 + math.exp(-x)))
        return 1 / (1 + math.exp(-x))

    def updateWeights(self, weights, derivative):
        sum = 0.0
        for colNum in range(self.data.getColumns() - 1):
            sum = sum + weights[colNum]
        for colNum in range(self.data.getColumns() - 1):
            weights[colNum] = weights[colNum] - (derivative * (weights[colNum]/sum))
        return weights
        # d_weights2 = weights, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        # d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))


    def predictRow(self, row):
        sum = 0
        for colNum in range(self.data.getColumns() - 1):
            sum = sum + self.VeryBestWeights[colNum] * row[colNum]
        value = round(sum)
        print("Sum: %f" % sum)
        print("Value: %i" % value)
        return value
            
    def printWeights(self):
        print("mse: %.3f with weights:" % self.mse)
        for colNum in range(self.data.getColumns() - 1):
            print("%.2f" % self.weights[colNum]) 
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
    ai.learn(99)
    ai.printWeights()

    # row = [1, 0, 1, 0, 0]
    # print("")
    # ai.predictRow(row)

main()