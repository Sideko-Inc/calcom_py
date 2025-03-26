import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from calcom_py.types import models


class DefaultClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDefaultScheduleOutput20240611:
        """
        Get default schedule

        Get the default schedule of the authenticated user.

        GET /v2/schedules/default

        Args:
            cal-api-version: Must be set to 2024-06-11
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.schedules.default.list(cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="GET",
            path="/v2/schedules/default",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetDefaultScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )


class AsyncDefaultClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetDefaultScheduleOutput20240611:
        """
        Get default schedule

        Get the default schedule of the authenticated user.

        GET /v2/schedules/default

        Args:
            cal-api-version: Must be set to 2024-06-11
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.schedules.default.list(cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="GET",
            path="/v2/schedules/default",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetDefaultScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )
