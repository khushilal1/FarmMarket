from django.shortcuts import render
from .models import Product
from plotly.offline import plot
from plotly.graph_objs import Scatter 
import json 
import plotly_express as px

# Create your views here.
def home(request):
    Date=['Jan 10','Jan 11','Jan 12','Jan 13','Jan 14','Jan 15','Jan 16','Jan 17','Jan 18','Jan 19']
    Rice_price=[65,63,64.5,59,66.5,55.5,57,68.5,70,63.5]
    basic_plot=px.line(x=Date,y=Rice_price,title="Rice price per kg(rs)")
    basic_plot.update_layout(paper_bgcolor = '#73BE73', plot_bgcolor='#73BE73')
    basic_plot.update_xaxes(title_text="Date")
    basic_plot.update_yaxes(title_text="Price")
    plot_div = basic_plot.to_html()
    return render(request,"Home/home.html",context={'plot_div': plot_div})

def products(request):
    Date=['Jan 10','Jan 11','Jan 12','Jan 13','Jan 14','Jan 15','Jan 16','Jan 17','Jan 18','Jan 19']
    Rice_price=[65,63,64.5,59,66.5,55.5,57,68.5,70,63.5]
    basic_plot=px.line(x=Date,y=Rice_price,title="Rice price per kg(rs)")
    plot_div = basic_plot.to_html()
    return render(request,"Home/products.html",context={'plot_div': plot_div})
    # products = Product.objects.all()
    # return render(request,"Home/products.html",{'products':products})