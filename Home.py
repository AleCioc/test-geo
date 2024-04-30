import osmnx as ox
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px


st.title("Dashboard geospaziale città di Milano")


if True:

    city_gdf = ox.geocode_to_gdf("Milano")

    #city_name = st.text_input("Inserisci il nome di una città:")
    #city_gdf = ox.geocode_to_gdf(city_name)

    with st.expander("Clicca per vedere dataset"):
        st.write(city_gdf.drop("geometry", axis=1))

    fig, ax = plt.subplots()
    city_gdf.plot(ax=ax)
    st.pyplot(fig)

    city_gdf_json = city_gdf.__geo_interface__

    with st.expander("Clicca per vedere GeoJSON"):
        st.write(city_gdf_json)

    city_gdf["id"] = list(range(len(city_gdf)))
    city_gdf = city_gdf.drop("geometry", axis=1)

    fig = px.choropleth_mapbox(
        city_gdf,
        geojson=city_gdf_json,
        locations='id',
        mapbox_style="carto-positron",
        center={"lat": city_gdf.lat.iloc[0], "lon": city_gdf.lon.iloc[0]},
        opacity=0.5,
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    scatter_data = {
        "lat": [45.5, 45.44],  # List of latitudes
        "lon": [9.2, 9.1],  # List of longitudes
        #"text": ["Location 1", "Location 2"],  # Optional text for each point
        "size": [20, 20]  # Optional sizes for each point
    }

    # Add scatter layer
    fig.add_scattermapbox(
        lat=scatter_data["lat"],
        lon=scatter_data["lon"],
        mode='markers+text',  # Shows both markers and text
        #marker=dict(size=scatter_data["size"], color="blue"),  # Customize marker appearance
        #text=scatter_data["text"],
        textposition="bottom right"
    )

    st.plotly_chart(fig)

else:

    st.error("Nome della città non valido!")


st.header("Area di circolazione veicolare")

area_circolazione_veicolare = gpd.read_file("DBT2012_STRATO01_E0/A010101.shp")

with st.expander("Clicca per vedere tabella completa"):
    st.dataframe(area_circolazione_veicolare.drop("geometry", axis=1))

fig, ax = plt.subplots()
area_circolazione_veicolare.plot(ax=ax)
st.pyplot(fig)


legend_string = """
A010101 Area di circolazione veicolare, 
A010102 Area di circolazione pedonale, 
A010103 Area di circolazione ciclabile, 
A010104 Area stradale, 
A010105 Viabilità mista secondaria, 
L010105 Viabilità mista secondaria, 
L010107 Elemento stradale, 
L010202 Elemento ferroviario, 
L010204 Elemento tranviario, 
L010206 Elemento di metropolitana, 
L010210 Binario industriale, 
P010108 Giunzione stradale, 
P010203 Giunzione ferroviaria, 
P010205 Giunzione tranviaria, 
P010207 Giunzione di metropolitana, 
LIM010102 Contorno area di circolazione pedonale, 
LIM010103 Contorno area di circolazione ciclabile, 
LIM010104 Contorno area stradale, 
LIM010105 Contorno viabilità mista secondaria. 
"""