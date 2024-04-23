import streamlit as st
from streamlit_folium import folium_static
import folium
import json

# Function to load GeoJSON file
def load_geojson(file):
    with open(file, 'r') as f:
        geojson_data = json.load(f)
    return geojson_data

# Main function
def main():
    st.title("GeoJSON Viewer")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload GeoJSON file", type=["geojson"])

    if uploaded_file is not None:
        # Read and parse GeoJSON file
        geojson_data = load_geojson(uploaded_file)

        # Display GeoJSON properties
        st.write("GeoJSON Properties:", geojson_data["properties"])

        # Create Folium map
        m = folium.Map(location=[0, 0], zoom_start=2)

        # Add GeoJSON layer to map
        folium.GeoJson(geojson_data, name="geojson").add_to(m)

        # Render map using streamlit-folium
        folium_static(m)

# Run the application
if __name__ == "__main__":
    main()