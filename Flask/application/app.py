# Another example chaining Bokeh's to Flask.

from bokeh.embed import components
from flask import Flask, render_template, flash, request, redirect, url_for
import bokeh
import pandas as pd
from util import make_plot
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool
from bokeh.plotting import gmap


import json

app = Flask(__name__)


#create the main plot




def process_input(route_n):
    option = get_option(route_n)
    return option

def get_option(route_n):
    r_options = {"Route 1":"Route1", "Route 2":"Route2", "Route 3": "Route3", "Route 4": "Route4", "Route 5": "Route5"}
    return r_options[route_n]


def create_figure(df):
    return fig

def get_coords(df):
    lon=df["longitude"].values
    lat=df["latitude"].values
    lat_mean=(lat.max()-lat.min())/2.0+ lat.min()
    lon_mean=(lon.max()-lon.min())/2.0 + lon.min()
    coords=dict(lat=df["latitude"].values,
              lon=df["longitude"].values)
    return coords, lat_mean, lon_mean

@app.route('/option', methods=['GET','POST'])
def option():
    if request.method == 'GET':
        route_n = request.args.get('route_n', '')
        option  = get_option(route_n)
        if option =="Route1" :
            df=pd.read_csv("./data/df1out.csv")
            coords,lat_mean,lon_mean=get_coords(df)
        elif option=="Route2" :
            df=pd.read_csv("./data/df2out.csv")
            coords,lat_mean,lon_mean=get_coords(df)
        elif option=="Route3" :
            df=pd.read_csv("./data/df3out.csv")
            coords,lat_mean,lon_mean=get_coords(df)
        elif option=="Route4" :
            df=pd.read_csv("./data/df4out.csv")
            coords,lat_mean,lon_mean=get_coords(df)
        elif option=="Route5" :
            df=pd.read_csv("./data/df5out.csv")
            coords,lat_mean,lon_mean=get_coords(df)
        figure = make_plot(df)
        fig_script, fig_div = components(figure)

    map_options = GMapOptions(lat=lat_mean, lng=lon_mean, map_type="roadmap", zoom=14)
    #map_options = GMapOptions(lat=51.759, lng=-1.255, map_type="roadmap", zoom=15)
    google_api='AIzaSyBdPAkzHMWahHjT9ml9zGeM6pR3u-VucKc'
    fig_map = gmap(google_api, map_options, title="Route Taken", plot_height=400, plot_width=500)
    fig_map.xaxis.axis_label= 'Longitude'
    fig_map.yaxis.axis_label= 'Latitude'
    source = ColumnDataSource(coords )
    fig_map.circle(x="lon", y="lat", size=5, fill_color="blue", fill_alpha=0.8, source=source)
#    show(fig_map)
    script2,div2=components(fig_map)  



    #figure = make_plot()
    #fig_script, fig_div = components(figure)
    return render_template(
        "location2.html.j2", option=option, route_n=route_n,
        fig_script=fig_script,
        fig_div=fig_div,
        bkversion=bokeh.__version__, df=df, script2=script2,div2=div2
    )



#    return render_template(
#        "bokeh.html.j2",
#        fig_script=fig_script,
#        fig_div=fig_div,
#        bkversion=bokeh.__version__,
#    )


#make bokeh plot here
        
 #       return render_template('location.html.j2', option=option, route_n=route_n,

  #          fig_script=fig_script,
  #          fig_div=fig_div,
#            bkversion=bokeh.__version__,
 
#        )
#def bokehplot():
#    return render_template(
#        "bokeh.html.j2",
#        fig_script=fig_script,
#        fig_div=fig_div,
#        bkversion=bokeh.__version__,
#    )




@app.route("/")
def home():
    return render_template("index.html.j2")


@app.route("/bokehplot")
def bokehplot():
    figure = make_plot()
    fig_script, fig_div = components(figure)
    return render_template(
        "bokeh.html.j2",
        fig_script=fig_script,
        fig_div=fig_div,
        bkversion=bokeh.__version__,
    )

@app.route('/slides')
def slides():
#    return redirect("https://docs.google.com/presentation/d/1cO9C43kTWr7ESRIlZbDpgL7jUplbcETwpupVDkttXCE/edit?usp=sharing")
    return redirect("https://docs.google.com/presentation/d/e/2PACX-1vR1Yboc3JPcWt3px-gM8d5u9aVCQ8-NgJFyoU9Xjf9dJRVxHiKX_E2SqIa4RLL3MoXBKfUdfy8uqR5s/pub?start=false&loop=false&delayms=3000")

if __name__ == "__main__":
    app.run(debug=True, port=5957)


