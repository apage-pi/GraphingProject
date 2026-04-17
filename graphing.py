import matplotlib.pyplot as plt
from mathInterpereter import evaluateFunction, getXValues

def graphFunction(function: str, startingXValue: int, endingXValue: int) -> None:
    XValues = getXValues(startingXValue, endingXValue)
    YValues = evaluateFunction(function, startingXValue, endingXValue)
    plt.plot(XValues, YValues)
    plt.title(f"Graph of {function}")
    plt.ylabel('Y-Axis')
    plt.xlabel('X-Axis')
    plt.show()

def functionToTextFile(fileName: str, function: str, startingXValue: int, endingXValue: int, interval: int=1) -> None:
    XValues = getXValues(startingXValue, endingXValue, interval)
    YValues = evaluateFunction(function, startingXValue, endingXValue, XValues)
    counter = 0
    with open(fileName, "w") as out:
        out.write("X        Y\n")
        for XValue in XValues:
            
            



graphFunction("x^2", -1, 1)