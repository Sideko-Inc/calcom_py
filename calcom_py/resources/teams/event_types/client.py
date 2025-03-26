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
from calcom_py.resources.teams.event_types.create_phone_call import (
    AsyncCreatePhoneCallClient,
    CreatePhoneCallClient,
)
from calcom_py.types import models, params


class EventTypesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.create_phone_call = CreatePhoneCallClient(base_client=self._base_client)

    def delete(
        self,
        *,
        event_type_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteTeamEventTypeOutput:
        """
        Delete a team event type

        DELETE /v2/teams/{teamId}/event-types/{eventTypeId}

        Args:
            eventTypeId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.event_types.delete(event_type_id=123.0, team_id=123.0)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/teams/{team_id}/event-types/{event_type_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteTeamEventTypeOutput,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        team_id: float,
        event_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hosts_limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetTeamEventTypesOutput:
        """
        Get a team event type

        GET /v2/teams/{teamId}/event-types

        Args:
            eventSlug: Slug of team event type to return.
            hostsLimit: Specifies the maximum number of hosts to include in the response. This limit helps optimize performance. If not provided, all Hosts will be fetched.
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.event_types.list(team_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(event_slug, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventSlug",
                to_encodable(item=event_slug, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(hosts_limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "hostsLimit",
                to_encodable(item=hosts_limit, dump_with=float),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/v2/teams/{team_id}/event-types",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetTeamEventTypesOutput,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        event_type_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetTeamEventTypeOutput:
        """
        Get an event type

        GET /v2/teams/{teamId}/event-types/{eventTypeId}

        Args:
            eventTypeId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.event_types.get(event_type_id=123.0, team_id=123.0)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/teams/{team_id}/event-types/{event_type_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetTeamEventTypeOutput,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        event_type_id: float,
        team_id: float,
        after_event_buffer: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        assign_all_team_members: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_event_buffer: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booker_layouts: typing.Union[
            typing.Optional[params.BookerLayouts20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_fields: typing.Union[
            typing.Optional[
                typing.List[
                    typing.Union[
                        params.NameDefaultFieldInput20240614,
                        params.EmailDefaultFieldInput20240614,
                        params.TitleDefaultFieldInput20240614,
                        params.NotesDefaultFieldInput20240614,
                        params.GuestsDefaultFieldInput20240614,
                        params.RescheduleReasonDefaultFieldInput20240614,
                        params.PhoneFieldInput20240614,
                        params.AddressFieldInput20240614,
                        params.TextFieldInput20240614,
                        params.NumberFieldInput20240614,
                        params.TextAreaFieldInput20240614,
                        params.SelectFieldInput20240614,
                        params.MultiSelectFieldInput20240614,
                        params.MultiEmailFieldInput20240614,
                        params.CheckboxGroupFieldInput20240614,
                        params.RadioGroupFieldInput20240614,
                        params.BooleanFieldInput20240614,
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_limits_count: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseBookingLimitsCount20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_limits_duration: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseBookingLimitsDuration20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_window: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BusinessDaysWindow20240614,
                    params.CalendarDaysWindow20240614,
                    params.RangeWindow20240614,
                    params.Disabled20240614,
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        color: typing.Union[
            typing.Optional[params.EventTypeColor20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        confirmation_policy: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseConfirmationPolicy20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        custom_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_calendar: typing.Union[
            typing.Optional[params.DestinationCalendar20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disable_guests: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_calendar_event_details: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_calendar_notes: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hosts: typing.Union[
            typing.Optional[typing.List[params.Host]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        length_in_minutes: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        length_in_minutes_options: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        locations: typing.Union[
            typing.Optional[
                typing.List[
                    typing.Union[
                        params.InputAddressLocation20240614,
                        params.InputLinkLocation20240614,
                        params.InputIntegrationLocation20240614,
                        params.InputPhoneLocation20240614,
                        params.InputAttendeeAddressLocation20240614,
                        params.InputAttendeePhoneLocation20240614,
                        params.InputAttendeeDefinedLocation20240614,
                        params.InputOrganizersDefaultApp20240614,
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        lock_time_zone_toggle_on_booking_page: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        minimum_booking_notice: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset_start: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        only_show_first_available_slot: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        recurrence: typing.Union[
            typing.Optional[
                typing.Union[params.Recurrence20240614, params.Disabled20240614]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        requires_booker_email_verification: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        schedule_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        seats: typing.Union[
            typing.Optional[
                typing.Union[params.Seats20240614, params.Disabled20240614]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        slot_interval: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        success_redirect_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        use_destination_calendar_email: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateTeamEventTypeOutput:
        """
        Update a team event type

        PATCH /v2/teams/{teamId}/event-types/{eventTypeId}

        Args:
            afterEventBuffer: Time spaces that can be appended after an event to give more time after it.
            assignAllTeamMembers: If true, all current and future team members will be assigned to this event type
            beforeEventBuffer: Time spaces that can be prepended before an event to give more time before it.
            bookerLayouts: BookerLayouts20240614
            bookingFields: Custom fields that can be added to the booking form when the event is booked by someone. By default booking form has name and email field.
            bookingLimitsCount: Limit how many times this event can be booked
            bookingLimitsDuration: Limit total amount of time that this event can be booked
            bookingWindow: Limit how far in the future this event can be booked
            color: EventTypeColor20240614
            confirmationPolicy: Specify how the booking needs to be manually confirmed before it is pushed to the integrations and a confirmation mail is sent.
            customName: Customizable event name with valid variables:
              {Event type title}, {Organiser}, {Scheduler}, {Location}, {Organiser first name},
              {Scheduler first name}, {Scheduler last name}, {Event duration}, {LOCATION},
              {HOST/ATTENDEE}, {HOST}, {ATTENDEE}, {USER}
            description: str
            destinationCalendar: DestinationCalendar20240614
            disableGuests: If true, person booking this event can't add guests via their emails.
            hideCalendarEventDetails: bool
            hideCalendarNotes: bool
            hosts: typing.List[Host]
            lengthInMinutes: float
            lengthInMinutesOptions: If you want that user can choose between different lengths of the event you can specify them here. Must include the provided `lengthInMinutes`.
            locations: Locations where the event will take place. If not provided, cal video link will be used as the location.
            lockTimeZoneToggleOnBookingPage: bool
            minimumBookingNotice: Minimum number of minutes before the event that a booking can be made.
            offsetStart: Offset timeslots shown to bookers by a specified number of minutes
            onlyShowFirstAvailableSlot: This will limit your availability for this event type to one slot per day, scheduled at the earliest available time.
            recurrence: Create a recurring event type.
            requiresBookerEmailVerification: bool
            scheduleId: If you want that this event has different schedule than user's default one you can specify it here.
            seats: Create an event type with multiple seats.
            slotInterval: Number representing length of each slot when event is booked. By default it equal length of the event type.
              If event length is 60 minutes then we would have slots 9AM, 10AM, 11AM etc. but if it was changed to 30 minutes then
              we would have slots 9AM, 9:30AM, 10AM, 10:30AM etc. as the available times to book the 60 minute event.
            slug: str
            successRedirectUrl: A valid URL where the booker will redirect to, once the booking is completed successfully
            title: str
            useDestinationCalendarEmail: bool
            eventTypeId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.event_types.patch(
            event_type_id=123.0,
            team_id=123.0,
            custom_name="{Event type title} between {Organiser} and {Scheduler}",
            description="Discover the culinary wonders of the Argentina by making the best flan ever!",
            length_in_minutes=60.0,
            length_in_minutes_options=["string", "string", "string"],
            slug="learn-the-secrets-of-masterchief",
            success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
            title="Learn the secrets of masterchief!",
        )
        ```
        """
        _json = to_encodable(
            item={
                "after_event_buffer": after_event_buffer,
                "assign_all_team_members": assign_all_team_members,
                "before_event_buffer": before_event_buffer,
                "booker_layouts": booker_layouts,
                "booking_fields": booking_fields,
                "booking_limits_count": booking_limits_count,
                "booking_limits_duration": booking_limits_duration,
                "booking_window": booking_window,
                "color": color,
                "confirmation_policy": confirmation_policy,
                "custom_name": custom_name,
                "description": description,
                "destination_calendar": destination_calendar,
                "disable_guests": disable_guests,
                "hide_calendar_event_details": hide_calendar_event_details,
                "hide_calendar_notes": hide_calendar_notes,
                "hosts": hosts,
                "length_in_minutes": length_in_minutes,
                "length_in_minutes_options": length_in_minutes_options,
                "locations": locations,
                "lock_time_zone_toggle_on_booking_page": lock_time_zone_toggle_on_booking_page,
                "minimum_booking_notice": minimum_booking_notice,
                "offset_start": offset_start,
                "only_show_first_available_slot": only_show_first_available_slot,
                "recurrence": recurrence,
                "requires_booker_email_verification": requires_booker_email_verification,
                "schedule_id": schedule_id,
                "seats": seats,
                "slot_interval": slot_interval,
                "slug": slug,
                "success_redirect_url": success_redirect_url,
                "title": title,
                "use_destination_calendar_email": use_destination_calendar_email,
            },
            dump_with=params._SerializerUpdateTeamEventTypeInput20240614,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/teams/{team_id}/event-types/{event_type_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateTeamEventTypeOutput,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        hosts: typing.List[params.Host],
        length_in_minutes: float,
        scheduling_type: typing_extensions.Literal[
            "collective", "managed", "roundRobin"
        ],
        slug: str,
        team_id: float,
        title: str,
        after_event_buffer: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        assign_all_team_members: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_event_buffer: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booker_layouts: typing.Union[
            typing.Optional[params.BookerLayouts20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_fields: typing.Union[
            typing.Optional[
                typing.List[
                    typing.Union[
                        params.NameDefaultFieldInput20240614,
                        params.EmailDefaultFieldInput20240614,
                        params.TitleDefaultFieldInput20240614,
                        params.NotesDefaultFieldInput20240614,
                        params.GuestsDefaultFieldInput20240614,
                        params.RescheduleReasonDefaultFieldInput20240614,
                        params.PhoneFieldInput20240614,
                        params.AddressFieldInput20240614,
                        params.TextFieldInput20240614,
                        params.NumberFieldInput20240614,
                        params.TextAreaFieldInput20240614,
                        params.SelectFieldInput20240614,
                        params.MultiSelectFieldInput20240614,
                        params.MultiEmailFieldInput20240614,
                        params.CheckboxGroupFieldInput20240614,
                        params.RadioGroupFieldInput20240614,
                        params.BooleanFieldInput20240614,
                        params.UrlFieldInput20240614,
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_limits_count: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseBookingLimitsCount20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_limits_duration: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseBookingLimitsDuration20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_window: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BusinessDaysWindow20240614,
                    params.CalendarDaysWindow20240614,
                    params.RangeWindow20240614,
                    params.Disabled20240614,
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        color: typing.Union[
            typing.Optional[params.EventTypeColor20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        confirmation_policy: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseConfirmationPolicy20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        custom_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_calendar: typing.Union[
            typing.Optional[params.DestinationCalendar20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disable_guests: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_calendar_event_details: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_calendar_notes: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        length_in_minutes_options: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        locations: typing.Union[
            typing.Optional[
                typing.List[
                    typing.Union[
                        params.InputAddressLocation20240614,
                        params.InputLinkLocation20240614,
                        params.InputIntegrationLocation20240614,
                        params.InputPhoneLocation20240614,
                        params.InputAttendeeAddressLocation20240614,
                        params.InputAttendeePhoneLocation20240614,
                        params.InputAttendeeDefinedLocation20240614,
                        params.InputOrganizersDefaultApp20240614,
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        lock_time_zone_toggle_on_booking_page: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        minimum_booking_notice: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset_start: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        only_show_first_available_slot: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        recurrence: typing.Union[
            typing.Optional[
                typing.Union[params.Recurrence20240614, params.Disabled20240614]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        requires_booker_email_verification: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        schedule_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        seats: typing.Union[
            typing.Optional[
                typing.Union[params.Seats20240614, params.Disabled20240614]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        slot_interval: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        success_redirect_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        use_destination_calendar_email: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateTeamEventTypeOutput:
        """
        Create an event type

        POST /v2/teams/{teamId}/event-types

        Args:
            afterEventBuffer: Time spaces that can be appended after an event to give more time after it.
            assignAllTeamMembers: If true, all current and future team members will be assigned to this event type
            beforeEventBuffer: Time spaces that can be prepended before an event to give more time before it.
            bookerLayouts: BookerLayouts20240614
            bookingFields: Custom fields that can be added to the booking form when the event is booked by someone. By default booking form has name and email field.
            bookingLimitsCount: Limit how many times this event can be booked
            bookingLimitsDuration: Limit total amount of time that this event can be booked
            bookingWindow: Limit how far in the future this event can be booked
            color: EventTypeColor20240614
            confirmationPolicy: Specify how the booking needs to be manually confirmed before it is pushed to the integrations and a confirmation mail is sent.
            customName: Customizable event name with valid variables:
              {Event type title}, {Organiser}, {Scheduler}, {Location}, {Organiser first name},
              {Scheduler first name}, {Scheduler last name}, {Event duration}, {LOCATION},
              {HOST/ATTENDEE}, {HOST}, {ATTENDEE}, {USER}
            description: str
            destinationCalendar: DestinationCalendar20240614
            disableGuests: If true, person booking this event can't add guests via their emails.
            hideCalendarEventDetails: bool
            hideCalendarNotes: bool
            lengthInMinutesOptions: If you want that user can choose between different lengths of the event you can specify them here. Must include the provided `lengthInMinutes`.
            locations: Locations where the event will take place. If not provided, cal video link will be used as the location.
            lockTimeZoneToggleOnBookingPage: bool
            minimumBookingNotice: Minimum number of minutes before the event that a booking can be made.
            offsetStart: Offset timeslots shown to bookers by a specified number of minutes
            onlyShowFirstAvailableSlot: This will limit your availability for this event type to one slot per day, scheduled at the earliest available time.
            recurrence: Create a recurring event type.
            requiresBookerEmailVerification: bool
            scheduleId: If you want that this event has different schedule than user's default one you can specify it here.
            seats: Create an event type with multiple seats.
            slotInterval: Number representing length of each slot when event is booked. By default it equal length of the event type.
              If event length is 60 minutes then we would have slots 9AM, 10AM, 11AM etc. but if it was changed to 30 minutes then
              we would have slots 9AM, 9:30AM, 10AM, 10:30AM etc. as the available times to book the 60 minute event.
            successRedirectUrl: A valid URL where the booker will redirect to, once the booking is completed successfully
            useDestinationCalendarEmail: bool
            hosts: typing.List[Host]
            lengthInMinutes: float
            schedulingType: The scheduling type for the team event - collective, roundRobin or managed.
            slug: str
            teamId: float
            title: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.event_types.create(
            hosts=[{"user_id": 123.0}],
            length_in_minutes=60.0,
            scheduling_type="collective",
            slug="learn-the-secrets-of-masterchief",
            team_id=123.0,
            title="Learn the secrets of masterchief!",
            custom_name="{Event type title} between {Organiser} and {Scheduler}",
            description="Discover the culinary wonders of the Argentina by making the best flan ever!",
            length_in_minutes_options=["string", "string", "string"],
            success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
        )
        ```
        """
        _json = to_encodable(
            item={
                "after_event_buffer": after_event_buffer,
                "assign_all_team_members": assign_all_team_members,
                "before_event_buffer": before_event_buffer,
                "booker_layouts": booker_layouts,
                "booking_fields": booking_fields,
                "booking_limits_count": booking_limits_count,
                "booking_limits_duration": booking_limits_duration,
                "booking_window": booking_window,
                "color": color,
                "confirmation_policy": confirmation_policy,
                "custom_name": custom_name,
                "description": description,
                "destination_calendar": destination_calendar,
                "disable_guests": disable_guests,
                "hide_calendar_event_details": hide_calendar_event_details,
                "hide_calendar_notes": hide_calendar_notes,
                "length_in_minutes_options": length_in_minutes_options,
                "locations": locations,
                "lock_time_zone_toggle_on_booking_page": lock_time_zone_toggle_on_booking_page,
                "minimum_booking_notice": minimum_booking_notice,
                "offset_start": offset_start,
                "only_show_first_available_slot": only_show_first_available_slot,
                "recurrence": recurrence,
                "requires_booker_email_verification": requires_booker_email_verification,
                "schedule_id": schedule_id,
                "seats": seats,
                "slot_interval": slot_interval,
                "success_redirect_url": success_redirect_url,
                "use_destination_calendar_email": use_destination_calendar_email,
                "hosts": hosts,
                "length_in_minutes": length_in_minutes,
                "scheduling_type": scheduling_type,
                "slug": slug,
                "title": title,
            },
            dump_with=params._SerializerCreateTeamEventTypeInput20240614,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/teams/{team_id}/event-types",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateTeamEventTypeOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncEventTypesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.create_phone_call = AsyncCreatePhoneCallClient(
            base_client=self._base_client
        )

    async def delete(
        self,
        *,
        event_type_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteTeamEventTypeOutput:
        """
        Delete a team event type

        DELETE /v2/teams/{teamId}/event-types/{eventTypeId}

        Args:
            eventTypeId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.event_types.delete(event_type_id=123.0, team_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/teams/{team_id}/event-types/{event_type_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteTeamEventTypeOutput,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        team_id: float,
        event_slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hosts_limit: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetTeamEventTypesOutput:
        """
        Get a team event type

        GET /v2/teams/{teamId}/event-types

        Args:
            eventSlug: Slug of team event type to return.
            hostsLimit: Specifies the maximum number of hosts to include in the response. This limit helps optimize performance. If not provided, all Hosts will be fetched.
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.event_types.list(team_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(event_slug, type_utils.NotGiven):
            encode_query_param(
                _query,
                "eventSlug",
                to_encodable(item=event_slug, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(hosts_limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "hostsLimit",
                to_encodable(item=hosts_limit, dump_with=float),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/v2/teams/{team_id}/event-types",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetTeamEventTypesOutput,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        event_type_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetTeamEventTypeOutput:
        """
        Get an event type

        GET /v2/teams/{teamId}/event-types/{eventTypeId}

        Args:
            eventTypeId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.event_types.get(event_type_id=123.0, team_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/teams/{team_id}/event-types/{event_type_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetTeamEventTypeOutput,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        event_type_id: float,
        team_id: float,
        after_event_buffer: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        assign_all_team_members: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_event_buffer: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booker_layouts: typing.Union[
            typing.Optional[params.BookerLayouts20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_fields: typing.Union[
            typing.Optional[
                typing.List[
                    typing.Union[
                        params.NameDefaultFieldInput20240614,
                        params.EmailDefaultFieldInput20240614,
                        params.TitleDefaultFieldInput20240614,
                        params.NotesDefaultFieldInput20240614,
                        params.GuestsDefaultFieldInput20240614,
                        params.RescheduleReasonDefaultFieldInput20240614,
                        params.PhoneFieldInput20240614,
                        params.AddressFieldInput20240614,
                        params.TextFieldInput20240614,
                        params.NumberFieldInput20240614,
                        params.TextAreaFieldInput20240614,
                        params.SelectFieldInput20240614,
                        params.MultiSelectFieldInput20240614,
                        params.MultiEmailFieldInput20240614,
                        params.CheckboxGroupFieldInput20240614,
                        params.RadioGroupFieldInput20240614,
                        params.BooleanFieldInput20240614,
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_limits_count: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseBookingLimitsCount20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_limits_duration: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseBookingLimitsDuration20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_window: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BusinessDaysWindow20240614,
                    params.CalendarDaysWindow20240614,
                    params.RangeWindow20240614,
                    params.Disabled20240614,
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        color: typing.Union[
            typing.Optional[params.EventTypeColor20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        confirmation_policy: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseConfirmationPolicy20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        custom_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_calendar: typing.Union[
            typing.Optional[params.DestinationCalendar20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disable_guests: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_calendar_event_details: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_calendar_notes: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hosts: typing.Union[
            typing.Optional[typing.List[params.Host]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        length_in_minutes: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        length_in_minutes_options: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        locations: typing.Union[
            typing.Optional[
                typing.List[
                    typing.Union[
                        params.InputAddressLocation20240614,
                        params.InputLinkLocation20240614,
                        params.InputIntegrationLocation20240614,
                        params.InputPhoneLocation20240614,
                        params.InputAttendeeAddressLocation20240614,
                        params.InputAttendeePhoneLocation20240614,
                        params.InputAttendeeDefinedLocation20240614,
                        params.InputOrganizersDefaultApp20240614,
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        lock_time_zone_toggle_on_booking_page: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        minimum_booking_notice: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset_start: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        only_show_first_available_slot: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        recurrence: typing.Union[
            typing.Optional[
                typing.Union[params.Recurrence20240614, params.Disabled20240614]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        requires_booker_email_verification: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        schedule_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        seats: typing.Union[
            typing.Optional[
                typing.Union[params.Seats20240614, params.Disabled20240614]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        slot_interval: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        success_redirect_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        use_destination_calendar_email: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateTeamEventTypeOutput:
        """
        Update a team event type

        PATCH /v2/teams/{teamId}/event-types/{eventTypeId}

        Args:
            afterEventBuffer: Time spaces that can be appended after an event to give more time after it.
            assignAllTeamMembers: If true, all current and future team members will be assigned to this event type
            beforeEventBuffer: Time spaces that can be prepended before an event to give more time before it.
            bookerLayouts: BookerLayouts20240614
            bookingFields: Custom fields that can be added to the booking form when the event is booked by someone. By default booking form has name and email field.
            bookingLimitsCount: Limit how many times this event can be booked
            bookingLimitsDuration: Limit total amount of time that this event can be booked
            bookingWindow: Limit how far in the future this event can be booked
            color: EventTypeColor20240614
            confirmationPolicy: Specify how the booking needs to be manually confirmed before it is pushed to the integrations and a confirmation mail is sent.
            customName: Customizable event name with valid variables:
              {Event type title}, {Organiser}, {Scheduler}, {Location}, {Organiser first name},
              {Scheduler first name}, {Scheduler last name}, {Event duration}, {LOCATION},
              {HOST/ATTENDEE}, {HOST}, {ATTENDEE}, {USER}
            description: str
            destinationCalendar: DestinationCalendar20240614
            disableGuests: If true, person booking this event can't add guests via their emails.
            hideCalendarEventDetails: bool
            hideCalendarNotes: bool
            hosts: typing.List[Host]
            lengthInMinutes: float
            lengthInMinutesOptions: If you want that user can choose between different lengths of the event you can specify them here. Must include the provided `lengthInMinutes`.
            locations: Locations where the event will take place. If not provided, cal video link will be used as the location.
            lockTimeZoneToggleOnBookingPage: bool
            minimumBookingNotice: Minimum number of minutes before the event that a booking can be made.
            offsetStart: Offset timeslots shown to bookers by a specified number of minutes
            onlyShowFirstAvailableSlot: This will limit your availability for this event type to one slot per day, scheduled at the earliest available time.
            recurrence: Create a recurring event type.
            requiresBookerEmailVerification: bool
            scheduleId: If you want that this event has different schedule than user's default one you can specify it here.
            seats: Create an event type with multiple seats.
            slotInterval: Number representing length of each slot when event is booked. By default it equal length of the event type.
              If event length is 60 minutes then we would have slots 9AM, 10AM, 11AM etc. but if it was changed to 30 minutes then
              we would have slots 9AM, 9:30AM, 10AM, 10:30AM etc. as the available times to book the 60 minute event.
            slug: str
            successRedirectUrl: A valid URL where the booker will redirect to, once the booking is completed successfully
            title: str
            useDestinationCalendarEmail: bool
            eventTypeId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.event_types.patch(
            event_type_id=123.0,
            team_id=123.0,
            custom_name="{Event type title} between {Organiser} and {Scheduler}",
            description="Discover the culinary wonders of the Argentina by making the best flan ever!",
            length_in_minutes=60.0,
            length_in_minutes_options=["string", "string", "string"],
            slug="learn-the-secrets-of-masterchief",
            success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
            title="Learn the secrets of masterchief!",
        )
        ```
        """
        _json = to_encodable(
            item={
                "after_event_buffer": after_event_buffer,
                "assign_all_team_members": assign_all_team_members,
                "before_event_buffer": before_event_buffer,
                "booker_layouts": booker_layouts,
                "booking_fields": booking_fields,
                "booking_limits_count": booking_limits_count,
                "booking_limits_duration": booking_limits_duration,
                "booking_window": booking_window,
                "color": color,
                "confirmation_policy": confirmation_policy,
                "custom_name": custom_name,
                "description": description,
                "destination_calendar": destination_calendar,
                "disable_guests": disable_guests,
                "hide_calendar_event_details": hide_calendar_event_details,
                "hide_calendar_notes": hide_calendar_notes,
                "hosts": hosts,
                "length_in_minutes": length_in_minutes,
                "length_in_minutes_options": length_in_minutes_options,
                "locations": locations,
                "lock_time_zone_toggle_on_booking_page": lock_time_zone_toggle_on_booking_page,
                "minimum_booking_notice": minimum_booking_notice,
                "offset_start": offset_start,
                "only_show_first_available_slot": only_show_first_available_slot,
                "recurrence": recurrence,
                "requires_booker_email_verification": requires_booker_email_verification,
                "schedule_id": schedule_id,
                "seats": seats,
                "slot_interval": slot_interval,
                "slug": slug,
                "success_redirect_url": success_redirect_url,
                "title": title,
                "use_destination_calendar_email": use_destination_calendar_email,
            },
            dump_with=params._SerializerUpdateTeamEventTypeInput20240614,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/teams/{team_id}/event-types/{event_type_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateTeamEventTypeOutput,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        hosts: typing.List[params.Host],
        length_in_minutes: float,
        scheduling_type: typing_extensions.Literal[
            "collective", "managed", "roundRobin"
        ],
        slug: str,
        team_id: float,
        title: str,
        after_event_buffer: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        assign_all_team_members: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        before_event_buffer: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booker_layouts: typing.Union[
            typing.Optional[params.BookerLayouts20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_fields: typing.Union[
            typing.Optional[
                typing.List[
                    typing.Union[
                        params.NameDefaultFieldInput20240614,
                        params.EmailDefaultFieldInput20240614,
                        params.TitleDefaultFieldInput20240614,
                        params.NotesDefaultFieldInput20240614,
                        params.GuestsDefaultFieldInput20240614,
                        params.RescheduleReasonDefaultFieldInput20240614,
                        params.PhoneFieldInput20240614,
                        params.AddressFieldInput20240614,
                        params.TextFieldInput20240614,
                        params.NumberFieldInput20240614,
                        params.TextAreaFieldInput20240614,
                        params.SelectFieldInput20240614,
                        params.MultiSelectFieldInput20240614,
                        params.MultiEmailFieldInput20240614,
                        params.CheckboxGroupFieldInput20240614,
                        params.RadioGroupFieldInput20240614,
                        params.BooleanFieldInput20240614,
                        params.UrlFieldInput20240614,
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_limits_count: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseBookingLimitsCount20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_limits_duration: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseBookingLimitsDuration20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        booking_window: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BusinessDaysWindow20240614,
                    params.CalendarDaysWindow20240614,
                    params.RangeWindow20240614,
                    params.Disabled20240614,
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        color: typing.Union[
            typing.Optional[params.EventTypeColor20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        confirmation_policy: typing.Union[
            typing.Optional[
                typing.Union[
                    params.BaseConfirmationPolicy20240614, params.Disabled20240614
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        custom_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_calendar: typing.Union[
            typing.Optional[params.DestinationCalendar20240614], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disable_guests: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_calendar_event_details: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_calendar_notes: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        length_in_minutes_options: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        locations: typing.Union[
            typing.Optional[
                typing.List[
                    typing.Union[
                        params.InputAddressLocation20240614,
                        params.InputLinkLocation20240614,
                        params.InputIntegrationLocation20240614,
                        params.InputPhoneLocation20240614,
                        params.InputAttendeeAddressLocation20240614,
                        params.InputAttendeePhoneLocation20240614,
                        params.InputAttendeeDefinedLocation20240614,
                        params.InputOrganizersDefaultApp20240614,
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        lock_time_zone_toggle_on_booking_page: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        minimum_booking_notice: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset_start: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        only_show_first_available_slot: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        recurrence: typing.Union[
            typing.Optional[
                typing.Union[params.Recurrence20240614, params.Disabled20240614]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        requires_booker_email_verification: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        schedule_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        seats: typing.Union[
            typing.Optional[
                typing.Union[params.Seats20240614, params.Disabled20240614]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        slot_interval: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        success_redirect_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        use_destination_calendar_email: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateTeamEventTypeOutput:
        """
        Create an event type

        POST /v2/teams/{teamId}/event-types

        Args:
            afterEventBuffer: Time spaces that can be appended after an event to give more time after it.
            assignAllTeamMembers: If true, all current and future team members will be assigned to this event type
            beforeEventBuffer: Time spaces that can be prepended before an event to give more time before it.
            bookerLayouts: BookerLayouts20240614
            bookingFields: Custom fields that can be added to the booking form when the event is booked by someone. By default booking form has name and email field.
            bookingLimitsCount: Limit how many times this event can be booked
            bookingLimitsDuration: Limit total amount of time that this event can be booked
            bookingWindow: Limit how far in the future this event can be booked
            color: EventTypeColor20240614
            confirmationPolicy: Specify how the booking needs to be manually confirmed before it is pushed to the integrations and a confirmation mail is sent.
            customName: Customizable event name with valid variables:
              {Event type title}, {Organiser}, {Scheduler}, {Location}, {Organiser first name},
              {Scheduler first name}, {Scheduler last name}, {Event duration}, {LOCATION},
              {HOST/ATTENDEE}, {HOST}, {ATTENDEE}, {USER}
            description: str
            destinationCalendar: DestinationCalendar20240614
            disableGuests: If true, person booking this event can't add guests via their emails.
            hideCalendarEventDetails: bool
            hideCalendarNotes: bool
            lengthInMinutesOptions: If you want that user can choose between different lengths of the event you can specify them here. Must include the provided `lengthInMinutes`.
            locations: Locations where the event will take place. If not provided, cal video link will be used as the location.
            lockTimeZoneToggleOnBookingPage: bool
            minimumBookingNotice: Minimum number of minutes before the event that a booking can be made.
            offsetStart: Offset timeslots shown to bookers by a specified number of minutes
            onlyShowFirstAvailableSlot: This will limit your availability for this event type to one slot per day, scheduled at the earliest available time.
            recurrence: Create a recurring event type.
            requiresBookerEmailVerification: bool
            scheduleId: If you want that this event has different schedule than user's default one you can specify it here.
            seats: Create an event type with multiple seats.
            slotInterval: Number representing length of each slot when event is booked. By default it equal length of the event type.
              If event length is 60 minutes then we would have slots 9AM, 10AM, 11AM etc. but if it was changed to 30 minutes then
              we would have slots 9AM, 9:30AM, 10AM, 10:30AM etc. as the available times to book the 60 minute event.
            successRedirectUrl: A valid URL where the booker will redirect to, once the booking is completed successfully
            useDestinationCalendarEmail: bool
            hosts: typing.List[Host]
            lengthInMinutes: float
            schedulingType: The scheduling type for the team event - collective, roundRobin or managed.
            slug: str
            teamId: float
            title: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.event_types.create(
            hosts=[{"user_id": 123.0}],
            length_in_minutes=60.0,
            scheduling_type="collective",
            slug="learn-the-secrets-of-masterchief",
            team_id=123.0,
            title="Learn the secrets of masterchief!",
            custom_name="{Event type title} between {Organiser} and {Scheduler}",
            description="Discover the culinary wonders of the Argentina by making the best flan ever!",
            length_in_minutes_options=["string", "string", "string"],
            success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
        )
        ```
        """
        _json = to_encodable(
            item={
                "after_event_buffer": after_event_buffer,
                "assign_all_team_members": assign_all_team_members,
                "before_event_buffer": before_event_buffer,
                "booker_layouts": booker_layouts,
                "booking_fields": booking_fields,
                "booking_limits_count": booking_limits_count,
                "booking_limits_duration": booking_limits_duration,
                "booking_window": booking_window,
                "color": color,
                "confirmation_policy": confirmation_policy,
                "custom_name": custom_name,
                "description": description,
                "destination_calendar": destination_calendar,
                "disable_guests": disable_guests,
                "hide_calendar_event_details": hide_calendar_event_details,
                "hide_calendar_notes": hide_calendar_notes,
                "length_in_minutes_options": length_in_minutes_options,
                "locations": locations,
                "lock_time_zone_toggle_on_booking_page": lock_time_zone_toggle_on_booking_page,
                "minimum_booking_notice": minimum_booking_notice,
                "offset_start": offset_start,
                "only_show_first_available_slot": only_show_first_available_slot,
                "recurrence": recurrence,
                "requires_booker_email_verification": requires_booker_email_verification,
                "schedule_id": schedule_id,
                "seats": seats,
                "slot_interval": slot_interval,
                "success_redirect_url": success_redirect_url,
                "use_destination_calendar_email": use_destination_calendar_email,
                "hosts": hosts,
                "length_in_minutes": length_in_minutes,
                "scheduling_type": scheduling_type,
                "slug": slug,
                "title": title,
            },
            dump_with=params._SerializerCreateTeamEventTypeInput20240614,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/teams/{team_id}/event-types",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateTeamEventTypeOutput,
            request_options=request_options or default_request_options(),
        )
