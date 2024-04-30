import osmnx as ox
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt


st.title("Dashboard geospaziale città di Milano")

try:

    # city_name = st.text_input("Inserisci il nome di una città:")
    city_gdf = ox.geocode_to_gdf("Milano")
    #city_gdf.crs = "epsg:4326"
    #city_gdf = city_gdf.to_crs("epsg:3857")

    print(city_gdf.crs)
    with st.expander("Clicca per vedere dataset"):
        st.write(city_gdf)

    # fig, ax = plt.subplots()
    # city_gdf.plot(ax=ax)
    # st.pyplot(fig)
    #
    # city_gdf_json = city_gdf.to_json()
    #
    # with st.expander("Clicca per vedere GeoJSON"):
    #     st.write(city_gdf_json)
    #
    # import plotly.express as px
    #
    # fig = px.choropleth_mapbox(
    #     city_gdf.drop("geometry", axis=1),
    #     geojson=city_gdf.to_json(),
    #     #locations='fips',
    #     #color='unemp',
    #     color_continuous_scale="Viridis",
    #     #range_color=(0, 12),
    #     mapbox_style="carto-positron",
    #     zoom=3,
    #     center = {"lat": 45, "lon": 9},
    #     opacity=0.5,
    #     #labels={'unemp':'unemployment rate'}
    # )
    # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # # fig.show()
    #
    # st.plotly_chart(fig)

except:

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