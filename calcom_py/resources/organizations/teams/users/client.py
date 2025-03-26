from calcom_py.core import AsyncBaseClient, SyncBaseClient
from calcom_py.resources.organizations.teams.users.schedules import (
    AsyncSchedulesClient,
    SchedulesClient,
)


class UsersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.schedules = SchedulesClient(base_client=self._base_client)


class AsyncUsersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.schedules = AsyncSchedulesClient(base_client=self._base_client)
