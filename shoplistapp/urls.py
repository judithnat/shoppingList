from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shop_list, name='shop_list'),
    url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
]
"""
NB: r'   its regex
^ beginning
$end
<pk>    assign result of this group  to variable name (here pk)
"""