from django.urls import path
from api.auth.views import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView
)

urlpatterns = [
    path('api/token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh'),
]
