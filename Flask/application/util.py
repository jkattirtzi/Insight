#from bokeh.sampledata.iris import flowers
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool

#def make_plot():
#    colormap = {"setosa": "red", "versicolor": "green", "virginica": "blue"}
#    colors = [colormap[x] for x in flowers["species"]]
#
#    p = figure(title="Iris Morphology")
#    p.xaxis.axis_label = "Petal Length"
#    p.yaxis.axis_label = "Petal Width"
#
#    p.circle(
#        flowers["petal_length"],
#        flowers["petal_width"],
#        color=colors,
#        fill_alpha=0.2,
#        size=10,
#    )

 #   return p
def make_plot(df):
    pvalues=df['power']
    pred=df['Predictions']
    x=df['T_T0_s']
    y=pvalues.values
    y2=pred.values
    lon=df['longitude']
    lat=df['latitude']
    lon=lon.values
    lat=lat.values
#    source = ColumnDataSource(data=dict(x, y, y2, lon, lat,))
#    source = ColumnDataSource(
#    x,
#    y,
#    y2,
#)
#    source=ColumnDataSource(data=dict(x=x, y=y, lon=lon,lat=lat))
    source=ColumnDataSource(df)


    TOOLTIPS =[("Time","@T_T0_s"),
               ("Actual Power","@power"),
               ("Predicted Power","@Predictions"),
               ("Longitude", "@longitude"),
               ("Latitude", "@latitude"), ]
    p = figure(plot_height=400, plot_width=500, title="Actual and Predicted Power", tools='hover,wheel_zoom',tooltips=TOOLTIPS  )
    p.xaxis.axis_label = "Time (s)"
    p.yaxis.axis_label = "Power (W)"
    p.line('T_T0_s','power' , color='blue', legend="Actual Power",source=source)
    p.circle('T_T0_s', 'Predictions', size=5, color='red',legend="Predicted Power", source=source)
    p.legend.location = "top_left"
    return p
#show(p)

