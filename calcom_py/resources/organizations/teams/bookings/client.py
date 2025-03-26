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
from calcom_py.types import models


class BookingsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        org_id: float,
        team_id: float,
        after_start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        attendee_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        attendee_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_end: typing.Union[
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingsOutput20240813:
        """
        Get organization team bookings

        GET /v2/organizations/{orgId}/teams/{teamId}/bookings

        Args:
            afterStart: Filter bookings with start after this date string.
            attendeeEmail: Filter bookings by the attendee's email address.
            attendeeName: Filter bookings by the attendee's name.
            beforeEnd: Filter bookings with end before this date string.
            eventTypeId: Filter bookings by event type id belonging to the team.
            eventTypeIds: Filter bookings by event type ids belonging to the team. Event type ids must be separated by a comma.
            skip: The number of items to skip
            sortCreated: Sort results by their creation time (when booking was made) in ascending or descending order.
            sortEnd: Sort results by their end time in ascending or descending order.
            sortStart: Sort results by their start time in ascending or descending order.
            status: Filter bookings by status. If you want to filter by multiple statuses, separate them with a comma.
            take: The number of items to return
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.bookings.list(org_id=123.0, team_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(after_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "afterStart",
                to_encodable(item=after_start, dump_with=str),
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
        if not isinstance(before_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "beforeEnd",
                to_encodable(item=before_end, dump_with=str),
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
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/bookings",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBookingsOutput20240813,
            request_options=request_options or default_request_options(),
        )


class AsyncBookingsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        org_id: float,
        team_id: float,
        after_start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        attendee_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        attendee_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_end: typing.Union[
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetBookingsOutput20240813:
        """
        Get organization team bookings

        GET /v2/organizations/{orgId}/teams/{teamId}/bookings

        Args:
            afterStart: Filter bookings with start after this date string.
            attendeeEmail: Filter bookings by the attendee's email address.
            attendeeName: Filter bookings by the attendee's name.
            beforeEnd: Filter bookings with end before this date string.
            eventTypeId: Filter bookings by event type id belonging to the team.
            eventTypeIds: Filter bookings by event type ids belonging to the team. Event type ids must be separated by a comma.
            skip: The number of items to skip
            sortCreated: Sort results by their creation time (when booking was made) in ascending or descending order.
            sortEnd: Sort results by their end time in ascending or descending order.
            sortStart: Sort results by their start time in ascending or descending order.
            status: Filter bookings by status. If you want to filter by multiple statuses, separate them with a comma.
            take: The number of items to return
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.bookings.list(org_id=123.0, team_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(after_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "afterStart",
                to_encodable(item=after_start, dump_with=str),
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
        if not isinstance(before_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "beforeEnd",
                to_encodable(item=before_end, dump_with=str),
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
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/bookings",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetBookingsOutput20240813,
            request_options=request_options or default_request_options(),
        )
