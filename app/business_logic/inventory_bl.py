# app/business_logic/inventory_bl.py


from app.repositories.material_repository import get_material_by_id
from app.repositories.tool_repository import get_tool_by_id
from app.repositories.flow_material_repository import (
    get_all_flow_materials,
    FlowMaterialRepository
)
from app.repositories.flow_tool_repository import (
    get_all_flow_tools,
    FlowToolRepository
)
from datetime import date, timedelta

class InventoryBL:

    @staticmethod
    def get_stock_levels(item_id: int, item_type: str):
        if item_type == 'material':
            item = get_material_by_id(item_id)
        elif item_type == 'tool':
            item = get_tool_by_id(item_id)

        else:
            raise ValueError("Invalid item type. Must be 'material' or 'tool'.")

        if not item:
            raise ValueError(f"{item_type.capitalize()} with ID {item_id} not found.")

        stock_difference = item.CANTIDAD - item.CANTIDAD_MINIMA
        alert = stock_difference < 0

        return {
            "item_id": item.ID,
            "item_name": item.NOMBRE,
            "current_stock": item.CANTIDAD,
            "minimum_stock": item.CANTIDAD_MINIMA,
            "stock_difference": stock_difference,
            "alert": alert
        }


    @staticmethod
    def get_inventory_turnover_ratio(item_id: int, item_type: str, start_date: date, end_date: date):
        if item_type == 'material':
            flows = FlowMaterialRepository.get_flows_by_item_and_date_range(item_id, start_date, end_date)

            item = get_material_by_id(item_id)
        elif item_type == 'tool':
            flows = FlowToolRepository.get_flows_by_tool_and_date_range(item_id, start_date, end_date)
            item = get_tool_by_id(item_id)

        else:
            raise ValueError("Invalid item type. Must be 'material' or 'tool'.")

        if not item:
            raise ValueError(f"{item_type.capitalize()} with ID {item_id} not found.")

        total_sold = sum(flow.CANTIDAD for flow in flows if flow.MOVIMIENTO == 'salida')
        total_entered = sum(flow.CANTIDAD for flow in flows if flow.MOVIMIENTO == 'entrada')

        beginning_inventory = item.CANTIDAD - total_entered + total_sold
        ending_inventory = item.CANTIDAD
        average_inventory = (beginning_inventory + ending_inventory) / 2

        if average_inventory == 0:
            turnover_ratio = 0
        else:
            turnover_ratio = total_sold / average_inventory

        return {
            "item_id": item.ID,
            "item_name": item.NOMBRE,
            "turnover_ratio": turnover_ratio,
            "total_sold": total_sold,
            "average_inventory": average_inventory,
            "start_date": start_date,
            "end_date": end_date
        }

    @staticmethod
    def get_average_replenishment_time(item_id: int, item_type: str):
        if item_type == 'material':

            flows = get_all_flow_materials()
            flows = [flow for flow in flows if flow.MATERIAL_ID == item_id]
        elif item_type == 'tool':
            flows = get_all_flow_tools()
            flows = [flow for flow in flows if flow.HERRAMIENTA_ID == item_id]

        else:
            raise ValueError("Invalid item type. Must be 'material' or 'tool'.")

        if not flows:
            raise ValueError("No flow records found for the given item.")


        # Filter 'entrada' movements and calculate time differences
        entrada_flows = [flow for flow in flows if flow.MOVIMIENTO == 'entrada']
        if len(entrada_flows) < 2:
            average_replenishment_time = 0
        else:
            entrada_flows.sort(key=lambda x: x.FECHA)
            replenishment_times = []
            for i in range(1, len(entrada_flows)):
                delta = (entrada_flows[i].FECHA - entrada_flows[i - 1].FECHA).days
                replenishment_times.append(delta)
            average_replenishment_time = sum(replenishment_times) / len(replenishment_times)

        item_name = entrada_flows[0].MATERIAL if item_type == 'material' else entrada_flows[0].HERRAMIENTA

        return {
            "item_id": item_id,
            "item_name": item_name,
            "average_replenishment_time": average_replenishment_time,
            "number_of_replenishments": len(entrada_flows)
        }


    @staticmethod
    def get_stockout_rate(item_id: int, item_type: str, start_date: date, end_date: date):
        if item_type == 'material':
            flows = FlowMaterialRepository.get_flows_by_item_and_date_range(item_id, start_date, end_date)

            item = get_material_by_id(item_id)
        elif item_type == 'tool':
            flows = FlowToolRepository.get_flows_by_tool_and_date_range(item_id, start_date, end_date)
            item = get_tool_by_id(item_id)

        else:
            raise ValueError("Invalid item type. Must be 'material' or 'tool'.")

        if not item:
            raise ValueError(f"{item_type.capitalize()} with ID {item_id} not found.")

        # Build daily stock levels

        date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
        stock_levels = {}
        cumulative_stock = item.CANTIDAD

        flows.sort(key=lambda x: x.FECHA)

        for current_date in date_list:
            # Update stock based on flows
            for flow in flows:
                if flow.FECHA.date() == current_date:
                    if flow.MOVIMIENTO == 'entrada':
                        cumulative_stock += flow.CANTIDAD
                    elif flow.MOVIMIENTO == 'salida':
                        cumulative_stock -= flow.CANTIDAD
            stock_levels[current_date] = cumulative_stock

        # Count stockout days
        stockout_days = sum(1 for level in stock_levels.values() if level <= 0)
        total_days = len(date_list)


        stockout_rate = (stockout_days / total_days) * 100

        return {
            "item_id": item.ID,
            "item_name": item.NOMBRE,
            "stockout_rate": stockout_rate,
            "stockout_days": stockout_days,
            "total_days": total_days,
            "start_date": start_date,
            "end_date": end_date

        }

