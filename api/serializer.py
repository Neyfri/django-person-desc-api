from rest_framework import serializers
from .models import PersonDesc

class PersonDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDesc
        #fields = ('id', 'name', 'age') ejemplo campos especificos 
        fields = "__all__"  # todos los campos de la clase modelo