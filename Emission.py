import pymagicc
from pymagicc import MAGICC6
import pandas as pd

from matplotlib import pyplot as plt


def main():
    '''
    This function plot Emissions.png which shows the Emission of Fossil and Industrial
    '''
    data_dfrm=pd.read_csv('rawrcps_dataset.csv')

    datafrm_filtered = data_dfrm[(data_dfrm.region == 'World') & (data_dfrm.variable == 'Emissions|CO2|MAGICC Fossil and Industrial')]

    datafrm_filtered= datafrm_filtered.drop(['climate_model', 'model', 'region', 'todo', 'unit', 'variable'], axis=1)
    newdatafrm= datafrm_filtered.T.reset_index().drop(0)
    newdatafrm.dropna(inplace=True)

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
    plt.ylabel('Emissions|CO2|MAGICC Fossil and Industrial')
    plt.grid()
    plt.title("Emissions|CO2|MAGICC Fossil and Industrial projection")

    plt.savefig("Emissions.png", dpi=150)


if __name__=='__main__':
    main()

