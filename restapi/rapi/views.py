from django.shortcuts import render
from rest_framework import viewsets
from .serializers import routerSerializer
from .models import router
from url_filter.integrations.drf import DjangoFilterBackend

# Create your views here.


class routerViewSet(viewsets.ModelViewSet):
    queryset = router.objects.all().order_by('sapid')
    serializer_class = routerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['loopback', 'type']
