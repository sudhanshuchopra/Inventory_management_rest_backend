from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from items.api import views

urlpatterns = [
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^item/$',views.ItemList.as_view()),
    url(r'^item/(?P<pk>[0-9]+)/$',views.ItemDetail.as_view()),
    url(r'^stock_status/$',views.stock_status)
]

urlpatterns = format_suffix_patterns(urlpatterns)