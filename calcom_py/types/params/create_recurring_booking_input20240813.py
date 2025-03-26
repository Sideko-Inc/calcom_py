import pydantic
import typing
import typing_extensions

from .attendee import Attendee, _SerializerAttendee
from .booking_input_address_location20240813 import (
    BookingInputAddressLocation20240813,
    _SerializerBookingInputAddressLocation20240813,
)
from .booking_input_attendee_address_location20240813 import (
    BookingInputAttendeeAddressLocation20240813,
    _SerializerBookingInputAttendeeAddressLocation20240813,
)
from .booking_input_attendee_defined_location20240813 import (
    BookingInputAttendeeDefinedLocation20240813,
    _SerializerBookingInputAttendeeDefinedLocation20240813,
)
from .booking_input_attendee_phone_location20240813 import (
    BookingInputAttendeePhoneLocation20240813,
    _SerializerBookingInputAttendeePhoneLocation20240813,
)
from .booking_input_integration_location20240813 import (
    BookingInputIntegrationLocation20240813,
    _SerializerBookingInputIntegrationLocation20240813,
)
from .booking_input_link_location20240813 import (
    BookingInputLinkLocation20240813,
    _SerializerBookingInputLinkLocation20240813,
)
from .booking_input_organizers_default_app_location20240813 import (
    BookingInputOrganizersDefaultAppLocation20240813,
    _SerializerBookingInputOrganizersDefaultAppLocation20240813,
)
from .booking_input_phone_location20240813 import (
    BookingInputPhoneLocation20240813,
    _SerializerBookingInputPhoneLocation20240813,
)


class CreateRecurringBookingInput20240813(typing_extensions.TypedDict):
    """
    CreateRecurringBookingInput20240813
    """

    attendee: typing_extensions.Required[Attendee]

    booking_fields_responses: typing_extensions.NotRequired[
        typing.Dict[str, typing.Any]
    ]
    """
    Booking field responses consisting of an object with booking field slug as keys and user response as values.
    """

    event_type_id: typing_extensions.Required[float]
    """
    The ID of the event type that is booked.
    """

    guests: typing_extensions.NotRequired[typing.List[str]]
    """
    An optional list of guest emails attending the event.
    """

    length_in_minutes: typing_extensions.NotRequired[float]
    """
    If it is an event type that has multiple possible lengths that attendee can pick from, you can pass the desired booking length here.
        If not provided then event type default length will be used for the booking.
    """

    location: typing_extensions.NotRequired[
        typing.Union[
            BookingInputAddressLocation20240813,
            BookingInputAttendeeAddressLocation20240813,
            BookingInputAttendeeDefinedLocation20240813,
            BookingInputAttendeePhoneLocation20240813,
            BookingInputIntegrationLocation20240813,
            BookingInputLinkLocation20240813,
            BookingInputPhoneLocation20240813,
            BookingInputOrganizersDefaultAppLocation20240813,
        ]
    ]
    """
    One of the event type locations. If instead of passing one of the location objects as required by schema you are still passing a string please use an object.
    """

    meeting_url: typing_extensions.NotRequired[str]
    """
    Deprecated - use 'location' instead. Meeting URL just for this booking. Displayed in email and calendar event. If not provided then cal video link will be generated.
    """

    metadata: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    You can store any additional data you want here. Metadata must have at most 50 keys, each key up to 40 characters, and string values up to 500 characters.
    """

    recurrence_count: typing_extensions.NotRequired[float]
    """
    The number of recurrences. If not provided then event type recurrence count will be used. Can't be more than
        event type recurrence count
    """

    start: typing_extensions.Required[str]
    """
    The start time of the booking in ISO 8601 format in UTC timezone.
    """


class _SerializerCreateRecurringBookingInput20240813(pydantic.BaseModel):
    """
    Serializer for CreateRecurringBookingInput20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attendee: _SerializerAttendee = pydantic.Field(
        alias="attendee",
    )
    booking_fields_responses: typing.Optional[typing.Dict[str, typing.Any]] = (
        pydantic.Field(alias="bookingFieldsResponses", default=None)
    )
    event_type_id: float = pydantic.Field(
        alias="eventTypeId",
    )
    guests: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="guests", default=None
    )
    length_in_minutes: typing.Optional[float] = pydantic.Field(
        alias="lengthInMinutes", default=None
    )
    location: typing.Optional[
        typing.Union[
            _SerializerBookingInputAddressLocation20240813,
            _SerializerBookingInputAttendeeAddressLocation20240813,
            _SerializerBookingInputAttendeeDefinedLocation20240813,
            _SerializerBookingInputAttendeePhoneLocation20240813,
            _SerializerBookingInputIntegrationLocation20240813,
            _SerializerBookingInputLinkLocation20240813,
            _SerializerBookingInputPhoneLocation20240813,
            _SerializerBookingInputOrganizersDefaultAppLocation20240813,
        ]
    ] = pydantic.Field(alias="location", default=None)
    meeting_url: typing.Optional[str] = pydantic.Field(alias="meetingUrl", default=None)
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    recurrence_count: typing.Optional[float] = pydantic.Field(
        alias="recurrenceCount", default=None
    )
    start: str = pydantic.Field(
        alias="start",
    )
