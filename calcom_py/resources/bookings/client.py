import typing
import typing_extensions

from calcom_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from calcom_py.resources.bookings.calendar_links import (
    AsyncCalendarLinksClient,
    CalendarLinksClient,
)
from calcom_py.types import models, params


class BookingsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.calendar_links = CalendarLinksClient(base_client=self._base_client)

    def list(
        self,
        *,
        cal_api_version: str,
        after_created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        after_start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        after_updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        attendee_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        attendee_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_end: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event_type_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event_type_ids: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sort_created: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        sort_end: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        sort_start: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        sort_updated_at: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal[
                        "cancelled", "past", "recurring", "unconfirmed", "upcoming"
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        team_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        teams_ids: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingsOutput20240813:
        """
        Get all bookings

        GET /v2/bookings

        Args:
            afterCreatedAt: Filter bookings that have been created after this date string.
            afterStart: Filter bookings with start after this date string.
            afterUpdatedAt: Filter bookings that have been updated after this date string.
            attendeeEmail: Filter bookings by the attendee's email address.
            attendeeName: Filter bookings by the attendee's name.
            beforeCreatedAt: Filter bookings that have been created before this date string.
            beforeEnd: Filter bookings with end before this date string.
            beforeUpdatedAt: Filter bookings that have been updated before this date string.
            eventTypeId: Filter bookings by event type id belonging to the user.
            eventTypeIds: Filter bookings by event type ids belonging to the user. Event type ids must be separated by a comma.
            skip: The number of items to skip
            sortCreated: Sort results by their creation time (when booking was made) in ascending or descending order.
            sortEnd: Sort results by their end time in ascending or descending order.
            sortStart: Sort results by their start time in ascending or descending order.
            sortUpdatedAt: Sort results by their updated time (for example when booking status changes) in ascending or descending order.
            status: Filter bookings by status. If you want to filter by multiple statuses, separate them with a comma.
            take: The number of items to return
            teamId: Filter bookings by team id that user is part of
            teamsIds: Filter bookings by team ids that user is part of. Team ids must be separated by a comma.
            cal-api-version: Must be set to 2024-08-13
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bookings.list(cal_api_version="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(after_created_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "afterCreatedAt",
                to_encodable(item=after_created_at, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(after_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "afterStart",
                to_encodable(item=after_start, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(after_updated_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "afterUpdatedAt",
                to_encodable(item=after_updated_at, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(attendee_email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "attendeeEmail",
                to_encodable(item=attendee_email, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(attendee_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "attendeeName",
                to_encodable(item=attendee_name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(before_created_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "beforeCreatedAt",
                to_encodable(item=before_created_at, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(before_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "beforeEnd",
                to_encodable(item=before_end, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(before_updated_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "beforeUpdatedAt",
                to_encodable(item=before_updated_at, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(event_type_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventTypeId",
                to_encodable(item=event_type_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(event_type_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventTypeIds",
                to_encodable(item=event_type_ids, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(skip, type_utils.NotGiven):
            encode_query_param(
                _query,
                "skip",
                to_encodable(item=skip, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(sort_created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortCreated",
                to_encodable(
                    item=sort_created,
                    dump_with=typing_extensions.Literal["asc", "desc"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(sort_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortEnd",
                to_encodable(
                    item=sort_end, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(sort_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortStart",
                to_encodable(
                    item=sort_start, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(sort_updated_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortUpdatedAt",
                to_encodable(
                    item=sort_updated_at,
                    dump_with=typing_extensions.Literal["asc", "desc"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing.List[
                        typing_extensions.Literal[
                            "cancelled", "past", "recurring", "unconfirmed", "upcoming"
                        ]
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(take, type_utils.NotGiven):
            encode_query_param(
                _query,
                "take",
                to_encodable(item=take, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(team_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "teamId",
                to_encodable(item=team_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(teams_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "teamsIds",
                to_encodable(item=teams_ids, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="GET",
            path="/v2/bookings",
            auth_names=["bearerAuth"],
            query_params=_query,
            headers=_header,
            cast_to=models.GetBookingsOutput20240813,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingOutput20240813:
        """
        Get a booking

        `:bookingUid` can be

              1. uid of a normal booking

              2. uid of one of the recurring booking recurrences

              3. uid of recurring booking which will return an array of all recurring booking recurrences (stored as recurringBookingUid on one of the individual recurrences).

        GET /v2/bookings/{bookingUid}

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
        client.bookings.get(booking_uid="string", cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="GET",
            path=f"/v2/bookings/{booking_uid}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        cal_api_version: str,
        data: typing.Union[
            params.CreateBookingInput20240813,
            params.CreateInstantBookingInput20240813,
            params.CreateRecurringBookingInput20240813,
        ],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateBookingOutput20240813:
        """
        Create a booking


              POST /v2/bookings is used to create regular bookings, recurring bookings and instant bookings. The request bodies for all 3 are almost the same except:
              If eventTypeId in the request body is id of a regular event, then regular booking is created.

              If it is an id of a recurring event type, then recurring booking is created.

              Meaning that the request bodies are equal but the outcome depends on what kind of event type it is with the goal of making it as seamless for developers as possible.

              For team event types it is possible to create instant meeting. To do that just pass `"instant": true` to the request body.

              The start needs to be in UTC aka if the timezone is GMT+2 in Rome and meeting should start at 11, then UTC time should have hours 09:00 aka without time zone.


        POST /v2/bookings

        Args:
            cal-api-version: Must be set to 2024-08-13
            data: typing.Union[CreateBookingInput20240813, CreateInstantBookingInput20240813, CreateRecurringBookingInput20240813]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bookings.create(
            cal_api_version="string",
            data={
                "attendee": {"name": "John Doe", "time_zone": "America/New_York"},
                "event_type_id": 123.0,
                "start": "2024-08-13T09:00:00Z",
            },
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item=data,
            dump_with=typing.Union[
                params._SerializerCreateBookingInput20240813,
                params._SerializerCreateInstantBookingInput20240813,
                params._SerializerCreateRecurringBookingInput20240813,
            ],
        )
        return self._base_client.request(
            method="POST",
            path="/v2/bookings",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.CreateBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        data: typing.Union[
            params.CancelBookingInput20240813, params.CancelSeatedBookingInput20240813
        ],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CancelBookingOutput20240813:
        """
        Cancel a booking

        :bookingUid can be :bookingUid of an usual booking, individual recurrence or recurring booking to cancel all recurrences.
            For seated bookings to cancel one individual booking provide :bookingUid and :seatUid in the request body. For recurring seated bookings it is not possible to cancel all of them with 1 call
            like with non-seated recurring bookings by providing recurring bookind uid - you have to cancel each recurrence booking by its bookingUid + seatUid.

        POST /v2/bookings/{bookingUid}/cancel

        Args:
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            data: typing.Union[CancelBookingInput20240813, CancelSeatedBookingInput20240813]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bookings.cancel(booking_uid="string", cal_api_version="string", data={})
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item=data,
            dump_with=typing.Union[
                params._SerializerCancelBookingInput20240813,
                params._SerializerCancelSeatedBookingInput20240813,
            ],
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/cancel",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.CancelBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    def confirm(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingOutput20240813:
        """
        Confirm booking that requires a confirmation

        POST /v2/bookings/{bookingUid}/confirm

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
        client.bookings.confirm(booking_uid="string", cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/confirm",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    def decline(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        reason: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingOutput20240813:
        """
        Decline booking that requires a confirmation

        POST /v2/bookings/{bookingUid}/decline

        Args:
            reason: Reason for declining a booking that requires a confirmation
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bookings.decline(
            booking_uid="string",
            cal_api_version="string",
            reason="Host has to take another call",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={"reason": reason},
            dump_with=params._SerializerDeclineBookingInput20240813,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/decline",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.GetBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    def mark_absent(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        attendees: typing.Union[
            typing.Optional[typing.List[params.Attendee]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        host: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.MarkAbsentBookingOutput20240813:
        """
        Mark a booking absence

        POST /v2/bookings/{bookingUid}/mark-absent

        Args:
            attendees: typing.List[Attendee]
            host: Whether the host was absent
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bookings.mark_absent(
            booking_uid="string", cal_api_version="string", host=False
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={"attendees": attendees, "host": host},
            dump_with=params._SerializerMarkAbsentBookingInput20240813,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/mark-absent",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.MarkAbsentBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    def reassign(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReassignBookingOutput20240813:
        """
        Automatically reassign booking to a new host

        POST /v2/bookings/{bookingUid}/reassign

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
        client.bookings.reassign(booking_uid="string", cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/reassign",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.ReassignBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    def reassign_to_user(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        user_id: float,
        reason: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReassignBookingOutput20240813:
        """
        Reassign a booking to a specific user

        POST /v2/bookings/{bookingUid}/reassign/{userId}

        Args:
            reason: Reason for reassigning the booking
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bookings.reassign_to_user(
            booking_uid="string",
            cal_api_version="string",
            user_id=123.0,
            reason="Host has to take another call",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={"reason": reason},
            dump_with=params._SerializerReassignToUserBookingInput20240813,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/reassign/{user_id}",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.ReassignBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    def reschedule(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        data: typing.Union[
            params.RescheduleBookingInput20240813,
            params.RescheduleSeatedBookingInput20240813,
        ],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RescheduleBookingOutput20240813:
        """
        Reschedule a booking

        Reschedule a booking or seated booking

        POST /v2/bookings/{bookingUid}/reschedule

        Args:
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            data: typing.Union[RescheduleBookingInput20240813, RescheduleSeatedBookingInput20240813]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bookings.reschedule(
            booking_uid="string",
            cal_api_version="string",
            data={"start": "2024-08-13T10:00:00Z"},
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item=data,
            dump_with=typing.Union[
                params._SerializerRescheduleBookingInput20240813,
                params._SerializerRescheduleSeatedBookingInput20240813,
            ],
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/reschedule",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.RescheduleBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )


class AsyncBookingsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.calendar_links = AsyncCalendarLinksClient(base_client=self._base_client)

    async def list(
        self,
        *,
        cal_api_version: str,
        after_created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        after_start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        after_updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        attendee_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        attendee_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_end: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event_type_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event_type_ids: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sort_created: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        sort_end: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        sort_start: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        sort_updated_at: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal[
                        "cancelled", "past", "recurring", "unconfirmed", "upcoming"
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        team_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        teams_ids: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingsOutput20240813:
        """
        Get all bookings

        GET /v2/bookings

        Args:
            afterCreatedAt: Filter bookings that have been created after this date string.
            afterStart: Filter bookings with start after this date string.
            afterUpdatedAt: Filter bookings that have been updated after this date string.
            attendeeEmail: Filter bookings by the attendee's email address.
            attendeeName: Filter bookings by the attendee's name.
            beforeCreatedAt: Filter bookings that have been created before this date string.
            beforeEnd: Filter bookings with end before this date string.
            beforeUpdatedAt: Filter bookings that have been updated before this date string.
            eventTypeId: Filter bookings by event type id belonging to the user.
            eventTypeIds: Filter bookings by event type ids belonging to the user. Event type ids must be separated by a comma.
            skip: The number of items to skip
            sortCreated: Sort results by their creation time (when booking was made) in ascending or descending order.
            sortEnd: Sort results by their end time in ascending or descending order.
            sortStart: Sort results by their start time in ascending or descending order.
            sortUpdatedAt: Sort results by their updated time (for example when booking status changes) in ascending or descending order.
            status: Filter bookings by status. If you want to filter by multiple statuses, separate them with a comma.
            take: The number of items to return
            teamId: Filter bookings by team id that user is part of
            teamsIds: Filter bookings by team ids that user is part of. Team ids must be separated by a comma.
            cal-api-version: Must be set to 2024-08-13
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bookings.list(cal_api_version="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(after_created_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "afterCreatedAt",
                to_encodable(item=after_created_at, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(after_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "afterStart",
                to_encodable(item=after_start, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(after_updated_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "afterUpdatedAt",
                to_encodable(item=after_updated_at, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(attendee_email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "attendeeEmail",
                to_encodable(item=attendee_email, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(attendee_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "attendeeName",
                to_encodable(item=attendee_name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(before_created_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "beforeCreatedAt",
                to_encodable(item=before_created_at, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(before_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "beforeEnd",
                to_encodable(item=before_end, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(before_updated_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "beforeUpdatedAt",
                to_encodable(item=before_updated_at, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(event_type_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventTypeId",
                to_encodable(item=event_type_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(event_type_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventTypeIds",
                to_encodable(item=event_type_ids, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(skip, type_utils.NotGiven):
            encode_query_param(
                _query,
                "skip",
                to_encodable(item=skip, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(sort_created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortCreated",
                to_encodable(
                    item=sort_created,
                    dump_with=typing_extensions.Literal["asc", "desc"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(sort_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortEnd",
                to_encodable(
                    item=sort_end, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(sort_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortStart",
                to_encodable(
                    item=sort_start, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(sort_updated_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sortUpdatedAt",
                to_encodable(
                    item=sort_updated_at,
                    dump_with=typing_extensions.Literal["asc", "desc"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing.List[
                        typing_extensions.Literal[
                            "cancelled", "past", "recurring", "unconfirmed", "upcoming"
                        ]
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(take, type_utils.NotGiven):
            encode_query_param(
                _query,
                "take",
                to_encodable(item=take, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(team_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "teamId",
                to_encodable(item=team_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(teams_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "teamsIds",
                to_encodable(item=teams_ids, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="GET",
            path="/v2/bookings",
            auth_names=["bearerAuth"],
            query_params=_query,
            headers=_header,
            cast_to=models.GetBookingsOutput20240813,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingOutput20240813:
        """
        Get a booking

        `:bookingUid` can be

              1. uid of a normal booking

              2. uid of one of the recurring booking recurrences

              3. uid of recurring booking which will return an array of all recurring booking recurrences (stored as recurringBookingUid on one of the individual recurrences).

        GET /v2/bookings/{bookingUid}

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
        await client.bookings.get(booking_uid="string", cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="GET",
            path=f"/v2/bookings/{booking_uid}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        cal_api_version: str,
        data: typing.Union[
            params.CreateBookingInput20240813,
            params.CreateInstantBookingInput20240813,
            params.CreateRecurringBookingInput20240813,
        ],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateBookingOutput20240813:
        """
        Create a booking


              POST /v2/bookings is used to create regular bookings, recurring bookings and instant bookings. The request bodies for all 3 are almost the same except:
              If eventTypeId in the request body is id of a regular event, then regular booking is created.

              If it is an id of a recurring event type, then recurring booking is created.

              Meaning that the request bodies are equal but the outcome depends on what kind of event type it is with the goal of making it as seamless for developers as possible.

              For team event types it is possible to create instant meeting. To do that just pass `"instant": true` to the request body.

              The start needs to be in UTC aka if the timezone is GMT+2 in Rome and meeting should start at 11, then UTC time should have hours 09:00 aka without time zone.


        POST /v2/bookings

        Args:
            cal-api-version: Must be set to 2024-08-13
            data: typing.Union[CreateBookingInput20240813, CreateInstantBookingInput20240813, CreateRecurringBookingInput20240813]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bookings.create(
            cal_api_version="string",
            data={
                "attendee": {"name": "John Doe", "time_zone": "America/New_York"},
                "event_type_id": 123.0,
                "start": "2024-08-13T09:00:00Z",
            },
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item=data,
            dump_with=typing.Union[
                params._SerializerCreateBookingInput20240813,
                params._SerializerCreateInstantBookingInput20240813,
                params._SerializerCreateRecurringBookingInput20240813,
            ],
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/bookings",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.CreateBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        data: typing.Union[
            params.CancelBookingInput20240813, params.CancelSeatedBookingInput20240813
        ],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CancelBookingOutput20240813:
        """
        Cancel a booking

        :bookingUid can be :bookingUid of an usual booking, individual recurrence or recurring booking to cancel all recurrences.
            For seated bookings to cancel one individual booking provide :bookingUid and :seatUid in the request body. For recurring seated bookings it is not possible to cancel all of them with 1 call
            like with non-seated recurring bookings by providing recurring bookind uid - you have to cancel each recurrence booking by its bookingUid + seatUid.

        POST /v2/bookings/{bookingUid}/cancel

        Args:
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            data: typing.Union[CancelBookingInput20240813, CancelSeatedBookingInput20240813]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bookings.cancel(
            booking_uid="string", cal_api_version="string", data={}
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item=data,
            dump_with=typing.Union[
                params._SerializerCancelBookingInput20240813,
                params._SerializerCancelSeatedBookingInput20240813,
            ],
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/cancel",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.CancelBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    async def confirm(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingOutput20240813:
        """
        Confirm booking that requires a confirmation

        POST /v2/bookings/{bookingUid}/confirm

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
        await client.bookings.confirm(booking_uid="string", cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/confirm",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    async def decline(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        reason: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingOutput20240813:
        """
        Decline booking that requires a confirmation

        POST /v2/bookings/{bookingUid}/decline

        Args:
            reason: Reason for declining a booking that requires a confirmation
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bookings.decline(
            booking_uid="string",
            cal_api_version="string",
            reason="Host has to take another call",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={"reason": reason},
            dump_with=params._SerializerDeclineBookingInput20240813,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/decline",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.GetBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    async def mark_absent(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        attendees: typing.Union[
            typing.Optional[typing.List[params.Attendee]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        host: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.MarkAbsentBookingOutput20240813:
        """
        Mark a booking absence

        POST /v2/bookings/{bookingUid}/mark-absent

        Args:
            attendees: typing.List[Attendee]
            host: Whether the host was absent
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bookings.mark_absent(
            booking_uid="string", cal_api_version="string", host=False
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={"attendees": attendees, "host": host},
            dump_with=params._SerializerMarkAbsentBookingInput20240813,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/mark-absent",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.MarkAbsentBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    async def reassign(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReassignBookingOutput20240813:
        """
        Automatically reassign booking to a new host

        POST /v2/bookings/{bookingUid}/reassign

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
        await client.bookings.reassign(booking_uid="string", cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/reassign",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.ReassignBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    async def reassign_to_user(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        user_id: float,
        reason: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReassignBookingOutput20240813:
        """
        Reassign a booking to a specific user

        POST /v2/bookings/{bookingUid}/reassign/{userId}

        Args:
            reason: Reason for reassigning the booking
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bookings.reassign_to_user(
            booking_uid="string",
            cal_api_version="string",
            user_id=123.0,
            reason="Host has to take another call",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item={"reason": reason},
            dump_with=params._SerializerReassignToUserBookingInput20240813,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/reassign/{user_id}",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.ReassignBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )

    async def reschedule(
        self,
        *,
        booking_uid: str,
        cal_api_version: str,
        data: typing.Union[
            params.RescheduleBookingInput20240813,
            params.RescheduleSeatedBookingInput20240813,
        ],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RescheduleBookingOutput20240813:
        """
        Reschedule a booking

        Reschedule a booking or seated booking

        POST /v2/bookings/{bookingUid}/reschedule

        Args:
            bookingUid: str
            cal-api-version: Must be set to 2024-08-13
            data: typing.Union[RescheduleBookingInput20240813, RescheduleSeatedBookingInput20240813]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bookings.reschedule(
            booking_uid="string",
            cal_api_version="string",
            data={"start": "2024-08-13T10:00:00Z"},
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        _json = to_encodable(
            item=data,
            dump_with=typing.Union[
                params._SerializerRescheduleBookingInput20240813,
                params._SerializerRescheduleSeatedBookingInput20240813,
            ],
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/bookings/{booking_uid}/reschedule",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.RescheduleBookingOutput20240813,
            request_options=request_options or default_request_options(),
        )
