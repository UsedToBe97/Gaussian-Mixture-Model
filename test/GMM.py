from numpy import *

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(' ')
        fltLine = map(float, curLine)
        for item in fltLine:
            print(item)
        dataMat.append(fltLine)
        #print(len(curLine))
    return dataMat

def gmm(file, K):
    loadDataSet(file)