import matplotlib.pyplot as plt
from mathInterpereter import evaluateFunction, getXValues

XValues = getXValues(-1, 1)
YValues = evaluateFunction("x^2", -1, 1)
plt.plot(XValues, YValues)
