import pydantic
import typing

from .address_field_output20240614 import AddressFieldOutput20240614
from .booker_layouts20240614 import BookerLayouts20240614
from .boolean_field_output20240614 import BooleanFieldOutput20240614
from .business_days_window20240614 import BusinessDaysWindow20240614
from .calendar_days_window20240614 import CalendarDaysWindow20240614
from .checkbox_group_field_output20240614 import CheckboxGroupFieldOutput20240614
from .destination_calendar20240614 import DestinationCalendar20240614
from .email_default_field_output20240614 import EmailDefaultFieldOutput20240614
from .event_type_color20240614 import EventTypeColor20240614
from .guests_default_field_output20240614 import GuestsDefaultFieldOutput20240614
from .location_default_field_output20240614 import LocationDefaultFieldOutput20240614
from .multi_email_field_output20240614 import MultiEmailFieldOutput20240614
from .multi_select_field_output20240614 import MultiSelectFieldOutput20240614
from .name_default_field_output20240614 import NameDefaultFieldOutput20240614
from .notes_default_field_output20240614 import NotesDefaultFieldOutput20240614
from .number_field_output20240614 import NumberFieldOutput20240614
from .output_address_location20240614 import OutputAddressLocation20240614
from .output_integration_location20240614 import OutputIntegrationLocation20240614
from .output_link_location20240614 import OutputLinkLocation20240614
from .output_organizers_default_app_location20240614 import (
    OutputOrganizersDefaultAppLocation20240614,
)
from .output_phone_location20240614 import OutputPhoneLocation20240614
from .output_unknown_location20240614 import OutputUnknownLocation20240614
from .phone_field_output20240614 import PhoneFieldOutput20240614
from .radio_group_field_output20240614 import RadioGroupFieldOutput20240614
from .range_window20240614 import RangeWindow20240614
from .recurrence20240614 import Recurrence20240614
from .reschedule_reason_default_field_output20240614 import (
    RescheduleReasonDefaultFieldOutput20240614,
)
from .seats20240614 import Seats20240614
from .select_field_output20240614 import SelectFieldOutput20240614
from .text_area_field_output20240614 import TextAreaFieldOutput20240614
from .text_field_output20240614 import TextFieldOutput20240614
from .title_default_field_output20240614 import TitleDefaultFieldOutput20240614
from .url_field_output20240614 import UrlFieldOutput20240614


