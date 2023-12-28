#Importación de bibliotecas utilizadas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset_flujo_vehicular.csv', sep=';')

#Exploración de Datos
print(df.head()) #muestra las primeras lineas del DataFrame

#Estadisticas descriptivas
print(df.describe())

# Visualización de distribución de variable
sns.histplot(df['CANTIDAD'], bins=20, kde=True)
plt.title('Distribución de CANTIDAD')
plt.show()

# Diagrama de dispersión entre dos variables
sns.scatterplot(x='CANTIDAD', y='BARRIO', data=df)
plt.title('Diagrama de Dispersión entre Cantidad y Sentido')
plt.show()