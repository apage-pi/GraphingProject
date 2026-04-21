import matplotlib.pyplot as plt
from mathInterpereter import evaluateFunction, getXValues, getYValuesFromRange, evaluateRelation

def graphFunction(function: str, startingXValue: int, endingXValue: int) -> None:
    XValues = getXValues(startingXValue, endingXValue)
    YValues = evaluateFunction(function, XValues)
    plt.plot(XValues, YValues)
    plt.title(f"Graph of {function}")
    plt.ylabel('Y-Axis')
    plt.xlabel('X-Axis')
    plt.show()

def graphRelation(relationSideLeft:str, relationSideRight: str, startingXValue: int, endingXValue:int, startingYValue: int, endingYValue:int):
    initialXValues = getXValues(startingXValue, endingXValue)
    initialYValues = getYValuesFromRange(startingYValue, endingYValue)
    XValues, YValues = evaluateRelation(relationSideLeft, relationSideRight, initialXValues, initialYValues)
    plt.plot(XValues, YValues)
    plt.title(f"Graph of {relationSideLeft} = {relationSideRight}")
    plt.ylabel("Y-Axis")
    plt.xlabel("x-Axis")
    plt.show()

def functionToTextFile(fileName: str, function: str, startingXValue: int, endingXValue: int, interval: int=1) -> None:
    XValues = getXValues(startingXValue, endingXValue, interval)
    YValues = evaluateFunction(function, XValues)
    with open(fileName, "w") as out:
        out.write("X        Y\n")
        for i in range(len(XValues)):
            out.write(f"{XValues[i]}   {YValues[i]}\n")
        out.close()

def relationToTextFile(fileName: str, relationSideLeft: str, relationSideRight, startingXValue: int, endingXValue: int, startingYValue: int, endingYValue: int, interval: int=1) -> None:
    initialXValues = getXValues(startingXValue, endingXValue)
    initialYValues = getYValuesFromRange(startingYValue, endingYValue)
    XValues, YValues = evaluateRelation(relationSideLeft, relationSideRight, initialXValues, initialYValues)
    with open(fileName, "w") as out:
        out.write("X        Y\n")
        for i in range(len(XValues)):
            out.write(f"{XValues[i]}   {YValues[i]}\n")
        out.close()
            