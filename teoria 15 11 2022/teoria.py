import pandas as pd
import matplotlib.pyplot as plt

def definirHistograma():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX']]
    df.CRIM.plot.hist()
    plt.show()

#definirHistograma()

def consumir():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX']]
    df.plot.scatter(x='CRIM', y='town', alpha=0.2)
    plt.show()
#consumir()

def consumirBarras():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX']]
    df.plot.scatter(x='CRIM', y='town', alpha=0.2)
    plt.show()

consumirBarras()