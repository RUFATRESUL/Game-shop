from django.urls import path,include
from . import views


app_name='shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/<str:slug>/', views.product_detail, name='product-detail'),
    path("games/",views.games, name="games"),
    path('games/playstation3/', views.game_list3, name='game-list3'),
    path('games/playstation4/', views.game_list4, name='game-list4'),
    path('games/playstation5/', views.game_list5, name='game-list5'),
    path('games/playstation3/child_games', views.child_game3, name='child_game3'),
    path('games/playstation4/child_games', views.child_game4, name='child_game4'),
    path('games/playstation5/child_games', views.child_game5, name='child_game5'),
    path('review/<int:pk>/', views.review, name='review'),
    path('api/', include('shop.api.urls'))
]
