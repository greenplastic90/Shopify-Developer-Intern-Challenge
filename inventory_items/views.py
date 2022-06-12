from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from inventory_items.serializers.common import InventoryItemSerializer
from .models import InventoryItem


# Create your views here.


class InventoryItemListView(APIView):

    # Get all inventory items from DB
    def get(self, _request):
        inventory_items = InventoryItem.objects.all()
        serialized_inventory_items = InventoryItemSerializer(
            inventory_items, many=True)

        return Response(serialized_inventory_items.data, status=status.HTTP_200_OK)

    # Add inventory item to DB
    def post(self, request):
        serialized_data = InventoryItemSerializer(data=request.data)

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


class InventoryItemDetailView(APIView):

    # Helper function that gets one inventory item
    def get_inventory_item(self, pk):
        try:
            return InventoryItem.objects.get(pk=pk)

        except InventoryItem.DoesNotExist:
            raise NotFound(detail="Item Not Found")

    # Delete one inventory item by its id

    def delete(self, _request, pk):
        inventory_item = self.get_inventory_item(pk=pk)

        inventory_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    # Update one inventory item by its id

    def put(self, request, pk):
        inventory_item_to_update = self.get_inventory_item(pk=pk)
        serialized_inventory_item = InventoryItemSerializer(
            inventory_item_to_update, data=request.data)

        try:
            serialized_inventory_item.is_valid()
            serialized_inventory_item.save()
            return Response(serialized_inventory_item.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response("Unprocessable Entity", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
