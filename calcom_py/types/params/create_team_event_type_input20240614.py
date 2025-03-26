import pydantic
import typing
import typing_extensions

from .address_field_input20240614 import (
    AddressFieldInput20240614,
    _SerializerAddressFieldInput20240614,
)
from .base_booking_limits_count20240614 import (
    BaseBookingLimitsCount20240614,
    _SerializerBaseBookingLimitsCount20240614,
)
from .base_booking_limits_duration20240614 import (
    BaseBookingLimitsDuration20240614,
    _SerializerBaseBookingLimitsDuration20240614,
)
from .base_confirmation_policy20240614 import (
    BaseConfirmationPolicy20240614,
    _SerializerBaseConfirmationPolicy20240614,
)
from .booker_layouts20240614 import (
    BookerLayouts20240614,
    _SerializerBookerLayouts20240614,
)
from .boolean_field_input20240614 import (
    BooleanFieldInput20240614,
    _SerializerBooleanFieldInput20240614,
)
from .business_days_window20240614 import (
    BusinessDaysWindow20240614,
    _SerializerBusinessDaysWindow20240614,
)
from .calendar_days_window20240614 import (
    CalendarDaysWindow20240614,
    _SerializerCalendarDaysWindow20240614,
)
from .checkbox_group_field_input20240614 import (
    CheckboxGroupFieldInput20240614,
    _SerializerCheckboxGroupFieldInput20240614,
)
from .destination_calendar20240614 import (
    DestinationCalendar20240614,
    _SerializerDestinationCalendar20240614,
)
from .disabled20240614 import Disabled20240614, _SerializerDisabled20240614
from .email_default_field_input20240614 import (
    EmailDefaultFieldInput20240614,
    _SerializerEmailDefaultFieldInput20240614,
)
from .event_type_color20240614 import (
    EventTypeColor20240614,
    _SerializerEventTypeColor20240614,
)
from .guests_default_field_input20240614 import (
    GuestsDefaultFieldInput20240614,
    _SerializerGuestsDefaultFieldInput20240614,
)
from .host import Host, _SerializerHost
from .input_address_location20240614 import (
    InputAddressLocation20240614,
    _SerializerInputAddressLocation20240614,
)
from .input_attendee_address_location20240614 import (
    InputAttendeeAddressLocation20240614,
    _SerializerInputAttendeeAddressLocation20240614,
)
from .input_attendee_defined_location20240614 import (
    InputAttendeeDefinedLocation20240614,
    _SerializerInputAttendeeDefinedLocation20240614,
)
from .input_attendee_phone_location20240614 import (
    InputAttendeePhoneLocation20240614,
    _SerializerInputAttendeePhoneLocation20240614,
)
from .input_integration_location20240614 import (
    InputIntegrationLocation20240614,
    _SerializerInputIntegrationLocation20240614,
)
from .input_link_location20240614 import (
    InputLinkLocation20240614,
    _SerializerInputLinkLocation20240614,
)
from .input_organizers_default_app20240614 import (
    InputOrganizersDefaultApp20240614,
    _SerializerInputOrganizersDefaultApp20240614,
)
from .input_phone_location20240614 import (
    InputPhoneLocation20240614,
    _SerializerInputPhoneLocation20240614,
)
from .multi_email_field_input20240614 import (
    MultiEmailFieldInput20240614,
    _SerializerMultiEmailFieldInput20240614,
)
from .multi_select_field_input20240614 import (
    MultiSelectFieldInput20240614,
    _SerializerMultiSelectFieldInput20240614,
)
from .name_default_field_input20240614 import (
    NameDefaultFieldInput20240614,
    _SerializerNameDefaultFieldInput20240614,
)
from .notes_default_field_input20240614 import (
    NotesDefaultFieldInput20240614,
    _SerializerNotesDefaultFieldInput20240614,
)
from .number_field_input20240614 import (
    NumberFieldInput20240614,
    _SerializerNumberFieldInput20240614,
)
from .phone_field_input20240614 import (
    PhoneFieldInput20240614,
    _SerializerPhoneFieldInput20240614,
)
from .radio_group_field_input20240614 import (
    RadioGroupFieldInput20240614,
    _SerializerRadioGroupFieldInput20240614,
)
from .range_window20240614 import RangeWindow20240614, _SerializerRangeWindow20240614
from .recurrence20240614 import Recurrence20240614, _SerializerRecurrence20240614
from .reschedule_reason_default_field_input20240614 import (
    RescheduleReasonDefaultFieldInput20240614,
    _SerializerRescheduleReasonDefaultFieldInput20240614,
)
from .seats20240614 import Seats20240614, _SerializerSeats20240614
from .select_field_input20240614 import (
    SelectFieldInput20240614,
    _SerializerSelectFieldInput20240614,
)
from .text_area_field_input20240614 import (
    TextAreaFieldInput20240614,
    _SerializerTextAreaFieldInput20240614,
)
from .text_field_input20240614 import (
    TextFieldInput20240614,
    _SerializerTextFieldInput20240614,
)
from .title_default_field_input20240614 import (
    TitleDefaultFieldInput20240614,
    _SerializerTitleDefaultFieldInput20240614,
)
from .url_field_input20240614 import (
    UrlFieldInput20240614,
    _SerializerUrlFieldInput20240614,
)


