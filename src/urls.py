# from django.conf.urls import url
#
# from src.views import PostManager
#
# urlpatterns = [
#     url(r'all', PostManager.as_view(), name='all_posts')
# ]

from src.views import PostManager
from django.conf.urls import url
urlpatterns = [
    url(r'all', PostManager.as_view(), name='all_posts' )
]