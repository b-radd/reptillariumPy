from flask import Flask, render_template, request
# import sqlite3
from datetime import datetime
import pandas as pd
import json
import plotly
import plotly.express as px
#
# from backend.sensorDB.sensor_list import sensor_list
# from backend.sensorDB.retreive import get_latest_data_by_sensor_id, get_sensor_id_by_pin

app = Flask(__name__)

# sensors = sensor_list()

# sqlite_db = 'sqliteDB/reptillarium.sqlite'


@app.route('/')
def index():

    now = datetime.now()

    templateData = {
        "time": now,
        "uv1_1_uv": None,
        "uv2_1_uv": None,
        "dht1_1_temp": None,
        "dht1_1_humid": None,
        "dht2_1_temp": None,
        "dht2_1_humid": None,
        "ow1_1_temp": None,
        "ow1_2_temp": None,
        "ow2_1_temp": None,
        "ow2_2_temp": None,
    }
    #
    # for s in sensors:
    #     if "relay" not in s:
    #
    #         spin = sensors.get(s).get("pin")
    #         sid = get_sensor_id_by_pin(sqlite_db, spin)
    #         latest_value = get_latest_data_by_sensor_id(sqlite_db, sid)
    #
    #         for sid_html in [key for key in templateData.keys() if s in key.lower()]:
    #             if sid_html and latest_value.get("measurementType"):
    #                 for sid_type in latest_value.get("measurementType").keys():
    #                     if sid_html.replace(s + "_", "") in sid_type:
    #                         templateData[sid_html] = "{:0.1f}".format(
    #                                 latest_value.get("measurementType").get(sid_type).get("measurementValue")
    #                             )
    #
    # conn = sqlite3.connect(sqlite_db)
    #
    # df = pd.read_sql_query("SELECT * FROM measurements WHERE measureType='temperature'", conn)
    #
    # conn.close()
    #
    # fig = px.line(df, x='timestamp', y='value', color='sensor_id', markers=True)
    # fig.update_xaxes(title_text='Time')
    # fig.update_yaxes(title_text='Temperature (ºC)', range=[0., 50.])
    #
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', **templateData)
    # return render_template('index.html', **templateData, graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
