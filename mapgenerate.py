import streamlit as st
import folium
import geopandas as gpd
from folium.plugins import MarkerCluster, Search
from streamlit_folium import st_folium

# Заголовок приложения
st.title("Карта кампуса КазАТУ")

# Загрузка данных GeoJSON
data = gpd.read_file("astana_kazatu_campus.geojson")

# Создание карты
campus_map = folium.Map(
    location=[51.187944, 71.409579],
    zoom_start=16

)

# Добавление тайлов
folium.TileLayer(
    tiles="https://tile2.maps.2gis.com/tiles?x={x}&y={y}&z={z}&v=1",
    attr="2ГИС",
    name="2ГИС Стандарт",
).add_to(campus_map)

# Кластер маркеров
marker_cluster = MarkerCluster().add_to(campus_map)

# Добавление маркеров с данными из GeoJSON
for _, row in data.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=f"<b>{row['name']}</b><br>{row['description']}",
        icon=folium.Icon(color='orange', icon='info-sign')
    ).add_to(marker_cluster)

# Добавление поиска
search = Search(
    layer=marker_cluster,
    search_label="name",
    placeholder="Искать по названию..."
).add_to(campus_map)

# Добавление переключателя слоёв
folium.LayerControl().add_to(campus_map)

# Отображение карты в Streamlit
st_folium(campus_map, width=800, height=600)
