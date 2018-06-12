
import json
from bokeh.plotting import figure, show, output_file
from challenge35 import get_months_count

output_file("plot.html")

x_categories = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                        'September', 'October', 'November', 'December']

data = get_months_count('ch34_birthdays.json')
x = list(data.keys())
y = list(data.values())


p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)

show(p)
