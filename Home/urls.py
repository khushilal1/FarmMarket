from django.urls import path 
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("products/",views.products,name='products'),
    path("products/<str:productname>",views.graph_view,name='graph_view'),
    path("seller/",views.seller,name="seller"),
    path("buyer/",views.buyer,name="buyer"),

]