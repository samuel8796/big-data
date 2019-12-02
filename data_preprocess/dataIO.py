import pandas as pd
import numpy as np
from pathlib import Path
from config import config
[2,3,26,33,34,36,39,40,49,50,51,52,53,54,60,61,65]

def load_row_dataset(path):
    list_of_column = config
    p = Path(path)
    row_data = pd.read_excel(p)
    row_data = row_data.iloc[:,list_of_column]
    return row_data


