import numpy as np
a1 = np.zeros((2, 3))
a2 = np.arange(10)
print(a1); print(a2)
a3= np.arange(2, 10, dtype=np.float)
a4 = np.arange(2, 3, 0.1)
print(a3); print(a4)
a5 = np.linspace(1., 4., 6)
a6 = np.indices((3,3))
print(a5); print(a6)
print('#',50*"-")