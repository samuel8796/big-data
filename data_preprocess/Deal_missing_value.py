import numpy as np

def missing_value(row_data):
    count = 0
    for j in range(0,15):
        for i in range(0,len(row_data)-1):
            if(np.isnan(np.array(row_data.iloc[[i],[j]]))):
                count+=1
                row_data.iloc[[i],[j]] = float(np.array(row_data.iloc[[i-1],[j]]))
    return row_data
