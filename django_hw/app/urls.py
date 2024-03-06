from django.urls import path
from .views import *


urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('create_book/', BookCreate.as_view(), name='create_book'),
    path('detail_book/<int:pk>', BookDetail.as_view(), name='detail_book'),
    path('update_book/<int:pk>', BookUpdate.as_view(), name='update_book'),
    path('delete_book/<int:pk>', BookDelete.as_view(), name='delete_book'),
    # path('create_comment/<int:post_id>', create_comment, name='create_comment'),
    # path('post/<int:post_id>', detail_post, name='detail_post'),
]
