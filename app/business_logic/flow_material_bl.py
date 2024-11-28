# app/services/flow_material_bl.py
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPException
from app.repositories.flow_material_repository import (
    create_flow_material, get_flow_material_by_id, get_all_flow_materials, update_flow_material, delete_flow_material, get_encargado_almacen
)
from app.repositories.material_repository import get_material_by_id, update_material_quantity
from app.schemas.flow_material_schema import FlowMaterialCreate, FlowMaterialOut
from app.core.config import settings  # Actualización de la importación

class FlowMaterialBL:

    @staticmethod
    def create_new_flow_material(flow_material_data: FlowMaterialCreate) -> FlowMaterialOut:
        # 1. Obtener el material asociado al MATERIAL_ID
        material = get_material_by_id(flow_material_data.MATERIAL_ID)
        if not material:
            raise ValueError("Material not found")

        # 2. Actualizar la cantidad de material según el tipo de movimiento
        if flow_material_data.MOVIMIENTO == "entrada":
            new_quantity = material.CANTIDAD + flow_material_data.CANTIDAD
        elif flow_material_data.MOVIMIENTO == "salida":
            if material.CANTIDAD < flow_material_data.CANTIDAD:
                raise ValueError("Insufficient material quantity for the requested output")
            new_quantity = material.CANTIDAD - flow_material_data.CANTIDAD
            if material.CANTIDAD_MINIMA > new_quantity:
                # Obtener el correo del encargado de almacen
                almacen_id = flow_material_data.ALMACEN_ID
                email_encargado = get_encargado_almacen(almacen_id)
                # Enviar un correo al encargado de almacen
                FlowMaterialBL.send_email(
                    email_encargado["CORREO"], 
                    "Alerta de cantidad mínima de material", 
                    f"La cantidad del material {material.NOMBRE} ha caído por debajo de la cantidad mínima de {material.CANTIDAD_MINIMA}. Actualmente hay {new_quantity} unidades en el almacén. Se recomienda realizar un pedido de reabastecimiento."
                )
        else:
            raise ValueError("Invalid movement type")

        # 3. Actualizar la cantidad en la tabla MATERIAL

        update_material_quantity(flow_material_data.MATERIAL_ID, new_quantity)
        
        return create_flow_material(flow_material_data)


    @staticmethod
    def get_flow_material(flow_material_id: int) -> FlowMaterialOut:
        flow_material = get_flow_material_by_id(flow_material_id)
        if not flow_material:
            raise ValueError("Flow material not found")
        return flow_material

    @staticmethod
    def get_all_flow_materials() -> list[FlowMaterialOut]:
        return get_all_flow_materials()

    @staticmethod
    def update_existing_flow_material(flow_material_id: int, flow_material_data: FlowMaterialCreate) -> FlowMaterialOut:
        flow_material = get_flow_material_by_id(flow_material_id)
        if not flow_material:
            raise ValueError("Flow material not found")
        return update_flow_material(flow_material_id, flow_material_data)

    @staticmethod
    def delete_flow_material(flow_material_id: int) -> None:
        flow_material = get_flow_material_by_id(flow_material_id)
        if not flow_material:
            raise ValueError("Flow material not found")
        delete_flow_material(flow_material_id)
        
    @staticmethod
    def get_email_encargado_almacen() -> str:
        encargado = get_encargado_almacen()
        if not encargado or not encargado.EMAIL:
            raise ValueError("No email found for the encargado de almacen")
        return encargado.EMAIL

    @staticmethod
    def send_email(to_address: str, subject: str, body: str):
        from_address = settings.EMAIL_FROM
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_address
        msg['To'] = to_address

        try:
            with SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
                server.starttls()  # Inicia TLS
                server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
                server.sendmail(from_address, [to_address], msg.as_string())
        except SMTPException as e:
            raise ValueError(f"Failed to send email: {e}")
