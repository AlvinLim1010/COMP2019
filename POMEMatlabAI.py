import POME_ANN as MatlabANN


class excelNeuralNetworkPOME:

    def __init__(self, matpath):
        self.matPath = matpath
        self.algo = MatlabANN.initialize()

    def predict(self, excelpath, rows):
        out = self.algo.PredictPOME(excelpath, self.matPath, rows)
        out = self._mlarray2PyArray(out)
        return out

    def train(self, excelpath, rows):
        self.algo.TrainPOME(excelpath, self.matPath, rows)

    # Converts matlab arrays to python arrays
    def _mlarray2PyArray(self, mldoublearray):
        x = mldoublearray[0]
        pyArrayOfArrays = []
        for row in mldoublearray:
            pyArray = []
            for element in row:
                pyArray.append(element)
            pyArrayOfArrays.append(pyArray)

        return pyArrayOfArrays



'''NN = excelNeuralNetworkPOME("C:\\Users\\User\\Desktop\\Year 2 Stuff (2nd Semester)\\pre_trained_net.mat")
output = NN.predict("C:\\Users\\User\\Desktop\\Year 2\\SE Group Project\\POME Data\\40S Thermal Pretreated.xlsx",30)
print(output)
print(type(output))
alg = MatlabANN.initialize()
out=alg.TrainPOME("C:\\Users\\User\\Desktop\\Year 2\\SE Group Project\\POME Data\\40S Thermal Pretreated.xlsx","C:\\Users\\User\\Desktop\\Year 2 Stuff (2nd Semester)\\pre_trained_net.mat",30)
print(out)'''