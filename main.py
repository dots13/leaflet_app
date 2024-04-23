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
        folium.GeoJson(geojson_data, style_function=style_function).add_to(m)

        # Clear the existing map and replace it with the updated one
        folium_map.empty()
        folium_static(m)

        # Add layer control to the map
        folium.LayerControl().add_to(m)

if __name__ == "__main__":
    main()
