import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from calcom_py.types import models


class ProviderClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ProviderVerifyClientOutput:
        """
        Get a provider

        GET /v2/provider/{clientId}

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.provider.get(client_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/provider/{client_id}",
            auth_names=["bearerAuth"],
            cast_to=models.ProviderVerifyClientOutput,
            request_options=request_options or default_request_options(),
        )

    def verify_token(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ProviderVerifyAccessTokenOutput:
        """
        Verify an access token

        GET /v2/provider/{clientId}/access-token

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.provider.verify_token(client_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/provider/{client_id}/access-token",
            auth_names=["bearerAuth"],
            cast_to=models.ProviderVerifyAccessTokenOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncProviderClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ProviderVerifyClientOutput:
        """
        Get a provider

        GET /v2/provider/{clientId}

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.provider.get(client_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/provider/{client_id}",
            auth_names=["bearerAuth"],
            cast_to=models.ProviderVerifyClientOutput,
            request_options=request_options or default_request_options(),
        )

    async def verify_token(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ProviderVerifyAccessTokenOutput:
        """
        Verify an access token

        GET /v2/provider/{clientId}/access-token

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.provider.verify_token(client_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/provider/{client_id}/access-token",
            auth_names=["bearerAuth"],
            cast_to=models.ProviderVerifyAccessTokenOutput,
            request_options=request_options or default_request_options(),
        )
