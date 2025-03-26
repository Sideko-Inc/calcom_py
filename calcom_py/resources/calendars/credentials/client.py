import httpx
import typing
import typing_extensions

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class CredentialsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        calendar_field: typing_extensions.Literal["apple"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Sync credentials

        POST /v2/calendars/{calendar}/credentials

        Args:
            calendar: typing_extensions.Literal["apple"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.calendars.credentials.create(calendar_field="apple")
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/v2/calendars/{calendar_field}/credentials",
            auth_names=["bearerAuth"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncCredentialsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        calendar_field: typing_extensions.Literal["apple"],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Sync credentials

        POST /v2/calendars/{calendar}/credentials

        Args:
            calendar: typing_extensions.Literal["apple"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.calendars.credentials.create(calendar_field="apple")
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/v2/calendars/{calendar_field}/credentials",
            auth_names=["bearerAuth"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )
