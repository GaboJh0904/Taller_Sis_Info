# app/services/provider_bl.py
from app.repositories.provider_repository import (
    fetch_provider_by_id, fetch_all_providers, insert_provider, update_provider, delete_provider
)
from app.schemas.provider_schema import ProviderCreate, ProviderOut

class ProviderBL:

    @staticmethod
    def create_new_provider(provider_data: ProviderCreate) -> ProviderOut:
        return insert_provider(provider_data)

    @staticmethod
    def get_provider_by_id(provider_id: int) -> ProviderOut:
        provider = fetch_provider_by_id(provider_id)
        if not provider:
            raise ValueError("Provider not found")
        return provider

    @staticmethod
    def get_all_providers() -> list[ProviderOut]:
        return fetch_all_providers()

    @staticmethod
    def update_existing_provider(provider_id: int, provider_data: ProviderCreate) -> ProviderOut:
        provider = fetch_provider_by_id(provider_id)
        if not provider:
            raise ValueError("Provider not found")
        return update_provider(provider_id, provider_data)

    @staticmethod
    def delete_provider_by_id(provider_id: int) -> None:
        provider = fetch_provider_by_id(provider_id)
        if not provider:
            raise ValueError("Provider not found")
        delete_provider(provider_id)
