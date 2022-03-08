from django.urls import path
from api.auth.views import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
    APILogoutRefreshToken,
    APILogoutAllToken
)
from api.user.views import UserMe

urlpatterns = [
    path('token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', APILogoutRefreshToken.as_view(), name='token_logout_refresh'),
    path('token/logout_all/', APILogoutAllToken.as_view(), name='token_logout_all'),
    path('user/me/', UserMe.as_view(), name='user_me'),
]
