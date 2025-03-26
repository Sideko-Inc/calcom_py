import typing

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
from calcom_py.resources.slots.reservations import (
    AsyncReservationsClient,
    ReservationsClient,
)
from calcom_py.types import models


class SlotsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.reservations = ReservationsClient(base_client=self._base_client)

    def list(
        self,
        *,
        cal_api_version: str,
        end: typing.Any,
        start: typing.Any,
        duration: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event_type_id: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event_type_slug: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slot_format: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_zone: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        usernames: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.SlotsListResponseObj0, models.SlotsListResponseObj1]:
        """
        Find out when is an event type ready to be booked.


              There are 4 ways to get available slots:

              1. By event type id. Event type id can be of user and team event types. Example '/v2/slots?eventTypeId=10&start=2050-09-05&end=2050-09-06&timeZone=Europe/Rome'

              2. By event type slug + username. Example '/v2/slots?eventTypeSlug=intro&username=bob&start=2050-09-05&end=2050-09-06'

              3. By event type slug + username + organization slug when searching within an organization. Example '/v2/slots?organizationSlug=org-slug&eventTypeSlug=intro&username=bob&start=2050-09-05&end=2050-09-06'

              4. By usernames only (used for dynamic event type - there is no specific event but you want to know when 2 or more people are available). Example '/v2/slots?usernames=alice,bob&username=bob&organizationSlug=org-slug&start=2050-09-05&end=2050-09-06'. As you see you also need to provide the slug of the organization to which each user in the 'usernames' array belongs.

              All of them require "start" and "end" query parameters which define the time range for which available slots should be checked.
              Optional parameters are:
              - timeZone: Time zone in which the available slots should be returned. Defaults to UTC.
              - duration: Only use for event types that allow multiple durations or for dynamic event types. If not passed for multiple duration event types defaults to default duration. For dynamic event types defaults to 30 aka each returned slot is 30 minutes long. So duration=60 means that returned slots will be each 60 minutes long.
              - slotFormat: Format of the slots. By default return is an object where each key is date and value is array of slots as string. If you want to get start and end of each slot use "range" as value.


        GET /v2/slots

        Args:
            duration: If event type has multiple possible durations then you can specify the desired duration here. Also, if you are fetching slots for a dynamic event then you can specify the duration her which defaults to 30, meaning that returned slots will be each 30 minutes long.
            eventTypeId: The ID of the event type for which available slots should be checked.
            eventTypeSlug: The slug of the event type for which available slots should be checked. If slug is provided then username must be provided too.
            slotFormat: Format of slot times in response. Use 'range' to get start and end times. Use 'time' or omit this query parameter to get only start time.
            timeZone: Time zone in which the available slots should be returned. Defaults to UTC.
            username: The username of the user to get event types for.
            usernames: The usernames for which available slots should be checked separated by a comma.

            Checking slots by usernames is used mainly for dynamic events where there is no specific event but we just want to know when 2 or more people are available.

            Must contain at least 2 usernames.
            cal-api-version: Must be set to 2024-09-04
            end:
            Time until which available slots should be checked.

            Must be in UTC timezone as ISO 8601 datestring.

            You can pass date without hours which defaults to end of day or specify hours:
            2024-08-20 (will have hours 23:59:59 aka at the very end of the date) or you can specify hours manually like 2024-08-20T18:00:00Z.
            start:
              Time starting from which available slots should be checked.

              Must be in UTC timezone as ISO 8601 datestring.

              You can pass date without hours which defaults to start of day or specify hours:
              2024-08-13 (will have hours 00:00:00 aka at very beginning of the date) or you can specify hours manually like 2024-08-13T09:00:00Z.
            request_options: Additional options to customize the HTTP request

        Returns:
            A map of available slots indexed by date, where each date is associated with an array of time slots. If format=range is specified, each slot will be an object with start and end properties denoting start and end of the slot.
              For seated slots each object will have attendeesCount and bookingUid properties.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.slots.list(
            cal_api_version="string", end="could be anything", start="could be anything"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "end",
            to_encodable(item=end, dump_with=typing.Any),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "start",
            to_encodable(item=start, dump_with=typing.Any),
            style="form",
            explode=True,
        )
        if not isinstance(duration, type_utils.NotGiven):
            encode_query_param(
                _query,
                "duration",
                to_encodable(item=duration, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(event_type_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventTypeId",
                to_encodable(item=event_type_id, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(event_type_slug, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventTypeSlug",
                to_encodable(item=event_type_slug, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(slot_format, type_utils.NotGiven):
            encode_query_param(
                _query,
                "slotFormat",
                to_encodable(item=slot_format, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(time_zone, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeZone",
                to_encodable(item=time_zone, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(username, type_utils.NotGiven):
            encode_query_param(
                _query,
                "username",
                to_encodable(item=username, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(usernames, type_utils.NotGiven):
            encode_query_param(
                _query,
                "usernames",
                to_encodable(item=usernames, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="GET",
            path="/v2/slots",
            auth_names=["bearerAuth"],
            query_params=_query,
            headers=_header,
            cast_to=typing.Union[
                models.SlotsListResponseObj0, models.SlotsListResponseObj1
            ],
            request_options=request_options or default_request_options(),
        )


class AsyncSlotsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.reservations = AsyncReservationsClient(base_client=self._base_client)

    async def list(
        self,
        *,
        cal_api_version: str,
        end: typing.Any,
        start: typing.Any,
        duration: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event_type_id: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        event_type_slug: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slot_format: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_zone: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        usernames: typing.Union[
            typing.Optional[typing.Any], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.SlotsListResponseObj0, models.SlotsListResponseObj1]:
        """
        Find out when is an event type ready to be booked.


              There are 4 ways to get available slots:

              1. By event type id. Event type id can be of user and team event types. Example '/v2/slots?eventTypeId=10&start=2050-09-05&end=2050-09-06&timeZone=Europe/Rome'

              2. By event type slug + username. Example '/v2/slots?eventTypeSlug=intro&username=bob&start=2050-09-05&end=2050-09-06'

              3. By event type slug + username + organization slug when searching within an organization. Example '/v2/slots?organizationSlug=org-slug&eventTypeSlug=intro&username=bob&start=2050-09-05&end=2050-09-06'

              4. By usernames only (used for dynamic event type - there is no specific event but you want to know when 2 or more people are available). Example '/v2/slots?usernames=alice,bob&username=bob&organizationSlug=org-slug&start=2050-09-05&end=2050-09-06'. As you see you also need to provide the slug of the organization to which each user in the 'usernames' array belongs.

              All of them require "start" and "end" query parameters which define the time range for which available slots should be checked.
              Optional parameters are:
              - timeZone: Time zone in which the available slots should be returned. Defaults to UTC.
              - duration: Only use for event types that allow multiple durations or for dynamic event types. If not passed for multiple duration event types defaults to default duration. For dynamic event types defaults to 30 aka each returned slot is 30 minutes long. So duration=60 means that returned slots will be each 60 minutes long.
              - slotFormat: Format of the slots. By default return is an object where each key is date and value is array of slots as string. If you want to get start and end of each slot use "range" as value.


        GET /v2/slots

        Args:
            duration: If event type has multiple possible durations then you can specify the desired duration here. Also, if you are fetching slots for a dynamic event then you can specify the duration her which defaults to 30, meaning that returned slots will be each 30 minutes long.
            eventTypeId: The ID of the event type for which available slots should be checked.
            eventTypeSlug: The slug of the event type for which available slots should be checked. If slug is provided then username must be provided too.
            slotFormat: Format of slot times in response. Use 'range' to get start and end times. Use 'time' or omit this query parameter to get only start time.
            timeZone: Time zone in which the available slots should be returned. Defaults to UTC.
            username: The username of the user to get event types for.
            usernames: The usernames for which available slots should be checked separated by a comma.

            Checking slots by usernames is used mainly for dynamic events where there is no specific event but we just want to know when 2 or more people are available.

            Must contain at least 2 usernames.
            cal-api-version: Must be set to 2024-09-04
            end:
            Time until which available slots should be checked.

            Must be in UTC timezone as ISO 8601 datestring.

            You can pass date without hours which defaults to end of day or specify hours:
            2024-08-20 (will have hours 23:59:59 aka at the very end of the date) or you can specify hours manually like 2024-08-20T18:00:00Z.
            start:
              Time starting from which available slots should be checked.

              Must be in UTC timezone as ISO 8601 datestring.

              You can pass date without hours which defaults to start of day or specify hours:
              2024-08-13 (will have hours 00:00:00 aka at very beginning of the date) or you can specify hours manually like 2024-08-13T09:00:00Z.
            request_options: Additional options to customize the HTTP request

        Returns:
            A map of available slots indexed by date, where each date is associated with an array of time slots. If format=range is specified, each slot will be an object with start and end properties denoting start and end of the slot.
              For seated slots each object will have attendeesCount and bookingUid properties.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.slots.list(
            cal_api_version="string", end="could be anything", start="could be anything"
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "end",
            to_encodable(item=end, dump_with=typing.Any),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "start",
            to_encodable(item=start, dump_with=typing.Any),
            style="form",
            explode=True,
        )
        if not isinstance(duration, type_utils.NotGiven):
            encode_query_param(
                _query,
                "duration",
                to_encodable(item=duration, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(event_type_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventTypeId",
                to_encodable(item=event_type_id, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(event_type_slug, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventTypeSlug",
                to_encodable(item=event_type_slug, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(slot_format, type_utils.NotGiven):
            encode_query_param(
                _query,
                "slotFormat",
                to_encodable(item=slot_format, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(time_zone, type_utils.NotGiven):
            encode_query_param(
                _query,
                "timeZone",
                to_encodable(item=time_zone, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(username, type_utils.NotGiven):
            encode_query_param(
                _query,
                "username",
                to_encodable(item=username, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        if not isinstance(usernames, type_utils.NotGiven):
            encode_query_param(
                _query,
                "usernames",
                to_encodable(item=usernames, dump_with=typing.Any),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="GET",
            path="/v2/slots",
            auth_names=["bearerAuth"],
            query_params=_query,
            headers=_header,
            cast_to=typing.Union[
                models.SlotsListResponseObj0, models.SlotsListResponseObj1
            ],
            request_options=request_options or default_request_options(),
        )
