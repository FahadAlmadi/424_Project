from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
       path('', views.item_list, name='item_list'),
       path('item/<int:pk>/', views.item_detail, name='item_detail'),
       path('item/new/', views.item_create, name='item_create'),
       path('item/<int:pk>/edit/', views.item_edit, name='item_edit'),
       path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),
       path('items_purchased_list/',views.items_purchased,name='purchased_items'),
       path('add_item_to_purchased/<int:item_id>/',views.add_item_to_purchased,name='add_item_to_purchased'),
       path('remove_item_from_purchased/<int:item_id>/',views.remove_item_from_purchased,name='remove_item_from_purchased'),
     
   ]