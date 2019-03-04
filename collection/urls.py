from django.urls import path
from . import views

urlpatterns = [
    path('', views.collections_list, name='collection_list'),

    path('new_collection/', views.new_collection, name='new_collection'),
    path('collection_items/<int:id>',
         views.collection_items, name='collection_items'),
    path('edit_collection/<int:id>',
         views.edit_collection, name='edit_collection'),
    path('delete_collection/<int:id>',
         views.delete_collection, name='delete_collection'),

    path('item_info/<int:id>', views.item_info, name='item_info'),
    path('new_item/', views.new_item, name='new_item'),
    path('delete_item/<int:id>', views.delete_item , name='delete_item'),

    path('category_filter/<int:id>', views.category_filter, name='category_filter'),
]
