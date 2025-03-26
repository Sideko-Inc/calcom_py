from calcom_py.core import AsyncBaseClient, SyncBaseClient
from calcom_py.resources.api_keys.refresh import AsyncRefreshClient, RefreshClient


class ApiKeysClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.refresh = RefreshClient(base_client=self._base_client)


class AsyncApiKeysClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.refresh = AsyncRefreshClient(base_client=self._base_client)
