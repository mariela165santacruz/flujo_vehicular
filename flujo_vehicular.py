# Importación de bibliotecas utilizadas
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
from shapely.geometry import Point

# Cargar datos desde un archivo CSV
df = pd.read_csv('dataset_flujo_vehicular.csv', sep=';')

# Filtrar filas con coordenadas válidas
df = df.dropna(subset=['LONGITUD', 'LATITUD'])

# Crear GeoDataFrame a partir de DataFrame
geometry = [Point(xy) for xy in zip(df['LONGITUD'], df['LATITUD'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)
gdf.crs = "EPSG:4326"  # Asignar el sistema de referencia espacial (CRS)

# Crear un mapa centrado en CABA
caba_map = folium.Map(location=[-34.61, -58.38], zoom_start=12)

# Crear un mapa de calor con las coordenadas
heat_data = [[point.xy[1][0], point.xy[0][0]] for point in gdf.geometry]
HeatMap(heat_data).add_to(caba_map)

# Guardar el mapa como un archivo HTML
caba_map.save("mapa_calor_caba.html")