class CreateTeamEventTypeInput20240614(typing_extensions.TypedDict):
    """
    CreateTeamEventTypeInput20240614
    """

    after_event_buffer: typing_extensions.NotRequired[float]
    """
    Time spaces that can be appended after an event to give more time after it.
    """

    assign_all_team_members: typing_extensions.NotRequired[bool]
    """
    If true, all current and future team members will be assigned to this event type
    """

    before_event_buffer: typing_extensions.NotRequired[float]
    """
    Time spaces that can be prepended before an event to give more time before it.
    """

    booker_layouts: typing_extensions.NotRequired[BookerLayouts20240614]

    booking_fields: typing_extensions.NotRequired[
        typing.List[
            typing.Union[
                NameDefaultFieldInput20240614,
                EmailDefaultFieldInput20240614,
                TitleDefaultFieldInput20240614,
                NotesDefaultFieldInput20240614,
                GuestsDefaultFieldInput20240614,
                RescheduleReasonDefaultFieldInput20240614,
                PhoneFieldInput20240614,
                AddressFieldInput20240614,
                TextFieldInput20240614,
                NumberFieldInput20240614,
                TextAreaFieldInput20240614,
                SelectFieldInput20240614,
                MultiSelectFieldInput20240614,
                MultiEmailFieldInput20240614,
                CheckboxGroupFieldInput20240614,
                RadioGroupFieldInput20240614,
                BooleanFieldInput20240614,
                UrlFieldInput20240614,
            ]
        ]
    ]
    """
    Custom fields that can be added to the booking form when the event is booked by someone. By default booking form has name and email field.
    """

    booking_limits_count: typing_extensions.NotRequired[
        typing.Union[BaseBookingLimitsCount20240614, Disabled20240614]
    ]
    """
    Limit how many times this event can be booked
    """

    booking_limits_duration: typing_extensions.NotRequired[
        typing.Union[BaseBookingLimitsDuration20240614, Disabled20240614]
    ]
    """
    Limit total amount of time that this event can be booked
    """

    booking_window: typing_extensions.NotRequired[
        typing.Union[
            BusinessDaysWindow20240614,
            CalendarDaysWindow20240614,
            RangeWindow20240614,
            Disabled20240614,
        ]
    ]
    """
    Limit how far in the future this event can be booked
    """

    color: typing_extensions.NotRequired[EventTypeColor20240614]

    confirmation_policy: typing_extensions.NotRequired[
        typing.Union[BaseConfirmationPolicy20240614, Disabled20240614]
    ]
    """
    Specify how the booking needs to be manually confirmed before it is pushed to the integrations and a confirmation mail is sent.
    """

    custom_name: typing_extensions.NotRequired[str]
    """
    Customizable event name with valid variables: 
          {Event type title}, {Organiser}, {Scheduler}, {Location}, {Organiser first name}, 
          {Scheduler first name}, {Scheduler last name}, {Event duration}, {LOCATION}, 
          {HOST/ATTENDEE}, {HOST}, {ATTENDEE}, {USER}
    """

    description: typing_extensions.NotRequired[str]

    destination_calendar: typing_extensions.NotRequired[DestinationCalendar20240614]

    disable_guests: typing_extensions.NotRequired[bool]
    """
    If true, person booking this event can't add guests via their emails.
    """

    hide_calendar_event_details: typing_extensions.NotRequired[bool]

    hide_calendar_notes: typing_extensions.NotRequired[bool]

    hosts: typing_extensions.Required[typing.List[Host]]

    length_in_minutes: typing_extensions.Required[float]

    length_in_minutes_options: typing_extensions.NotRequired[typing.List[str]]
    """
    If you want that user can choose between different lengths of the event you can specify them here. Must include the provided `lengthInMinutes`.
    """

    locations: typing_extensions.NotRequired[
        typing.List[
            typing.Union[
                InputAddressLocation20240614,
                InputLinkLocation20240614,
                InputIntegrationLocation20240614,
                InputPhoneLocation20240614,
                InputAttendeeAddressLocation20240614,
                InputAttendeePhoneLocation20240614,
                InputAttendeeDefinedLocation20240614,
                InputOrganizersDefaultApp20240614,
            ]
        ]
    ]
    """
    Locations where the event will take place. If not provided, cal video link will be used as the location.
    """

    lock_time_zone_toggle_on_booking_page: typing_extensions.NotRequired[bool]

    minimum_booking_notice: typing_extensions.NotRequired[float]
    """
    Minimum number of minutes before the event that a booking can be made.
    """

    offset_start: typing_extensions.NotRequired[float]
    """
    Offset timeslots shown to bookers by a specified number of minutes
    """

    only_show_first_available_slot: typing_extensions.NotRequired[bool]
    """
    This will limit your availability for this event type to one slot per day, scheduled at the earliest available time.
    """

    recurrence: typing_extensions.NotRequired[
        typing.Union[Recurrence20240614, Disabled20240614]
    ]
    """
    Create a recurring event type.
    """

    requires_booker_email_verification: typing_extensions.NotRequired[bool]

    schedule_id: typing_extensions.NotRequired[float]
    """
    If you want that this event has different schedule than user's default one you can specify it here.
    """

    scheduling_type: typing_extensions.Required[
        typing_extensions.Literal["collective", "managed", "roundRobin"]
    ]
    """
    The scheduling type for the team event - collective, roundRobin or managed.
    """

    seats: typing_extensions.NotRequired[typing.Union[Seats20240614, Disabled20240614]]
    """
    Create an event type with multiple seats.
    """

    slot_interval: typing_extensions.NotRequired[float]
    """
    Number representing length of each slot when event is booked. By default it equal length of the event type.
          If event length is 60 minutes then we would have slots 9AM, 10AM, 11AM etc. but if it was changed to 30 minutes then
          we would have slots 9AM, 9:30AM, 10AM, 10:30AM etc. as the available times to book the 60 minute event.
    """

    slug: typing_extensions.Required[str]

    success_redirect_url: typing_extensions.NotRequired[str]
    """
    A valid URL where the booker will redirect to, once the booking is completed successfully
    """

    title: typing_extensions.Required[str]

    use_destination_calendar_email: typing_extensions.NotRequired[bool]


