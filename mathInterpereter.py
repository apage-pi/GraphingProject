from pymep.realParser import eval

def evaluate(evaluation: str, xValue: float) -> float:
    result = round(float(eval(evaluation, xValue)), 6)
    return result

def getYValues(function: str, xValues: list[float]) -> list[float]:
    yValues = []
    for xValue in xValues:
        yValues.append(evaluate(function, xValue))
    return yValues

def evaluateFunction(function: str, XValues: list=[]) -> list[float]:
    YValues = getYValues(function, XValues)
    return YValues

def getXValues(startingXValue: int, endingXValue: int, interval:int=1000) -> list[int]:
    XValues = []
    for i in range(startingXValue*interval, endingXValue*interval + 1):
        XValues.append(float(i)/float(interval))
    return XValues

def checkXAndYValues(functionSide1: str, functionSide2: int, XValues: list[int], YValues:list[int]) -> list[int], list[int]:
    if "x" in functionSide1:
        if "y" in functionSide1:
            for i in range(len(XValues))
