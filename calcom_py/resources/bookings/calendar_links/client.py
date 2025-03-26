import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from calcom_py.types import models


class CalendarLinksClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CalendarLinksOutput20240813:
        """
        Get 'Add to Calendar' links for a booking

        Retrieve calendar links for a booking that can be used to add the event to various calendar services. Returns links for Google Calendar, Microsoft Office, Microsoft Outlook, and a downloadable ICS file.

        GET /v2/bookings/{bookingUid}/calendar-links

        Args:
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bookings.calendar_links.list(
            booking_uid="string", cal_api_version="string"
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="GET",
            path=f"/v2/bookings/{booking_uid}/calendar-links",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.CalendarLinksOutput20240813,
            request_options=request_options or default_request_options(),
        )


class AsyncCalendarLinksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CalendarLinksOutput20240813:
        """
        Get 'Add to Calendar' links for a booking

        Retrieve calendar links for a booking that can be used to add the event to various calendar services. Returns links for Google Calendar, Microsoft Office, Microsoft Outlook, and a downloadable ICS file.

        GET /v2/bookings/{bookingUid}/calendar-links

        Args:
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bookings.calendar_links.list(
            booking_uid="string", cal_api_version="string"
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="GET",
            path=f"/v2/bookings/{booking_uid}/calendar-links",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.CalendarLinksOutput20240813,
            request_options=request_options or default_request_options(),
        )
