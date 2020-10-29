from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from abcd2.users.models import MNS

class UserView(APIView):

    def post(self, request, *args, **kwargs):

        username = request.data.get("username")
        email = request.data.get("email", "")
        password = request.data.get("password", "admin@123")

        try:
            user = MNS.objects.get(username=username.lower())
        except MNS.DoesNotExist:
            MNS.objects._create_user(username=username, password=password, is_superuser=False, email=email, is_staff=True)
            return Response("User successfully Created", status=status.HTTP_200_OK)
        else:
            return Response("User Already exists", status=status.HTTP_400_BAD_REQUEST)
