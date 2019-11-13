import numpy as np
from config import config

def deal_missing_value(row_data):
  for i in range(0,len(row_data[' - PRICE HIGH'])):
    if(np.isnan(row_data[' - PRICE HIGH'][i])):
        row_data[' - PRICE HIGH'][i]=row_data[' - PRICE HIGH'][i-1]
    if(np.isnan(row_data[' - MARKET VALUE'][i])):
        row_data[' - MARKET VALUE'][i]=row_data[' - MARKET VALUE'][i-1]
    if(np.isnan(row_data[' - PRICE LOW'][i])):
        row_data[' - PRICE LOW'][i]=row_data[' - PRICE LOW'][i-1]
    if(np.isnan(row_data[' - DIVIDEND YIELD'][i])):
        row_data[' - DIVIDEND YIELD'][i]=row_data[' - DIVIDEND YIELD'][i-1]
    if(np.isnan(row_data[' - EARNINGS PER SHR'][i])):
        row_data[' - EARNINGS PER SHR'][i]=row_data[' - EARNINGS PER SHR'][i-1]
    if(np.isnan(row_data[' - OPENING PRICE'][i])):
        row_data[' - OPENING PRICE'][i]=row_data[' - OPENING PRICE'][i-1]
    if(np.isnan(row_data[' - TURNOVER BY VALUE'][i])):
        row_data[' - TURNOVER BY VALUE'][i]=row_data[' - TURNOVER BY VALUE'][i-1]
    if(np.isnan(row_data[' - TURNOVER BY VOLUME'][i])):
        row_data[' - TURNOVER BY VOLUME'][i]=row_data[' - TURNOVER BY VOLUME'][i-1]
    if(np.isnan(row_data[' - BK VAL PS 12M FWD'][i])):
        row_data[' - BK VAL PS 12M FWD'][i]=row_data[' - BK VAL PS 12M FWD'][i-1]
    if(np.isnan(row_data[' - EV 12M FWD'][i])):
        row_data[' - EV 12M FWD'][i]=row_data[' - EV 12M FWD'][i-1]
    if(np.isnan(row_data[' - NET INCOME 12M FWD'][i])):
        row_data[' - NET INCOME 12M FWD'][i]=row_data[' - NET INCOME 12M FWD'][i-1]
    if(np.isnan(row_data[' - PRETAX PRF 12M FWD'][i])):
        row_data[' - PRETAX PRF 12M FWD'][i]=row_data[' - PRETAX PRF 12M FWD'][i-1]
    if(np.isnan(row_data[' - ROE 12M FWD'][i])):
        row_data[' - ROE 12M FWD'][i]=row_data[' - ROE 12M FWD'][i-1]
    if(np.isnan(row_data[' - SALES 12M FWD'][i])):
        row_data[' - SALES 12M FWD'][i]=row_data[' - SALES 12M FWD'][i-1]
    if(np.isnan(row_data[' - P/CSH FLOW RATIO'][i])):
        row_data[' - P/CSH FLOW RATIO'][i]=row_data[' - P/CSH FLOW RATIO'][i-1]
    if(np.isnan(row_data[' - PRICE TO BOOK VAL'][i])):
        row_data[' - PRICE TO BOOK VAL'][i]=row_data[' - PRICE TO BOOK VAL'][i-1]
    if(np.isnan(row_data[' - NUMBER OF SHARES'][i])):
        row_data[' - NUMBER OF SHARES'][i]=row_data[' - NUMBER OF SHARES'][i-1]
        
    return row_data
