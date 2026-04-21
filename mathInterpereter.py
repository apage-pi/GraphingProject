from pymep.realParser import eval, parse

def evaluate(evaluation: str, variable) -> float:
    result = round(float(eval(evaluation, variable)), 6)
    return result

def evaluateExpression(evaluation: str) -> float:
    result = round(float(parse(evaluation)))
    return result

def getYValuesFromFunction(function: str, xValues: list[float]) -> list[float]:
    yValues = []
    for xValue in xValues:
        yValues.append(evaluate(function, xValue))
    return yValues

def evaluateFunction(function: str, XValues: list=[]) -> list[float]:
    YValues = getYValuesFromFunction(function, XValues)
    return YValues

def getXValues(startingXValue: int, endingXValue: int, interval:int=1000) -> list[int]:
    XValues = []
    for i in range(startingXValue*interval, endingXValue*interval + 1):
        XValues.append(float(i)/float(interval))
    return XValues

def GetYValuesFromRange(startingYValue: int, endingYValue: int, interval:int=1000) -> list[int]:
    YValues = []
    for i in range(startingYValue*interval, endingYValue*interval + 1):
        YValues.append(float(i)/float(interval))
    return YValues

def evaluateRelation(functionLeftSide: str, functionRightSide: str, XValues: list[int], YValues:list[int]) -> tuple[list[float], list[float]]:
    rightSideResult: float = 0
    leftSideResult: float = 0
    correctXValues: list[float] = []
    correctYValues: list[float] = []
    variables = {}
    if "x" in functionLeftSide:
        if "y" in functionLeftSide:
            for i in range(len(XValues)):
                for j in range(len(YValues)):
                    variables = {"x":str(XValues[i]), "y":str(YValues[j])}
                    leftSideResult = float(evaluate(functionLeftSide, variables))
                    rightSideResult = float(evaluateExpression(functionRightSide))
                    if leftSideResult == rightSideResult:
                        correctXValues.append(leftSideResult)
                        correctYValues.append(rightSideResult)
                    else:
                        pass
        else:
            for i in range(len(XValues)):
                for j in range(len(YValues)):
                    leftSideResult = float(evaluate(functionLeftSide, XValues[i]))
                    rightSideResult = float(evaluate(functionRightSide, YValues[j]))
                    if leftSideResult == rightSideResult:
                        correctXValues.append(leftSideResult)
                        correctYValues.append(rightSideResult)
                    else:
                        pass
    return correctXValues, correctYValues


