import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from calcom_py.types import models, params


class IcsFeedClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def check(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Check an ICS feed

        GET /v2/calendars/ics-feed/check

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.calendars.ics_feed.check()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v2/calendars/ics-feed/check",
            auth_names=["bearerAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    def save(
        self,
        *,
        urls: typing.List[str],
        read_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateIcsFeedOutputResponseDto:
        """
        Save an ICS feed

        POST /v2/calendars/ics-feed/save

        Args:
            readOnly: Whether to allowing writing to the calendar or not
            urls: An array of ICS URLs
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.calendars.ics_feed.save(
            urls=["https://cal.com/ics/feed.ics", "http://cal.com/ics/feed.ics"],
            read_only=False,
        )
        ```
        """
        _json = to_encodable(
            item={"read_only": read_only, "urls": urls},
            dump_with=params._SerializerCreateIcsFeedInputDto,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/calendars/ics-feed/save",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateIcsFeedOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncIcsFeedClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def check(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Check an ICS feed

        GET /v2/calendars/ics-feed/check

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.calendars.ics_feed.check()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v2/calendars/ics-feed/check",
            auth_names=["bearerAuth"],
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    async def save(
        self,
        *,
        urls: typing.List[str],
        read_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateIcsFeedOutputResponseDto:
        """
        Save an ICS feed

        POST /v2/calendars/ics-feed/save

        Args:
            readOnly: Whether to allowing writing to the calendar or not
            urls: An array of ICS URLs
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.calendars.ics_feed.save(
            urls=["https://cal.com/ics/feed.ics", "http://cal.com/ics/feed.ics"],
            read_only=False,
        )
        ```
        """
        _json = to_encodable(
            item={"read_only": read_only, "urls": urls},
            dump_with=params._SerializerCreateIcsFeedInputDto,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/calendars/ics-feed/save",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateIcsFeedOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
