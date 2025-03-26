import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class TimezonesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get all timezones

        GET /v2/timezones

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.timezones.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v2/timezones",
            auth_names=["bearerAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )


class AsyncTimezonesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get all timezones

        GET /v2/timezones

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.timezones.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v2/timezones",
            auth_names=["bearerAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
