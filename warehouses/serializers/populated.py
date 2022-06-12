from .common import WarehouseSerializer
from inventory_items.serializers.common import InventoryItemSerializer


class PopulatedWarehouseSerializer(WarehouseSerializer):
    inventory_items = InventoryItemSerializer(many=True)
