import pandas as pd
import numpy as np
emp=[101,102,103,104,105,106,107,108,109,110]
age=[28,32,29,35,41,26,38,30,45,27]
print("mean:",np.mean(age))
print("median:",np.median(age))
print("variance:",np.var(age))
print("std:",np.std(age))
print("correlation:",np.corrcoef(age,emp))
