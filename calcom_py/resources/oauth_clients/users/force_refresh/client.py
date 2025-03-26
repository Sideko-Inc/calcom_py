import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from calcom_py.types import models


class ForceRefreshClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        client_id: str,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.KeysResponseDto:
        """
        Force refresh tokens

        If you have lost managed user access or refresh token, then you can get new ones by using OAuth credentials.
            Each access token is valid for 60 minutes and each refresh token for 1 year. Make sure to store them later in your database, for example, by updating the User model to have `calAccessToken` and `calRefreshToken` columns.

        POST /v2/oauth-clients/{clientId}/users/{userId}/force-refresh

        Args:
            clientId: str
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.users.force_refresh.create(
            client_id="string", user_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/v2/oauth-clients/{client_id}/users/{user_id}/force-refresh",
            auth_names=["bearerAuth"],
            cast_to=models.KeysResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncForceRefreshClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        client_id: str,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.KeysResponseDto:
        """
        Force refresh tokens

        If you have lost managed user access or refresh token, then you can get new ones by using OAuth credentials.
            Each access token is valid for 60 minutes and each refresh token for 1 year. Make sure to store them later in your database, for example, by updating the User model to have `calAccessToken` and `calRefreshToken` columns.

        POST /v2/oauth-clients/{clientId}/users/{userId}/force-refresh

        Args:
            clientId: str
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.users.force_refresh.create(
            client_id="string", user_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/v2/oauth-clients/{client_id}/users/{user_id}/force-refresh",
            auth_names=["bearerAuth"],
            cast_to=models.KeysResponseDto,
            request_options=request_options or default_request_options(),
        )
