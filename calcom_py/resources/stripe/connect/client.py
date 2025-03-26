import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from calcom_py.types import models


class ConnectClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def redirect(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.StripConnectOutputResponseDto:
        """
        Get stripe connect URL

        GET /v2/stripe/connect

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.stripe.connect.redirect()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v2/stripe/connect",
            auth_names=["bearerAuth"],
            cast_to=models.StripConnectOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncConnectClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def redirect(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.StripConnectOutputResponseDto:
        """
        Get stripe connect URL

        GET /v2/stripe/connect

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.stripe.connect.redirect()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v2/stripe/connect",
            auth_names=["bearerAuth"],
            cast_to=models.StripConnectOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
