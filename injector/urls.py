from django.urls import path


from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name="process_order"),

]