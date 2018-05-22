from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^show_wish_list$', views.show_wish_list),
    url(r'^show_add_wish$', views.show_add_wish),
    url(r'^add_wish$', views.add_wish),
    url(r'^add_to_wish_list/(?P<wish_id>\d+)$',views.add_to_wish_list),
    url(r'^remove_from_list/(?P<wish_id>\d+)$',views.remove_from_list),
    url(r'^wish_item/(?P<wish_id>\d+)$',views.wish_item)
    
]                           