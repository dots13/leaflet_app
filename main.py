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

    # Display the map
    folium_static(m)

    # File uploader widget
    uploaded_file = st.file_uploader("Upload GeoJSON file", type=["geojson"])

    if uploaded_file is not None:
        # Read and parse GeoJSON file
        geojson_data = json.load(uploaded_file)

        # Add GeoJSON layer to map
        layer = folium.GeoJson(geojson_data)
        layer.add_to(m)

        # Clear the existing map and replace it with the updated one
        folium_map.empty()
        folium_static(m)

        # Add layer control to the map
        folium.LayerControl().add_to(m)

        # Create a multiselect widget to choose active layers
        active_layers = st.multiselect("Select active layers", [layer.get_name()], [layer.get_name()])

        # Toggle layer visibility based on user selection
        for l in m._children.values():
            if isinstance(l, folium.Layer) and l.get_name() not in active_layers:
                m.remove_layer(l)

if __name__ == "__main__":
    main()
