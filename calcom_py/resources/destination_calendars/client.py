import typing
import typing_extensions

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from calcom_py.types import models, params


class DestinationCalendarsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def update(
        self,
        *,
        external_id: str,
        integration: typing_extensions.Literal[
            "apple_calendar", "google_calendar", "office365_calendar"
        ],
        delegation_credential_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DestinationCalendarsOutputResponseDto:
        """
        Update destination calendars

        PUT /v2/destination-calendars

        Args:
            delegationCredentialId: str
            externalId: Unique identifier used to represent the specific calendar, as returned by the /calendars endpoint
            integration: The calendar service you want to integrate, as returned by the /calendars endpoint
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.destination_calendars.update(
            external_id="https://caldav.icloud.com/26962146906/calendars/1644422A-1945-4438-BBC0-4F0Q23A57R7S/",
            integration="apple_calendar",
        )
        ```
        """
        _json = to_encodable(
            item={
                "delegation_credential_id": delegation_credential_id,
                "external_id": external_id,
                "integration": integration,
            },
            dump_with=params._SerializerDestinationCalendarsInputBodyDto,
        )
        return self._base_client.request(
            method="PUT",
            path="/v2/destination-calendars",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.DestinationCalendarsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncDestinationCalendarsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def update(
        self,
        *,
        external_id: str,
        integration: typing_extensions.Literal[
            "apple_calendar", "google_calendar", "office365_calendar"
        ],
        delegation_credential_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DestinationCalendarsOutputResponseDto:
        """
        Update destination calendars

        PUT /v2/destination-calendars

        Args:
            delegationCredentialId: str
            externalId: Unique identifier used to represent the specific calendar, as returned by the /calendars endpoint
            integration: The calendar service you want to integrate, as returned by the /calendars endpoint
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.destination_calendars.update(
            external_id="https://caldav.icloud.com/26962146906/calendars/1644422A-1945-4438-BBC0-4F0Q23A57R7S/",
            integration="apple_calendar",
        )
        ```
        """
        _json = to_encodable(
            item={
                "delegation_credential_id": delegation_credential_id,
                "external_id": external_id,
                "integration": integration,
            },
            dump_with=params._SerializerDestinationCalendarsInputBodyDto,
        )
        return await self._base_client.request(
            method="PUT",
            path="/v2/destination-calendars",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.DestinationCalendarsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
