from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('fetch_data/', views.fetch_data, name='fetch_data'),
    path('control/', views.control_view, name='control'),

    # path("business", views.business, name="Business"),
    # path("about/", views.about, name="AboutUs"),
    # path("contact/", views.contact, name="ContactUs"),
    # # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),

]
