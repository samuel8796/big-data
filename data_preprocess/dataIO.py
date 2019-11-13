import pandas as pd
import numpy as np
from pathlib import Path

def load_row_dataset(path):
    p = Path(path)
    csv_list = list(p.glob('**/*.xlsx'))
    row_data_list = []
    
    for i in csv_list:
        row_data = pd.read_excel(i)
        #row_data = row_data[[' - MARKET VALUE',' - DIVIDEND YIELD',' - EARNINGS PER SHR',' - PRICE HIGH',' - PRICE LOW',' - OPENING PRICE',' - TURNOVER BY VALUE',' - TURNOVER BY VOLUME',' - BK VAL PS 12M FWD',' - EV 12M FWD',' - NET INCOME 12M FWD',' - PRETAX PRF 12M FWD',' - ROE 12M FWD',' - SALES 12M FWD',' - P/CSH FLOW RATIO',' - PRICE TO BOOK VAL',' - NUMBER OF SHARES']]
        row_data_list.append(row_data)
        
    return row_data_list
