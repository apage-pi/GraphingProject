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

def getYValuesFromRange(startingYValue: int, endingYValue: int, interval:int=1000) -> list[int]:
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
            for xValue in XValues:
                for yValue in YValues:
                    variables = {"x":xValue, "y":yValue}
                    leftSideResult = round(float(evaluate(functionLeftSide, variables)), 6)
                    rightSideResult = round(float(evaluateExpression(functionRightSide)), 6)
                    if leftSideResult >= rightSideResult - 0.0001 and leftSideResult <= rightSideResult + 0.0001:
                        correctXValues.append(xValue)
                        correctYValues.append(yValue)
        else:
            for xValue in XValues:
                for yValue in YValues:
                    leftSideResult = round(float(evaluate(functionLeftSide, xValue)), 6)
                    rightSideResult = round(float(evaluate(functionRightSide, yValue)), 6)
                    if leftSideResult >= rightSideResult - 0.0001 and leftSideResult <= rightSideResult + 0.0001:
                        correctXValues.append(xValue)
                        correctYValues.append(yValue)
    else:
        if "y" in functionLeftSide:
            for xValue in XValues:
                for yValue in YValues:
                    leftSideResult = round(float(evaluate(functionLeftSide, yValue)), 6)
                    rightSideResult = round(float(evaluate(functionRightSide, xValue)), 6)
                    if leftSideResult >= rightSideResult - 0.0001 and leftSideResult <= rightSideResult + 0.0001:
                        correctXValues.append(xValue)
                        correctYValues.append(yValue)
        else:
            for xValue in XValues:
                for yValue in YValues:
                    variables = {"x":xValue, "y":yValue}
                    leftSideResult = round(float(evaluateExpression(functionLeftSide)), 6)
                    rightSideResult = round(float(evaluate(functionRightSide, variables)), 6)
                    if leftSideResult >= rightSideResult - 0.0001 and leftSideResult <= rightSideResult + 0.0001:
                        correctXValues.append(xValue)
                        correctYValues.append(yValue)
    return correctXValues, correctYValues


