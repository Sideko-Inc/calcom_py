import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from calcom_py.types import models


class SchedulesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        org_id: float,
        team_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetSchedulesOutput20240611:
        """
        Get schedules of a team member

        GET /v2/organizations/{orgId}/teams/{teamId}/users/{userId}/schedules

        Args:
            orgId: float
            teamId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.users.schedules.list(
            org_id=123.0, team_id=123.0, user_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/users/{user_id}/schedules",
            auth_names=["bearerAuth"],
            cast_to=models.GetSchedulesOutput20240611,
            request_options=request_options or default_request_options(),
        )


class AsyncSchedulesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        org_id: float,
        team_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetSchedulesOutput20240611:
        """
        Get schedules of a team member

        GET /v2/organizations/{orgId}/teams/{teamId}/users/{userId}/schedules

        Args:
            orgId: float
            teamId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.users.schedules.list(
            org_id=123.0, team_id=123.0, user_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/users/{user_id}/schedules",
            auth_names=["bearerAuth"],
            cast_to=models.GetSchedulesOutput20240611,
            request_options=request_options or default_request_options(),
        )
