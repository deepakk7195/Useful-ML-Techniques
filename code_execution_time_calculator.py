import numpy as np
from datetime import datetime
import time

v = np.arange(1000)

import time
start = time.time()
print(start)
v1 = v
print('It took', time.time()-start, 'seconds for BFL.')

startw = time.time()
print(startw)
v2 = v.copy() # Takes longer
print('It took', time.time()-startw, 'seconds for BFL.')

# Thus directly passing by reference is faster than using copy function.