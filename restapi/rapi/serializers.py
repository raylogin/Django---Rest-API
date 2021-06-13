from rest_framework import serializers
from .models import router


class routerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = router
        fields = ('id', 'sapid', 'hostname', 'loopback', 'type')

