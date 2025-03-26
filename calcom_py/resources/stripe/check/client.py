import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from calcom_py.types import models


class CheckClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def check(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.StripCredentialsCheckOutputResponseDto:
        """
        Check stripe connection

        GET /v2/stripe/check

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.stripe.check.check()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v2/stripe/check",
            auth_names=["bearerAuth"],
            cast_to=models.StripCredentialsCheckOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, team_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.StripCredentialsCheckOutputResponseDto:
        """
        Check team stripe connection

        GET /v2/stripe/check/{teamId}

        Args:
            teamId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.stripe.check.get(team_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/stripe/check/{team_id}",
            auth_names=["bearerAuth"],
            cast_to=models.StripCredentialsCheckOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncCheckClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def check(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.StripCredentialsCheckOutputResponseDto:
        """
        Check stripe connection

        GET /v2/stripe/check

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.stripe.check.check()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v2/stripe/check",
            auth_names=["bearerAuth"],
            cast_to=models.StripCredentialsCheckOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, team_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.StripCredentialsCheckOutputResponseDto:
        """
        Check team stripe connection

        GET /v2/stripe/check/{teamId}

        Args:
            teamId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.stripe.check.get(team_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/stripe/check/{team_id}",
            auth_names=["bearerAuth"],
            cast_to=models.StripCredentialsCheckOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
