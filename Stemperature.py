import pymagicc
from pymagicc import MAGICC6
import pandas as pd

from matplotlib import pyplot as plt


def main():

    data_dfrm=pd.read_csv('totalrcp_dataset.csv')

    datafrm_filtered = data_dfrm[(data_dfrm.region == 'World') & (data_dfrm.variable == 'Surface Temperature')]

    datafrm_filtered= datafrm_filtered.drop(['climate_model', 'model', 'region', 'todo', 'unit', 'variable'], axis=1)
    newdatafrm= datafrm_filtered.T.reset_index().drop(0)

    # newdatafrm.reindex()
    newdatafrm.columns = [ 'year','RCP26', 'RCP45', 'RCP60', 'RCP85']
    newdatafrm['year']=pd.to_datetime(newdatafrm['year'], errors = 'coerce')
    df=newdatafrm

    plt.figure(figsize=(12, 8))
    plt.plot(df['year'], df['RCP26'], label='RCP26')
    plt.plot(df['year'], df['RCP45'], label='RCP45')
    plt.plot(df['year'], df['RCP60'], label='RCP60')
    plt.plot(df['year'], df['RCP85'], label='RCP85')
    plt.legend(title='Scenario list')
    plt.xlabel('year')
    plt.ylabel('°C over pre-industrial (1760-2100 mean)')
    plt.grid()
    plt.title("Global Mean Temperature Projection")

    plt.savefig("stemperature.png", dpi=150)


if __name__=='__main__':
    main()