class _SerializerCreateTeamEventTypeInput20240614(pydantic.BaseModel):
    """
    Serializer for CreateTeamEventTypeInput20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    after_event_buffer: typing.Optional[float] = pydantic.Field(
        alias="afterEventBuffer", default=None
    )
    assign_all_team_members: typing.Optional[bool] = pydantic.Field(
        alias="assignAllTeamMembers", default=None
    )
    before_event_buffer: typing.Optional[float] = pydantic.Field(
        alias="beforeEventBuffer", default=None
    )
    booker_layouts: typing.Optional[_SerializerBookerLayouts20240614] = pydantic.Field(
        alias="bookerLayouts", default=None
    )
    booking_fields: typing.Optional[
        typing.List[
            typing.Union[
                _SerializerNameDefaultFieldInput20240614,
                _SerializerEmailDefaultFieldInput20240614,
                _SerializerTitleDefaultFieldInput20240614,
                _SerializerNotesDefaultFieldInput20240614,
                _SerializerGuestsDefaultFieldInput20240614,
                _SerializerRescheduleReasonDefaultFieldInput20240614,
                _SerializerPhoneFieldInput20240614,
                _SerializerAddressFieldInput20240614,
                _SerializerTextFieldInput20240614,
                _SerializerNumberFieldInput20240614,
                _SerializerTextAreaFieldInput20240614,
                _SerializerSelectFieldInput20240614,
                _SerializerMultiSelectFieldInput20240614,
                _SerializerMultiEmailFieldInput20240614,
                _SerializerCheckboxGroupFieldInput20240614,
                _SerializerRadioGroupFieldInput20240614,
                _SerializerBooleanFieldInput20240614,
                _SerializerUrlFieldInput20240614,
            ]
        ]
    ] = pydantic.Field(alias="bookingFields", default=None)
    booking_limits_count: typing.Optional[
        typing.Union[
            _SerializerBaseBookingLimitsCount20240614, _SerializerDisabled20240614
        ]
    ] = pydantic.Field(alias="bookingLimitsCount", default=None)
    booking_limits_duration: typing.Optional[
        typing.Union[
            _SerializerBaseBookingLimitsDuration20240614, _SerializerDisabled20240614
        ]
    ] = pydantic.Field(alias="bookingLimitsDuration", default=None)
    booking_window: typing.Optional[
        typing.Union[
            _SerializerBusinessDaysWindow20240614,
            _SerializerCalendarDaysWindow20240614,
            _SerializerRangeWindow20240614,
            _SerializerDisabled20240614,
        ]
    ] = pydantic.Field(alias="bookingWindow", default=None)
    color: typing.Optional[_SerializerEventTypeColor20240614] = pydantic.Field(
        alias="color", default=None
    )
    confirmation_policy: typing.Optional[
        typing.Union[
            _SerializerBaseConfirmationPolicy20240614, _SerializerDisabled20240614
        ]
    ] = pydantic.Field(alias="confirmationPolicy", default=None)
    custom_name: typing.Optional[str] = pydantic.Field(alias="customName", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    destination_calendar: typing.Optional[_SerializerDestinationCalendar20240614] = (
        pydantic.Field(alias="destinationCalendar", default=None)
    )
    disable_guests: typing.Optional[bool] = pydantic.Field(
        alias="disableGuests", default=None
    )
    hide_calendar_event_details: typing.Optional[bool] = pydantic.Field(
        alias="hideCalendarEventDetails", default=None
    )
    hide_calendar_notes: typing.Optional[bool] = pydantic.Field(
        alias="hideCalendarNotes", default=None
    )
    hosts: typing.List[_SerializerHost] = pydantic.Field(
        alias="hosts",
    )
    length_in_minutes: float = pydantic.Field(
        alias="lengthInMinutes",
    )
    length_in_minutes_options: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="lengthInMinutesOptions", default=None
    )
    locations: typing.Optional[
        typing.List[
            typing.Union[
                _SerializerInputAddressLocation20240614,
                _SerializerInputLinkLocation20240614,
                _SerializerInputIntegrationLocation20240614,
                _SerializerInputPhoneLocation20240614,
                _SerializerInputAttendeeAddressLocation20240614,
                _SerializerInputAttendeePhoneLocation20240614,
                _SerializerInputAttendeeDefinedLocation20240614,
                _SerializerInputOrganizersDefaultApp20240614,
            ]
        ]
    ] = pydantic.Field(alias="locations", default=None)
    lock_time_zone_toggle_on_booking_page: typing.Optional[bool] = pydantic.Field(
        alias="lockTimeZoneToggleOnBookingPage", default=None
    )
    minimum_booking_notice: typing.Optional[float] = pydantic.Field(
        alias="minimumBookingNotice", default=None
    )
    offset_start: typing.Optional[float] = pydantic.Field(
        alias="offsetStart", default=None
    )
    only_show_first_available_slot: typing.Optional[bool] = pydantic.Field(
        alias="onlyShowFirstAvailableSlot", default=None
    )
    recurrence: typing.Optional[
        typing.Union[_SerializerRecurrence20240614, _SerializerDisabled20240614]
    ] = pydantic.Field(alias="recurrence", default=None)
    requires_booker_email_verification: typing.Optional[bool] = pydantic.Field(
        alias="requiresBookerEmailVerification", default=None
    )
    schedule_id: typing.Optional[float] = pydantic.Field(
        alias="scheduleId", default=None
    )
    scheduling_type: typing_extensions.Literal[
        "collective", "managed", "roundRobin"
    ] = pydantic.Field(
        alias="schedulingType",
    )
    seats: typing.Optional[
        typing.Union[_SerializerSeats20240614, _SerializerDisabled20240614]
    ] = pydantic.Field(alias="seats", default=None)
    slot_interval: typing.Optional[float] = pydantic.Field(
        alias="slotInterval", default=None
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
    success_redirect_url: typing.Optional[str] = pydantic.Field(
        alias="successRedirectUrl", default=None
    )
    title: str = pydantic.Field(
        alias="title",
    )
    use_destination_calendar_email: typing.Optional[bool] = pydantic.Field(
        alias="useDestinationCalendarEmail", default=None
    )
