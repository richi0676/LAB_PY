import folium
import pandas as pd
from flask import Flask

app = Flask(__name__)


@app.route("/")
def base():
    latitude = [31.447755, 29.806303, 40.290613]
    longitude = [-8.067835, 2.657929, -4.037180]
    map = folium.Map(
        location=[31.447755, -8.067835], zoom_start=3)
    for i in range(len(latitude)):
        folium.Circle(
            location=[latitude[i], longitude[i]],
            radius=500000,
            fill=True,
            color='red',
        ).add_to(map)

    return map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)

# Importer data
Covid_data = pd.read_csv('C:/Users/black/PycharmProjects/pythonProject/test-install/LAB1/Covid_data.csv')
