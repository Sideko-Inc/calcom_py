import pydantic
import typing_extensions


class Seats20240614(typing_extensions.TypedDict):
    """
    Seats20240614
    """

    seats_per_time_slot: typing_extensions.Required[float]
    """
    Number of seats available per time slot
    """

    show_attendee_info: typing_extensions.Required[bool]
    """
    Show attendee information to other guests
    """

    show_availability_count: typing_extensions.Required[bool]
    """
    Display the count of available seats
    """


class _SerializerSeats20240614(pydantic.BaseModel):
    """
    Serializer for Seats20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    seats_per_time_slot: float = pydantic.Field(
        alias="seatsPerTimeSlot",
    )
    show_attendee_info: bool = pydantic.Field(
        alias="showAttendeeInfo",
    )
    show_availability_count: bool = pydantic.Field(
        alias="showAvailabilityCount",
    )
