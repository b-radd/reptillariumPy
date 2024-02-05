from flask import Flask, render_template, request
import sqlite3
from datetime import datetime, timedelta
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
import serial
from waitress import serve

# from backend.sensorDB.sensor_list import sensor_list
# from backend.sensorDB.retreive import get_latest_data_by_sensor_id, get_sensor_id_by_pin

app = Flask(__name__)

# sensors = sensor_list()

sqlite_db = 'db/sensorData.sqlite'


@app.route('/')
def index():

    now = datetime.now()
    backdate = 7

    conn = sqlite3.connect(sqlite_db)

    latest_read = pd.read_sql_query(
        """
        SELECT * FROM measurements
        """
        , conn)

    templateData = {
        "time": latest_read['timestamp'].max(),
    }

    for group, data in latest_read.groupby('sensor_id'):
        templateData[group.replace('.', '_')] = data.loc[data['timestamp'] == data['timestamp'].max()]['value'].values[0]

    # print(latest_read.to_string())

    conn.close()

    # print(templateData)

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

    df = pd.read_sql_query(
        """
        SELECT * FROM measurements WHERE measureType='temperature' AND vivarium_id=1
        """
        , conn)

    conn.close()

    fig = go.Figure()

    for group, data in df.groupby('sensor_position'):
        fig.add_trace(go.Line(
            x=data['timestamp'],
            y=data['value'],
            name=group,
            yaxis='y'
        )
        )

    conn = sqlite3.connect(sqlite_db)

    # df = pd.read_sql_query(
    #     """
    #     SELECT * FROM measurements WHERE measureType='humidity' AND vivarium_id=1
    #     """
    #     , conn)
    #
    # conn.close()

    for group, data in df.groupby('sensor_position'):
        fig.add_trace(go.Line(
            x=data['timestamp'],
            y=data['value'],
            name=group,
            yaxis='y2'
        )
        )

    fig = px.line(df, x='timestamp', y='value', color='sensor_position', markers=True)
    fig.update_xaxes(title_text='Time')
    # fig.update_xaxes(
    #     rangeslider_visible=False,
    #     rangeselector=dict(
    #         buttons=list([
    #             dict(count=3, label="3h", step="hour", stepmode="backward"),
    #             dict(count=6, label="6h", step="hour", stepmode="backward"),
    #             dict(count=12, label="12h", step="hour", stepmode="backward"),
    #             dict(count=24, label="1d", step="hour", stepmode="todate"),
    #             dict(count=7, label="1w", step="day", stepmode="backward"),
    #             dict(count=14, label="2w", step="day", stepmode="backward"),
    #             # dict(count=3, label="1q", step="month", stepmode="backward"),
    #             # dict(count=6, label="1/2y", step="month", stepmode="backward"),
    #             # dict(count=1, label="1y", step="year", stepmode="backward"),
    #             dict(step="all")
    #         ])
    #     ),
    #     tickformatstops=[
    #         # dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
    #         dict(dtickrange=[1000, 60000], value="%I:%M:%S %p"),
    #         dict(dtickrange=[60000, 3600000], value="%I:%M %p"),
    #         dict(dtickrange=[3600000, 86400000], value="%I %p"),
    #         dict(dtickrange=[86400000, 604800000], value="%e. %b"),
    #         dict(dtickrange=[604800000, "M1"], value="%e. %b"),
    #         dict(dtickrange=["M1", "M12"], value="%b '%y"),
    #         dict(dtickrange=["M12", None], value="%Y")
    #     ]
    # )
    # fig.update_yaxes(title_text='Temperature (ºC)', range=[10., 40.])
    # fig.update_yaxes(title_text='Temperature (ºC)',)
    fig.update_layout(
        xaxis=dict(
            title_text='Time',
            rangeslider_visible=False,
            rangeselector=dict(
                buttons=list([
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(count=6, label="6h", step="hour", stepmode="backward"),
                    dict(count=12, label="12h", step="hour", stepmode="backward"),
                    dict(count=24, label="1d", step="hour", stepmode="backward"),
                    # dict(count=7*24, label="1w", step="hour", stepmode="backward"),
                    # dict(count=14, label="2w", step="day", stepmode="backward"),
                    # dict(count=3, label="1q", step="month", stepmode="backward"),
                    # dict(count=6, label="1/2y", step="month", stepmode="backward"),
                    # dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            ),
            tickformatstops=[
                # dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
                dict(dtickrange=[1000, 60000], value="%I:%M:%S %p"),
                dict(dtickrange=[60000, 3600000], value="%I:%M %p"),
                dict(dtickrange=[3600000, 86400000], value="%I %p"),
                dict(dtickrange=[86400000, 604800000], value="%e. %b"),
                dict(dtickrange=[604800000, "M1"], value="%e. %b"),
                # dict(dtickrange=["M1", "M12"], value="%b '%y"),
                # dict(dtickrange=["M12", None], value="%Y")
            ]
        ),

        # yaxis=dict(
        #     title_text='Temperature (ºC)',
        #     titlefont=dict(color="#1f77b4"),
        #     tickfont=dict(color="#1f77b4"),
        #     showgrid=False,
        # ),
        #
        # yaxis2=dict(
        #     title_text="yaxis2 title",
        #     overlaying="y",
        #     side="right",
        #     position=1.,
        #     showgrid=False,
        # ),
    )


    graphJSON_1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    conn = sqlite3.connect(sqlite_db)

    df = pd.read_sql_query(
        """
        SELECT * FROM measurements WHERE measureType='temperature' AND vivarium_id=2
        """
        , conn)

    conn.close()

    fig = px.line(df, x='timestamp', y='value', color='sensor_position', markers=True)
    fig.update_xaxes(title_text='Time')
    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(count=6, label="6h", step="hour", stepmode="backward"),
                dict(count=12, label="12h", step="hour", stepmode="backward"),
                dict(count=24, label="1d", step="hour", stepmode="backward"),
                # dict(count=7 * 24, label="1w", step="hour", stepmode="backward"),
                # dict(count=14, label="2w", step="day", stepmode="backward"),
                # dict(count=3, label="1q", step="month", stepmode="backward"),
                # dict(count=6, label="1/2y", step="month", stepmode="backward"),
                # dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        tickformatstops=[
            # dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
            dict(dtickrange=[1000, 60000], value="%I:%M:%S %p"),
            dict(dtickrange=[60000, 3600000], value="%I:%M %p"),
            dict(dtickrange=[3600000, 86400000], value="%I %p"),
            dict(dtickrange=[86400000, 604800000], value="%e. %b"),
            dict(dtickrange=[604800000, "M1"], value="%e. %b"),
            # dict(dtickrange=["M1", "M12"], value="%b '%y"),
            # dict(dtickrange=["M12", None], value="%Y")
        ]
    )

    graphJSON_2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    conn = sqlite3.connect(sqlite_db)

    df = pd.read_sql_query(
        """
        SELECT * FROM measurements WHERE measureType='humidity' AND vivarium_id=2
        """
        , conn)

    conn.close()

    fig = px.line(df, x='timestamp', y='value', color='sensor_position', markers=True)
    fig.update_xaxes(title_text='Time')
    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(count=6, label="6h", step="hour", stepmode="backward"),
                dict(count=12, label="12h", step="hour", stepmode="backward"),
                dict(count=24, label="1d", step="hour", stepmode="backward"),
                # dict(count=7 * 24, label="1w", step="hour", stepmode="backward"),
                # dict(count=14, label="2w", step="day", stepmode="backward"),
                # dict(count=3, label="1q", step="month", stepmode="backward"),
                # dict(count=6, label="1/2y", step="month", stepmode="backward"),
                # dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        tickformatstops=[
            # dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
            dict(dtickrange=[1000, 60000], value="%I:%M:%S %p"),
            dict(dtickrange=[60000, 3600000], value="%I:%M %p"),
            dict(dtickrange=[3600000, 86400000], value="%I %p"),
            dict(dtickrange=[86400000, 604800000], value="%e. %b"),
            dict(dtickrange=[604800000, "M1"], value="%e. %b"),
            # dict(dtickrange=["M1", "M12"], value="%b '%y"),
            # dict(dtickrange=["M12", None], value="%Y")
        ]
    )

    graphJSON_3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # return df_vi1.to_html()
    # return render_template('index.html', **templateData)
    # return render_template('index.html', **templateData, graphJSON=graphJSON)
    return render_template(
        'index.html',
        **templateData,
        graphJSON_1=graphJSON_1,
        graphJSON_2=graphJSON_2,
        graphJSON_3=graphJSON_3,
    )


if __name__ == '__main__':
    # app.run(host='192.168.0.219', port=8090)
    serve(app, host='192.168.0.219', port=8090)
    # serve(app, host='0.0.0.0', port=8090)
