import pymagicc
from pymagicc import MAGICC6
from pymagicc import rcp26, rcp45, rcp60, rcp85
import pandas as pd
from pymagicc.scenarios import rcps

'''
This function load four secinarios and collect them into  csv files entitled 
totalrcp_dataset and rawrcps_dataset
'''
with MAGICC6() as magicc:
    data = magicc.run(rcp26)
    for rcp in [rcp45, rcp60, rcp85]:
        data.append(magicc.run(rcp), inplace=True)

data.to_csv ('totalrcp_dataset.csv')
rcps.to_csv('rawrcps_dataset.csv')


