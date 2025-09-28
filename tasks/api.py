from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer
    
    @action(detail=True, methods=['post'])
    def done(self, request, pk=None):
        task = self.get_object()
        task.done = True
        task.save()
        return Response({'status': 'task marked as done'}, status=status.HTTP_200_OK)