from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
import pandas as pd
import json
import plotly
import plotly.express as px
import serial

# from backend.sensorDB.sensor_list import sensor_list
# from backend.sensorDB.retreive import get_latest_data_by_sensor_id, get_sensor_id_by_pin

app = Flask(__name__)

# sensors = sensor_list()

sqlite_db = 'db/sensorData.sqlite'


@app.route('/')
def index():

    now = datetime.now()

    templateData = {
        "time": now,
        "1.1": None,
        "1.2": None,
        "1.3": None,
        "1.4": None,
        "2.1": None,
        "2.2": None,
        "2.3": None,
        "2.4": None,
    }

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
    conn = sqlite3.connect(sqlite_db)

    df_vi1 = pd.read_sql_query(
        """
        SELECT * FROM measurements WHERE measureType='temperature' AND vivarium_id=1
        """
        , conn)

    conn.close()

    fig = px.line(df_vi1, x='timestamp', y='value', color='sensor_position', markers=True)
    fig.update_xaxes(title_text='Time')
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=6, label="6h", step="hour", stepmode="backward"),
                dict(count=12, label="12h", step="hour", stepmode="backward"),
                dict(count=1, label="1d", step="day", stepmode="todate"),
                dict(count=7, label="1w", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=3, label="1q", step="month", stepmode="backward"),
                dict(count=6, label="1/2y", step="month", stepmode="backward"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        tickformatstops = [
            dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
            dict(dtickrange=[1000, 60000], value="%H:%M:%S s"),
            dict(dtickrange=[60000, 3600000], value="%H:%M m"),
            dict(dtickrange=[3600000, 86400000], value="%H:%M h"),
            dict(dtickrange=[86400000, 604800000], value="%e. %b d"),
            dict(dtickrange=[604800000, "M1"], value="%e. %b w"),
            dict(dtickrange=["M1", "M12"], value="%b '%y M"),
            dict(dtickrange=["M12", None], value="%Y Y")
        ]
    )
    # fig.update_yaxes(title_text='Temperature (ºC)', range=[10., 40.])
    fig.update_yaxes(title_text='Temperature (ºC)',)

    graphJSON_1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    conn = sqlite3.connect(sqlite_db)

    df_vi2 = pd.read_sql_query(
        """
        SELECT * FROM measurements WHERE measureType='temperature' AND vivarium_id=2
        """
        , conn)

    conn.close()

    fig = px.line(df_vi2, x='timestamp', y='value', color='sensor_position', markers=True)
    fig.update_xaxes(title_text='Time')
    # fig.update_yaxes(title_text='Temperature (ºC)', range=[10., 40.])
    fig.update_yaxes(title_text='Temperature (ºC)',)

    graphJSON_2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # return df_vi1.to_html()
    # return render_template('index.html', **templateData)
    # return render_template('index.html', **templateData, graphJSON=graphJSON)
    return render_template('index.html', graphJSON_1=graphJSON_1, graphJSON_2=graphJSON_2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