class EventTypeOutput20240614(pydantic.BaseModel):
    """
    EventTypeOutput20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    after_event_buffer: typing.Optional[float] = pydantic.Field(
        alias="afterEventBuffer", default=None
    )
    before_event_buffer: typing.Optional[float] = pydantic.Field(
        alias="beforeEventBuffer", default=None
    )
    booker_layouts: typing.Optional[BookerLayouts20240614] = pydantic.Field(
        alias="bookerLayouts", default=None
    )
    booking_fields: typing.List[
        typing.Union[
            NameDefaultFieldOutput20240614,
            EmailDefaultFieldOutput20240614,
            LocationDefaultFieldOutput20240614,
            RescheduleReasonDefaultFieldOutput20240614,
            TitleDefaultFieldOutput20240614,
            NotesDefaultFieldOutput20240614,
            GuestsDefaultFieldOutput20240614,
            PhoneFieldOutput20240614,
            AddressFieldOutput20240614,
            TextFieldOutput20240614,
            NumberFieldOutput20240614,
            TextAreaFieldOutput20240614,
            SelectFieldOutput20240614,
            MultiSelectFieldOutput20240614,
            MultiEmailFieldOutput20240614,
            CheckboxGroupFieldOutput20240614,
            RadioGroupFieldOutput20240614,
            BooleanFieldOutput20240614,
            UrlFieldOutput20240614,
        ]
    ] = pydantic.Field(
        alias="bookingFields",
    )
    booking_limits_count: typing.Optional[typing.Dict[str, typing.Any]] = (
        pydantic.Field(alias="bookingLimitsCount", default=None)
    )
    booking_limits_duration: typing.Optional[typing.Dict[str, typing.Any]] = (
        pydantic.Field(alias="bookingLimitsDuration", default=None)
    )
    booking_window: typing.Optional[
        typing.List[
            typing.Union[
                BusinessDaysWindow20240614,
                CalendarDaysWindow20240614,
                RangeWindow20240614,
            ]
        ]
    ] = pydantic.Field(alias="bookingWindow", default=None)
    """
    Limit how far in the future this event can be booked
    """
    color: typing.Optional[EventTypeColor20240614] = pydantic.Field(
        alias="color", default=None
    )
    confirmation_policy: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="confirmationPolicy", default=None
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    custom_name: typing.Optional[str] = pydantic.Field(alias="customName", default=None)
    description: str = pydantic.Field(
        alias="description",
    )
    destination_calendar: typing.Optional[DestinationCalendar20240614] = pydantic.Field(
        alias="destinationCalendar", default=None
    )
    disable_guests: bool = pydantic.Field(
        alias="disableGuests",
    )
    forward_params_success_redirect: typing.Optional[typing.Dict[str, typing.Any]] = (
        pydantic.Field(
            alias="forwardParamsSuccessRedirect",
        )
    )
    hide_calendar_event_details: typing.Optional[bool] = pydantic.Field(
        alias="hideCalendarEventDetails", default=None
    )
    hide_calendar_notes: typing.Optional[bool] = pydantic.Field(
        alias="hideCalendarNotes", default=None
    )
    id: float = pydantic.Field(
        alias="id",
    )
    is_instant_event: bool = pydantic.Field(
        alias="isInstantEvent",
    )
    length_in_minutes: float = pydantic.Field(
        alias="lengthInMinutes",
    )
    length_in_minutes_options: typing.Optional[typing.List[float]] = pydantic.Field(
        alias="lengthInMinutesOptions", default=None
    )
    """
    If you want that user can choose between different lengths of the event you can specify them here. Must include the provided `lengthInMinutes`.
    """
    locations: typing.List[
        typing.Union[
            OutputAddressLocation20240614,
            OutputLinkLocation20240614,
            OutputIntegrationLocation20240614,
            OutputPhoneLocation20240614,
            OutputOrganizersDefaultAppLocation20240614,
            OutputUnknownLocation20240614,
        ]
    ] = pydantic.Field(
        alias="locations",
    )
    lock_time_zone_toggle_on_booking_page: bool = pydantic.Field(
        alias="lockTimeZoneToggleOnBookingPage",
    )
    metadata: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="metadata",
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
    owner_id: float = pydantic.Field(
        alias="ownerId",
    )
    price: float = pydantic.Field(
        alias="price",
    )
    recurrence: Recurrence20240614 = pydantic.Field(
        alias="recurrence",
    )
    requires_booker_email_verification: typing.Optional[bool] = pydantic.Field(
        alias="requiresBookerEmailVerification", default=None
    )
    schedule_id: typing.Optional[float] = pydantic.Field(
        alias="scheduleId",
    )
    seats: typing.Optional[Seats20240614] = pydantic.Field(alias="seats", default=None)
    seats_per_time_slot: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="seatsPerTimeSlot", default=None
    )
    seats_show_availability_count: typing.Optional[bool] = pydantic.Field(
        alias="seatsShowAvailabilityCount", default=None
    )
    slot_interval: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="slotInterval", default=None
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
    success_redirect_url: typing.Optional[typing.Dict[str, typing.Any]] = (
        pydantic.Field(
            alias="successRedirectUrl",
        )
    )
    title: str = pydantic.Field(
        alias="title",
    )
    use_destination_calendar_email: typing.Optional[bool] = pydantic.Field(
        alias="useDestinationCalendarEmail", default=None
    )
    users: typing.List[str] = pydantic.Field(
        alias="users",
    )
