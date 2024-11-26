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

    @staticmethod
    def get_spending_trend(project_id: int):
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")

        material_allocations = get_material_allocations_by_project(project_id)
        tool_allocations = get_tool_allocations_by_project(project_id)

        spending_records = []

        for allocation in material_allocations:
            flow_material = get_flow_material_by_id(allocation.FLUJO_MATERIAL_ID)
            material = get_material_by_id(flow_material.MATERIAL_ID)
            if material:
                amount = material.PRECIO_UNITARIO * allocation.CANTIDAD
                date = flow_material.FECHA.date()
                spending_records.append({
                    "date": date,
                    "amount": float(amount)
                })

        for allocation in tool_allocations:
            flow_tool = get_flow_tool_by_id(allocation.FLUJO_HERRAMIENTA_ID)
            tool = get_tool_by_id(flow_tool.HERRAMIENTA_ID)
            if tool:
                amount = tool.PRECIO_UNITARIO * allocation.CANTIDAD
                date = flow_tool.FECHA.date()
                spending_records.append({
                    "date": date,
                    "amount": float(amount)
                })

        # Aggregate spending over time (e.g., daily)
        spending_over_time = defaultdict(float)
        for record in spending_records:
            date_key = record["date"].strftime("%Y-%m-%d")
            spending_over_time[date_key] += record["amount"]

        spending_over_time_list = [
            {"date": date_key, "amount": amount}
            for date_key, amount in sorted(spending_over_time.items())
        ]

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "spending_over_time": spending_over_time_list
        }

    @staticmethod
    def get_expense_breakdown(project_id: int):
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")

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

        total_expense = total_material_spending + total_tool_spending

        expenses = [
            {"category": "Materials", "amount": float(total_material_spending)},
            {"category": "Tools", "amount": float(total_tool_spending)}
        ]

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "expenses": expenses,
            "total_expense": float(total_expense)
        }
