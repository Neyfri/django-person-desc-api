from rest_framework import viewsets
from .serializer import PersonDescSerializer
from  .models import PersonDesc

# Create your views here.

class PersonDescViewSet(viewsets.ModelViewSet):
    queryset = PersonDesc.objects.all()
    serializer_class = PersonDescSerializer