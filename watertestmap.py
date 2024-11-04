import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("How to Test Water at Home")
left, middle, right = st.columns(3)
if left.button("Water Testing Kits", use_container_width=True):
    left.markdown("Home water testing kits are readily available in stores and are used to test water for contaminants. They test for things like pH, hardness, chlorine, nitrates, and bacteria.")
if middle.button("Boiling Test", use_container_width=True):
    middle.markdown("You can boil water for more than a minute to kill off most harmfull bacteria that may be in the water. Boiling won't get rid of heavy metals or chemical contaminants that may be in the water.")
if right.button("Smell and Look test", use_container_width=True):
    right.markdown("The smell and look of the water can be an indicator of quality. Cloudiness can show that the water has high mineral content or contamination. Rotten egg smell can indicate bacteria or hydrogen sulfide.")
# Define the Home Depot store locations with coordinates
locations = [
    {"name": "Blossom Hill Road", "lat": 37.2442, "lon": -121.8378, "address": "920 Blossom Hill Rd, San Jose, CA 95123"},
    {"name": "Hillsdale Avenue", "lat": 37.2731, "lon": -121.9236, "address": "1855 Hillsdale Ave, San Jose, CA 95124"},
    {"name": "Capitol Expressway", "lat": 37.2777, "lon": -121.8602, "address": "635 W Capitol Expy, San Jose, CA 95136"},
    {"name": "Monterey Highway", "lat": 37.3067, "lon": -121.8649, "address": "2181 Monterey Hwy, San Jose, CA 95125"},
    {"name": "De Anza Boulevard", "lat": 37.3072, "lon": -122.0313, "address": "975 S De Anza Blvd, San Jose, CA 95129"},
    {"name": "Story Road", "lat": 37.3542, "lon": -121.8204, "address": "2855 Story Rd, San Jose, CA 95127"}
]

# Initialize the map centered around San Jose
m = folium.Map(location=[37.3, -121.86], zoom_start=11)

# Add red dot markers to the map
for store in locations:
    folium.CircleMarker(
        location=[store["lat"], store["lon"]],
        radius=5,                  # Size of the dot
        color='red',               # Border color of the circle
        fill=True,
        fill_color='red',          # Fill color of the circle
        fill_opacity=0.8,          # Transparency
        popup=folium.Popup(f"<b>{store['name']}</b><br>{store['address']}", max_width=250),
        tooltip=store["name"]
    ).add_to(m)

# Display the map in Streamlit
st.title("Home Depot Locations That Sell Water Test Kits in San Jose")
st_folium(m, width=725, height=500)