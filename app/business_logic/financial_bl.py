from app.repositories.project_repository import ProjectOut


class FinancialBL:
    @staticmethod
    def get_budget_variance(project_id: int):
        project = ProjectRepository.get_project(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")

        assigned_budget = project.PRESUPUESTO_ASIGNADO

        # Calculate actual spending
        material_allocations = MaterialAllocationRepository.get_allocations_by_project(project_id)
        tool_allocations = ToolAllocationRepository.get_allocations_by_project(project_id)

        total_material_spending = 0
        for allocation in material_allocations:
            material = MaterialRepository.get_material_by_flow_id(allocation.FLUJO_MATERIAL_ID)
            if material:
                total_material_spending += material.PRECIO_UNITARIO * allocation.CANTIDAD

        total_tool_spending = 0
        for allocation in tool_allocations:
            tool = ToolRepository.get_tool_by_flow_id(allocation.FLUJO_HERRAMIENTA_ID)
            if tool:
                total_tool_spending += tool.PRECIO_UNITARIO * allocation.CANTIDAD

        actual_spending = total_material_spending + total_tool_spending

        budget_variance = assigned_budget - actual_spending

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "assigned_budget": assigned_budget,
            "actual_spending": actual_spending,
            "budget_variance": budget_variance
        }
    
    @staticmethod
    def get_spending_trend(project_id: int):
        project = ProjectRepository.get_project(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")

        # Get all allocations with dates
        material_allocations = MaterialAllocationRepository.get_allocations_with_dates_by_project(project_id)
        tool_allocations = ToolAllocationRepository.get_allocations_with_dates_by_project(project_id)

        # Combine allocations
        spending_records = []

        for allocation in material_allocations:
            material = MaterialRepository.get_material_by_flow_id(allocation.FLUJO_MATERIAL_ID)
            if material:
                amount = material.PRECIO_UNITARIO * allocation.CANTIDAD
                spending_records.append({
                    "date": allocation.FECHA,
                    "amount": amount
                })

        for allocation in tool_allocations:
            tool = ToolRepository.get_tool_by_flow_id(allocation.FLUJO_HERRAMIENTA_ID)
            if tool:
                amount = tool.PRECIO_UNITARIO * allocation.CANTIDAD
                spending_records.append({
                    "date": allocation.FECHA,
                    "amount": amount
                })

        # Aggregate spending over time (e.g., monthly)
        spending_over_time = {}
        for record in spending_records:
            date_key = record["date"].strftime("%Y-%m")  # Group by month
            spending_over_time.setdefault(date_key, 0)
            spending_over_time[date_key] += record["amount"]

        # Convert to list of dicts
        spending_over_time_list = [
            {"date": date_key, "amount": amount}
            for date_key, amount in sorted(spending_over_time.items())
        ]

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "spending_over_time": spending_over_time_list
        }

