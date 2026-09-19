from rest_framework import generics
from rest_framework.response import Response
from apps.user.permissions import IsStudent, IsAdminOrStudent, IsMine, IsMineOrAdmin
from .models import Problem
from .serializers import ProblemSerializer

class ProblemListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProblemSerializer

    def get_queryset(self):
        if self.request.user.role == "STUDENT":
            return Problem.objects.filter(user=self.request.user)
        return Problem.objects.all()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsStudent()]
        return [IsAdminOrStudent()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=201)

class ProblemDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [IsMineOrAdmin]