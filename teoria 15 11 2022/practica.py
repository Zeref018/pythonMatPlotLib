#consume los datos del archivo inversiones
#almacena en un dataFrame el título, el importe y el distrito
#gráfico de dispersiçon de los importes de inversiones por distrito
#grafico de barras de la inversion media de los 10 primeros distritos
#grafico circular de las inversiones de 10 titulos


import pandas as pd
import matplotlib.pyplot as plt

datos=pd.read_csv('Classificaci%C3%B3_del_s%C3%B2l.csv')
df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL', 'CODI_TIPUSSOL']]
df.head(10).plot.scatter(x='SUPERFICIE', y='TIPUSSOL', alpha=0.2)
plt.show()

valor_por_ciudad = df.groupby("SUPERFICIE")["CODI_TIPUSSOL"].mean()
valor_por_ciudad.head(10).plot.barh()
plt.show()