from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserSerializer


class UserMe(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: UserSerializer(many=False)
        }
    )
    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data)
