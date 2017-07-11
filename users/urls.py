from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from users.api import views

urlpatterns = [
    url(r'^users/items/(?P<email>[\w.@+-]+)$', views.get_items),
    url(r'^additems$',views.add_items),
    url(r'^requestitems$',views.request_item),
    url(r'^updateitems$',views.update_items),

]

urlpatterns = format_suffix_patterns(urlpatterns)