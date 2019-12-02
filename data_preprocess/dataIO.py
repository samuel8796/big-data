import pandas as pd
import numpy as np
from pathlib import Path
from config import listofcolumn


def load_row_dataset(path):
    list_of_column = listofcolumn()
    p = Path(path)
    row_data = pd.read_excel(p)
    row_data = row_data.iloc[:,list_of_column]
    return row_data


