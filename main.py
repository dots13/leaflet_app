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

        def style_function(feature):
            color = feature['properties'].get('color', 'blue') 
            return {
                'fillColor': color,
                'color': color,
                'weight': 1.5,
                'fillOpacity': 0.5
        }

        # Add GeoJSON layer to map
        layer = folium.GeoJson(geojson_data, style_function=style_function).add_to(m)
        layer.add_to(m)

        # Calculate bounding box of GeoJSON features
        bbox = [[float('inf'), float('inf')], [float('-inf'), float('-inf')]]
        for feature in geojson_data['features']:
            coords = feature['geometry']['coordinates']
            for coord in coords:
                bbox[0][0] = min(bbox[0][0], coord[1])
                bbox[0][1] = min(bbox[0][1], coord[0])
                bbox[1][0] = max(bbox[1][0], coord[1])
                bbox[1][1] = max(bbox[1][1], coord[0])

        # Set map viewport to bounding box
        m.fit_bounds(bbox)
        
        # Clear the existing map and replace it with the updated one
        folium_map.empty()
        folium_static(m)

        # Add layer control to the map
        folium.LayerControl().add_to(m)

if __name__ == "__main__":
    main()
