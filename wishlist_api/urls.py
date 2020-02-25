from django.contrib import admin
from django.urls import path
from items import views
from api import views as apiviews
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('items/list/', views.item_list, name='item-list'),
    path('items/detail/<int:item_id>/', views.item_detail, name='item-detail'),
    path('items/wishlist/', views.wishlist, name='wishlist' ),

    path('user/register/', views.user_register, name='user-register'),
    path('user/login/', views.user_login, name='user-login'),
    path('user/logout/', views.user_logout, name='user-logout'),

    path('items/<int:item_id>/favorite/', views.item_favorite, name='item-favorite'),

    path('api/login/', TokenObtainPairView.as_view(), name="api-login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('api/register/', apiviews.Register.as_view(), name="api-register"),

    path('api/items/list', apiviews.ItemListView.as_view(), name='api-list'),
    path('api/items/detail/<int:item_id>/', apiviews.ItemDetailView.as_view(), name='api-detail'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
