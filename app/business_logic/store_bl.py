from app.repositories.store_repository import (
    create_almacen,
    get_almacen_by_id,
    get_all_almacenes,
    update_almacen,
    delete_almacen
)
from app.schemas.store_schema import AlmacenCreate, AlmacenOut


class StoreBL:

    @staticmethod
    def create_new_store(store_data: AlmacenCreate) -> AlmacenOut:
        if not store_data.UBICACION.strip():
            raise ValueError("La ubicación del almacén no puede estar vacía")

        # Crear el almacén en la base de datos
        return create_almacen(store_data)

    @staticmethod
    def get_store_by_id(store_id: int) -> AlmacenOut:
        store = get_almacen_by_id(store_id)
        if not store:
            raise ValueError("El almacén no fue encontrado")
        return store

    @staticmethod
    def get_all_stores() -> list[AlmacenOut]:
        # Obtener todos los almacenes
        return get_all_almacenes()

    @staticmethod
    def update_existing_store(store_id: int, store_data: AlmacenCreate) -> AlmacenOut:
        # Validar que el almacén exista antes de actualizar
        existing_store = get_almacen_by_id(store_id)
        if not existing_store:
            raise ValueError("El almacén no fue encontrado para actualizar")
        
        # Actualizar los datos del almacén
        return update_almacen(store_id, store_data)

    @staticmethod
    def delete_store(store_id: int) -> None:
        existing_store = get_almacen_by_id(store_id)
        if not existing_store:
            raise ValueError("El almacén no fue encontrado para eliminar")
        
        # Eliminar el almacén
        delete_almacen(store_id)
