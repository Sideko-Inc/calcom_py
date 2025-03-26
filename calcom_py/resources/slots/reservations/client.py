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


class ReservationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        cal_api_version: str,
        uid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        DELETE /v2/slots/reservations/{uid}

        Args:
            cal-api-version: Must be set to 2024-09-04
            uid: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.slots.reservations.delete(cal_api_version="string", uid="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/slots/reservations/{uid}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        cal_api_version: str,
        uid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReservedSlotOutput20240904:
        """
        Get reserved slot

        GET /v2/slots/reservations/{uid}

        Args:
            cal-api-version: Must be set to 2024-09-04
            uid: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.slots.reservations.get(cal_api_version="string", uid="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="GET",
            path=f"/v2/slots/reservations/{uid}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetReservedSlotOutput20240904,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        cal_api_version: str,
        event_type_id: float,
        slot_start: str,
        uid: str,
        reservation_duration: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slot_duration: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReserveSlotOutputResponse20240904:
        """
        Updated reserved a slot

        PATCH /v2/slots/reservations/{uid}

        Args:
            reservationDuration: ONLY for authenticated requests with api key, access token or OAuth credentials (ID + secret).

              For how many minutes the slot should be reserved - for this long time noone else can book this event type at `start` time. If not provided, defaults to 5 minutes.
            slotDuration: By default slot duration is equal to event type length, but if you want to reserve a slot for an event type that has a variable length you can specify it here as a number in minutes. If you don't have this set explicitly that event type can have one of many lengths you can omit this.
            cal-api-version: Must be set to 2024-09-04
            eventTypeId: The ID of the event type for which slot should be reserved.
            slotStart: ISO 8601 datestring in UTC timezone representing available slot.
            uid: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.slots.reservations.patch(
            cal_api_version="string",
            event_type_id=1.0,
            slot_start="2024-09-04T09:00:00Z",
            uid="string",
            reservation_duration=5.0,
            slot_duration=123.0,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={
                "reservation_duration": reservation_duration,
                "slot_duration": slot_duration,
                "event_type_id": event_type_id,
                "slot_start": slot_start,
            },
            dump_with=params._SerializerReserveSlotInput20240904,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/slots/reservations/{uid}",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.ReserveSlotOutputResponse20240904,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        cal_api_version: str,
        event_type_id: float,
        slot_start: str,
        reservation_duration: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slot_duration: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReserveSlotOutputResponse20240904:
        """
        Reserve a slot

        Make a slot not available for others to book for a certain period of time.

        POST /v2/slots/reservations

        Args:
            reservationDuration: ONLY for authenticated requests with api key, access token or OAuth credentials (ID + secret).

              For how many minutes the slot should be reserved - for this long time noone else can book this event type at `start` time. If not provided, defaults to 5 minutes.
            slotDuration: By default slot duration is equal to event type length, but if you want to reserve a slot for an event type that has a variable length you can specify it here as a number in minutes. If you don't have this set explicitly that event type can have one of many lengths you can omit this.
            cal-api-version: Must be set to 2024-09-04
            eventTypeId: The ID of the event type for which slot should be reserved.
            slotStart: ISO 8601 datestring in UTC timezone representing available slot.
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.slots.reservations.create(
            cal_api_version="string",
            event_type_id=1.0,
            slot_start="2024-09-04T09:00:00Z",
            reservation_duration=5.0,
            slot_duration=123.0,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={
                "reservation_duration": reservation_duration,
                "slot_duration": slot_duration,
                "event_type_id": event_type_id,
                "slot_start": slot_start,
            },
            dump_with=params._SerializerReserveSlotInput20240904,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/slots/reservations",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.ReserveSlotOutputResponse20240904,
            request_options=request_options or default_request_options(),
        )


class AsyncReservationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        cal_api_version: str,
        uid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        DELETE /v2/slots/reservations/{uid}

        Args:
            cal-api-version: Must be set to 2024-09-04
            uid: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.slots.reservations.delete(cal_api_version="string", uid="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/slots/reservations/{uid}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        cal_api_version: str,
        uid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetReservedSlotOutput20240904:
        """
        Get reserved slot

        GET /v2/slots/reservations/{uid}

        Args:
            cal-api-version: Must be set to 2024-09-04
            uid: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.slots.reservations.get(cal_api_version="string", uid="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="GET",
            path=f"/v2/slots/reservations/{uid}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetReservedSlotOutput20240904,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        cal_api_version: str,
        event_type_id: float,
        slot_start: str,
        uid: str,
        reservation_duration: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slot_duration: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReserveSlotOutputResponse20240904:
        """
        Updated reserved a slot

        PATCH /v2/slots/reservations/{uid}

        Args:
            reservationDuration: ONLY for authenticated requests with api key, access token or OAuth credentials (ID + secret).

              For how many minutes the slot should be reserved - for this long time noone else can book this event type at `start` time. If not provided, defaults to 5 minutes.
            slotDuration: By default slot duration is equal to event type length, but if you want to reserve a slot for an event type that has a variable length you can specify it here as a number in minutes. If you don't have this set explicitly that event type can have one of many lengths you can omit this.
            cal-api-version: Must be set to 2024-09-04
            eventTypeId: The ID of the event type for which slot should be reserved.
            slotStart: ISO 8601 datestring in UTC timezone representing available slot.
            uid: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.slots.reservations.patch(
            cal_api_version="string",
            event_type_id=1.0,
            slot_start="2024-09-04T09:00:00Z",
            uid="string",
            reservation_duration=5.0,
            slot_duration=123.0,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={
                "reservation_duration": reservation_duration,
                "slot_duration": slot_duration,
                "event_type_id": event_type_id,
                "slot_start": slot_start,
            },
            dump_with=params._SerializerReserveSlotInput20240904,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/slots/reservations/{uid}",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.ReserveSlotOutputResponse20240904,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        cal_api_version: str,
        event_type_id: float,
        slot_start: str,
        reservation_duration: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slot_duration: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReserveSlotOutputResponse20240904:
        """
        Reserve a slot

        Make a slot not available for others to book for a certain period of time.

        POST /v2/slots/reservations

        Args:
            reservationDuration: ONLY for authenticated requests with api key, access token or OAuth credentials (ID + secret).

              For how many minutes the slot should be reserved - for this long time noone else can book this event type at `start` time. If not provided, defaults to 5 minutes.
            slotDuration: By default slot duration is equal to event type length, but if you want to reserve a slot for an event type that has a variable length you can specify it here as a number in minutes. If you don't have this set explicitly that event type can have one of many lengths you can omit this.
            cal-api-version: Must be set to 2024-09-04
            eventTypeId: The ID of the event type for which slot should be reserved.
            slotStart: ISO 8601 datestring in UTC timezone representing available slot.
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.slots.reservations.create(
            cal_api_version="string",
            event_type_id=1.0,
            slot_start="2024-09-04T09:00:00Z",
            reservation_duration=5.0,
            slot_duration=123.0,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={
                "reservation_duration": reservation_duration,
                "slot_duration": slot_duration,
                "event_type_id": event_type_id,
                "slot_start": slot_start,
            },
            dump_with=params._SerializerReserveSlotInput20240904,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/slots/reservations",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.ReserveSlotOutputResponse20240904,
            request_options=request_options or default_request_options(),
        )
