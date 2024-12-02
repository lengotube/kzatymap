import json

data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [71.409579, 51.187944]
            },
            "properties": {
                "name": "Второй корпус",
                "description": "Второй корпус, БИОФак"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [71.412948, 51.186956]
            },
            "properties": {
                "name": "Общежитие №1",
                "description": "Общежитие для студентов"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [71.412732, 51.187521]
            },
            "properties": {
                "name": "Столовая",
                "description": "8 столовая"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [71.409660, 51.187058]
            },
            "properties": {
                "name": "Главный корпус",
                "description": "Казахский агротехнический исследовательский университет имени Сакена Сейфуллина"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [71.410650, 51.186704]
            },
            "properties": {
                "name": "Военная кафедра",
                "description": "Казахский агротехнический университет имени Сакена Сейфуллина, военная кафедра"
            }
        },
    ]
}

with open("astana_kazatu_campus.geojson", "w") as f:
    json.dump(data, f)
