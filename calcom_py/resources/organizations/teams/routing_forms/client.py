from calcom_py.core import AsyncBaseClient, SyncBaseClient
from calcom_py.resources.organizations.teams.routing_forms.responses import (
    AsyncResponsesClient,
    ResponsesClient,
)


class RoutingFormsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.responses = ResponsesClient(base_client=self._base_client)


class AsyncRoutingFormsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.responses = AsyncResponsesClient(base_client=self._base_client)
