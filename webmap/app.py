import folium

map = folium.Map(location=[12.924474,77.672475], zoom_start=15, titles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[12.924474,77.672475], popup="Cloud 9 Hospital", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[12.924474,77.562475], popup="Testing", icon=folium.Icon(color='red')))

map.add_child(fg)
map.save("Map1.html")