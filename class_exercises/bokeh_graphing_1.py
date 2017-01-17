# import pandas and bokeh
from bokeh.plotting import figure, output_file, save
import numpy as np
import pandas as pd

# create set of values for x and y
x = [n for n in range(10)]                                                                                                                   
y = [np.random.randint(10) for n in x]                                                                                                       

# create html file
output_file('bokeh_graph_1.html')

# make figure
figure_1 = figure(width = 400, height = 400)
figure_1.circle(x,y)
save(figure_1)

# make another figure
y2 = np.random.rand(10) * 10
figure_1.asterisk(x, y2, line_color='black', size = 10)
save(figure_1)

# make yet another figure
y3 = np.random.randint(10)
figure_1.line(x, y3, line_color='red')
# Add markers representing each y value
figure_1.square(x, y3, line_color='black', fill_color='purple', fill_alpha=.5, size=15)
save(figure_1)