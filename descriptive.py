import pandas as pd
import numpy as np
marks=[30,55,80,85,87,90,95,100]
hours=[2,5,7,7,8,9,10,11]
print("mean:",np.mean(marks))
print("median:",np.median(marks))
print("variance:",np.var(marks))
print("std:",np.std(marks))
print("correlation:",np.corrcoef(marks,hours))
