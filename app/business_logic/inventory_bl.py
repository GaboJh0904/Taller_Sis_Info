# app/business_logic/inventory_bl.py

from app.repositories.material_repository import MaterialRepository
from app.repositories.tool_repository import ToolRepository

from datetime import date
from app.repositories.flow_material_repository import FlowMaterialRepository
from app.repositories.flow_tool_repository import FlowToolRepository


class InventoryBL:


    @staticmethod
    def get_stock_levels(item_id: int, item_type: str):
        if item_type == 'material':
            item = MaterialRepository.get_material(item_id)
        elif item_type == 'tool':
            item = ToolRepository.get_tool(item_id)
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
            item = MaterialRepository.get_material(item_id)
        elif item_type == 'tool':
            flows = FlowToolRepository.get_flows_by_item_and_date_range(item_id, start_date, end_date)
            item = ToolRepository.get_tool(item_id)
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
            flows = FlowMaterialRepository.get_flows_by_item(item_id)
        elif item_type == 'tool':
            flows = FlowToolRepository.get_flows_by_item(item_id)
        else:
            raise ValueError("Invalid item type. Must be 'material' or 'tool'.")

        if not flows:
            raise ValueError("No flow records found for the given item.")

        # Sort flows by date
        flows.sort(key=lambda x: x.FECHA)

        replenishment_times = []
        last_replenishment_date = None

        for flow in flows:
            if flow.MOVIMIENTO == 'entrada':
                if last_replenishment_date:
                    delta = (flow.FECHA - last_replenishment_date).days
                    replenishment_times.append(delta)
                last_replenishment_date = flow.FECHA

        if not replenishment_times:
            average_replenishment_time = 0
        else:
            average_replenishment_time = sum(replenishment_times) / len(replenishment_times)

        return {
            "item_id": item_id,
            "item_name": flows[0].item_name,  # Assuming item_name is available
            "average_replenishment_time": average_replenishment_time,
            "number_of_replenishments": len(replenishment_times)
        }
    

    @staticmethod
    def get_stockout_rate(item_id: int, item_type: str, start_date: date, end_date: date):
        if item_type == 'material':
            flows = FlowMaterialRepository.get_flows_by_item_and_date_range(item_id, start_date, end_date)
            item = MaterialRepository.get_material(item_id)
        elif item_type == 'tool':
            flows = FlowToolRepository.get_flows_by_item_and_date_range(item_id, start_date, end_date)
            item = ToolRepository.get_tool(item_id)
        else:
            raise ValueError("Invalid item type. Must be 'material' or 'tool'.")

        if not item:
            raise ValueError(f"{item_type.capitalize()} with ID {item_id} not found.")

        # Build daily stock levels
        date_range = (end_date - start_date).days + 1
        stock_levels = [0] * date_range  # Initialize stock levels to zero

        # Assume we have a function to get initial stock level at start_date
        initial_stock = item.CANTIDAD  # Simplified assumption
        stock_levels[0] = initial_stock

        # Update stock levels based on flows
        for flow in flows:
            index = (flow.FECHA.date() - start_date).days
            if flow.MOVIMIENTO == 'entrada':
                stock_levels[index] += flow.CANTIDAD
            elif flow.MOVIMIENTO == 'salida':
                stock_levels[index] -= flow.CANTIDAD

        # Calculate cumulative stock levels
        for i in range(1, date_range):
            stock_levels[i] += stock_levels[i - 1]

        # Count stockout days
        stockout_days = sum(1 for level in stock_levels if level <= 0)
        total_days = date_range

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