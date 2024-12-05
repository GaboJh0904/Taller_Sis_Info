# app/business_logic/financial_bl.py

from app.repositories.project_repository import get_project_by_id
from app.repositories.material_allocation_repository import get_material_allocations_by_project
from app.repositories.tool_allocation_repository import get_tool_allocations_by_project
from app.repositories.material_repository import get_material_by_id
from app.repositories.tool_repository import get_tool_by_id
from app.repositories.flow_material_repository import get_flow_material_by_id
from app.repositories.flow_tool_repository import get_flow_tool_by_id
from collections import defaultdict

class FinancialBL:

    @staticmethod
    def get_budget_variance(project_id: int):
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")

        assigned_budget = project.PRESUPUESTO_ASIGNADO

        # Calculate actual spending
        material_allocations = get_material_allocations_by_project(project_id)
        tool_allocations = get_tool_allocations_by_project(project_id)

        total_material_spending = 0
        for allocation in material_allocations:
            flow_material = get_flow_material_by_id(allocation.FLUJO_MATERIAL_ID)
            material = get_material_by_id(flow_material.MATERIAL_ID)
            if material:
                total_material_spending += material.PRECIO_UNITARIO * allocation.CANTIDAD

        total_tool_spending = 0
        for allocation in tool_allocations:
            flow_tool = get_flow_tool_by_id(allocation.FLUJO_HERRAMIENTA_ID)
            tool = get_tool_by_id(flow_tool.HERRAMIENTA_ID)
            if tool:
                total_tool_spending += tool.PRECIO_UNITARIO * allocation.CANTIDAD

        actual_spending = total_material_spending + total_tool_spending

        budget_variance = assigned_budget - actual_spending

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "assigned_budget": float(assigned_budget),
            "actual_spending": float(actual_spending),
            "budget_variance": float(budget_variance)
        }

    from collections import defaultdict

    @staticmethod
    def get_spending_trend(project_id: int, fase: str = None):
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")

        material_allocations = get_material_allocations_by_project(project_id, fase)
        tool_allocations = get_tool_allocations_by_project(project_id, fase)

        spending_over_time = defaultdict(float)

        for allocation in material_allocations:
            flow_material = get_flow_material_by_id(allocation.FLUJO_MATERIAL_ID)
            if not flow_material:
                continue  
            material = get_material_by_id(flow_material.MATERIAL_ID)
            if material:
                amount = material.PRECIO_UNITARIO * allocation.CANTIDAD
                date_key = flow_material.FECHA.strftime("%Y-%m-%d")
                spending_over_time[date_key] += float(amount)

        for allocation in tool_allocations:
            flow_tool = get_flow_tool_by_id(allocation.FLUJO_HERRAMIENTA_ID)
            if not flow_tool:
                continue 
            tool = get_tool_by_id(flow_tool.HERRAMIENTA_ID)
            if tool:
                amount = tool.PRECIO_UNITARIO * allocation.CANTIDAD
                date_key = flow_tool.FECHA.strftime("%Y-%m-%d")
                spending_over_time[date_key] += float(amount)

        spending_over_time_list = [
            {"date": date, "amount": amount}
            for date, amount in sorted(spending_over_time.items())
        ]

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "spending_over_time": spending_over_time_list
        }

    @staticmethod
    def get_material_spending(project_id: int):
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")


        material_allocations = get_material_allocations_by_project(project_id)

        material_spending = defaultdict(float)


        total = 0


        for allocation in material_allocations:
            flow_material = get_flow_material_by_id(allocation.FLUJO_MATERIAL_ID)
            if not flow_material:
                continue 
            material = get_material_by_id(flow_material.MATERIAL_ID)
            if material:
                amount = material.PRECIO_UNITARIO * allocation.CANTIDAD
                material_name = material.NOMBRE  
                material_spending[material_name] += float(amount)
                total +=  float(amount)

        material_spending_list = [
            {"category": material, "total_spent": amount}
            for material, amount in sorted(material_spending.items())
        ]

        print(material_spending_list)

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "expenses": material_spending_list,
            "total_expense": total
        }


    @staticmethod
    def get_tool_spending(project_id: int):
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")

        tool_allocations = get_tool_allocations_by_project(project_id)

        tool_spending = defaultdict(float)

        total = 0

        for allocation in tool_allocations:
            flow_tool = get_flow_tool_by_id(allocation.FLUJO_HERRAMIENTA_ID)
            if not flow_tool:
                continue  
            tool = get_tool_by_id(flow_tool.HERRAMIENTA_ID)
            if tool:
                amount = tool.PRECIO_UNITARIO * allocation.CANTIDAD
                tool_name = tool.NOMBRE  
                tool_spending[tool_name] += float(amount)
                total += float(amount)

        tool_spending_list = [
            {"category": tool, "total_spent": amount}
            for tool, amount in sorted(tool_spending.items())
        ]

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "expenses": tool_spending_list,
            "total_expense": total
        }