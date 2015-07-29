#! /usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
from bokeh.charts import Area, show, output_file

# create some example data
xyvalues = OrderedDict(
    emacs=[500, 823, 774, 981, 913, 913, 934, 813, 956, 942, 923, 912, 934, 999],
    vx=[12, 33, 47, 15, 12, 12, 14, 23, 25, 22, 226, 26, 11, 13],
    atxx=[22, 43, 10, 25, 26, 101, 114, 203, 194, 215, 201, 227, 139, 160],
    sublxxx=[22, 43, 10, 25, 26, 101, 114, 203, 194, 215, 201, 227, 139, 160],
)

output_file(filename="index.html")

area = Area(
    xyvalues, title="Editor",
    stacked=True, legend="top_left"
).legend("top_left")

show(area)
