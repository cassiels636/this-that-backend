from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from minervatest.decorators import validate_request_data
from .models import This, That
from .serializers import ThisSerializer, ThatSerializer, RandPairingSerializer
from collections import namedtuple


Pairing = namedtuple('Names', ('this_name', 'that_name'))


class ListThisNamesView(generics.ListAPIView):
    queryset = This.objects.all()
    serializer_class = ThisSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        this = This.objects.create(
            name=request.data["name"],
        )
        return Response(
            data=ThisSerializer(this).data,
            status=status.HTTP_201_CREATED
        )


class ListThatNamesView(generics.ListAPIView):
    queryset = That.objects.all()
    serializer_class = ThatSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        that = That.objects.create(
            name=request.data["name"],
        )
        return Response(
            data=ThatSerializer(that).data,
            status=status.HTTP_201_CREATED
        )


class RandomPairingView(viewsets.ViewSet):

    def list(self, request):
        name = Pairing(
            this_name=This.objects.all().order_by('?')[:1].values_list('name', flat=True).first(),
            that_name=That.objects.all().order_by('?')[:1].values_list('name', flat=True).first(),
        )

        serializer = RandPairingSerializer(name)
        return Response(serializer.data)
