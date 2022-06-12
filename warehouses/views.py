from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from warehouses.serializers.populated import PopulatedWarehouseSerializer
from warehouses.serializers.common import WarehouseSerializer
from .models import Warehouse


# Create your views here

class WarehouseListView(APIView):

    # Get all warehouses from DB
    def get(self, _request):
        warehouses = Warehouse.objects.all()
        serialized_warehouse = PopulatedWarehouseSerializer(
            warehouses, many=True)

        return Response(serialized_warehouse.data, status=status.HTTP_200_OK)

    # Add warehouse to DB
    def post(self, request):
        serialized_data = WarehouseSerializer(data=request.data)

        try:
            serialized_data.is_valid()
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detial": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
