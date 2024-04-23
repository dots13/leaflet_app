import streamlit as st
from streamlit_folium import folium_static
import folium
import json

def main():
    st.title("GeoJSON Viewer")

    # Create or load the Folium map
    folium_map = st.empty()

    # Initialize the map with default location and zoom
    m = folium.Map(location=[0, 0], zoom_start=2)

    # File uploader widget
    uploaded_file = st.file_uploader("Upload GeoJSON file", type=["geojson"])

    if uploaded_file is not None:
        # Read and parse GeoJSON file
        geojson_data = json.load(uploaded_file)

        # Add style
        def style_function(feature):
            color = feature['properties'].get('color', 'blue') 
            return {
                'fillColor': color,
                'color': color,
                'weight': 2.5,
                'fillOpacity': 0.5
        }

        # Add GeoJSON layer to map
        layer = folium.GeoJson(geojson_data, style_function=style_function).add_to(m)
        layer.add_to(m)


        
        # Clear the existing map and replace it with the updated one
        folium_map.empty()
        folium_static(m)

        # Add layer control to the map
        folium.LayerControl().add_to(m)

def extract_coords(feature):
    geom_type = feature['geometry']['type']
    if geom_type == 'Polygon':
        return feature['geometry']['coordinates'][0]  # Assuming a single polygon
    elif geom_type == 'LineString':
        return feature['geometry']['coordinates']
    elif geom_type == 'MultiPoint':
        return feature['geometry']['coordinates']
    elif geom_type == 'MultiLineString':
        coords = []
        for line_string in feature['geometry']['coordinates']:
            coords.extend(line_string)
        return coords
    else:
        raise ValueError(f"Unsupported geometry type: {geom_type}")

if __name__ == "__main__":
    main()
