import matplotlib.pyplot as plt
from mathInterpereter import evaluateFunction, getXValues

XValues = getXValues(-1, 1)
YValues = evaluateFunction("x^2", -1, 1)
equation = "x^2"
plt.plot(XValues, YValues)
plt.title(f"Graph of {equation}")
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.show()