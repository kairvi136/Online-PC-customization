from django.urls import path
from django.utils.regex_helper import normalize
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:category_slug>/', views.shop, name='categries'),
    path('shop/<slug:category_slug>/<slug:product_details_slug>/', views.product_details, name='product_details'),
    path('search/', views.search, name='search'),
    path('review/<int:product_id>/', views.review, name='review'),
    path('gaming_chair/', views.Gaming_chair, name="Gaming_chair"),
    path('processor/', views.Processor, name="Processor"),
    path('mouse/', views.Mouse, name="Mouse"),
    path('monitor/', views.Monitor, name="Monitor"),
    path('motherboard/', views.Motherboard, name="Motherboard"),
    path('ssd/', views.SSD, name="SSD"),
    path('keyboard/', views.Keyboard, name="Keyboard"),
    path('graphics_card/', views.Graphics_card, name="Graphics_card"),
    path('storage/', views.Storage, name="Storage"),
    path('mouse_pad/', views.Mouse_pad, name="Mouse_pad"),
    path('glass_cleaner/', views.Glass_cleaner, name="Glass_cleaner"),
    path('earphone/', views.Earphone, name="Earphone"),
    path('laptop/', views.Laptop, name="Laptop"),
    path('laptop_stand/', views.Laptop_stand, name="Laptop_stand"),
]
