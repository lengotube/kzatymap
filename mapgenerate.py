import folium
import geopandas as gpd
from folium.plugins import MarkerCluster, Search

data = gpd.read_file("/Users/grobye/Downloads/дз обл/lab13/astana_kazatu_campus.geojson")

campus_map = folium.Map(
    location=[51.187944, 71.409579],
    zoom_start=16
)

folium.TileLayer(
    tiles="https://tile2.maps.2gis.com/tiles?x={x}&y={y}&z={z}&v=1",
    attr="2ГИС",
    name="2ГИС Стандарт",
).add_to(campus_map)

# Создание кластера маркеров
marker_cluster = MarkerCluster().add_to(campus_map)

# Добавление маркеров с метками для поиска
for _, row in data.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=f"<b>{row['name']}</b><br>{row['description']}",
        icon=folium.Icon(color='orange', icon='ghost', prefix='fa')
    ).add_to(marker_cluster)

# Добавление поиска по меткам
search = Search(
    layer=marker_cluster,
    search_label="name",  # Указываем, что поиск по имени
    placeholder="Искать по названию..."
).add_to(campus_map)

folium.LayerControl().add_to(campus_map)

campus_map.save("/Users/grobye/Downloads/дз обл/lab13/kazatu_campus_map_with_search.html")
print("Карта успешно создана и сохранена.")
