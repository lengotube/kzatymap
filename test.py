import geopandas as gpd

# Загрузка данных
data = gpd.read_file("astana_kazatu_campus.geojson")

# Проверка данных
print(data.head())

# Очистка (например, удаление дублирующих записей)
data = data.drop_duplicates()
