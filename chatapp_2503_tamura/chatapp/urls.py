from django.urls import path
from . import views

urlpatterns = [
    # 例えば、チャット関連のURLを追加
    path('', views.index, name='index'),
    # 他のチャットに関連するURLもここに追加
]