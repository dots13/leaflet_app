import streamlit as st
from streamlit_folium import folium_static
import folium
import json

def main():
    st.title("GeoJSON Viewer")

    # Create a placeholder for the Folium map
    folium_map = folium.Map(location=[0, 0], zoom_start=2)

    # Display the map as a Streamlit widget
    folium_static(folium_map)

    # File uploader widget
    uploaded_file = st.file_uploader("Upload GeoJSON file", type=["geojson"])

    if uploaded_file is not None:
        # Read and parse GeoJSON file
        geojson_data = json.load(uploaded_file)

        # Add GeoJSON layer to map
        folium.GeoJson(geojson_data).add_to(folium_map)

        # Update the map widget
        folium_static(folium_map)

if __name__ == "__main__":
    main()
