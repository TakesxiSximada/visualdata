# -*- coding: utf-8 -*-
import time
from numpy import cumprod, linspace, random
from bokeh.plotting import figure, show, output_file

num_points = 300
now = time.time()
dt = 24 * 3600  # days in seconds
dates = linspace(now, now + num_points*dt, num_points) * 1000  # times in ms

acme = cumprod(random.lognormal(0.0, 0.02, size=600))
choam = cumprod(random.lognormal(0.0, 0.04, size=600))

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

output_file("index.html", title="なんとなく自分の気分が良くなるグラフ")
r = figure(x_axis_type="datetime", tools=TOOLS)
r.line(dates, acme, color='#1F78B4', legend='Other')
r.line(dates, choam, color='#FB9A99', legend='Emacs')

r.title = "なんとなく自分の気分が良くなるグラフ"
r.grid.grid_line_alpha = 0.3
show(r)
