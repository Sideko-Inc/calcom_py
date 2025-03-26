import pydantic


class Seats20240614(pydantic.BaseModel):
    """
    Seats20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    seats_per_time_slot: float = pydantic.Field(
        alias="seatsPerTimeSlot",
    )
    """
    Number of seats available per time slot
    """
    show_attendee_info: bool = pydantic.Field(
        alias="showAttendeeInfo",
    )
    """
    Show attendee information to other guests
    """
    show_availability_count: bool = pydantic.Field(
        alias="showAvailabilityCount",
    )
    """
    Display the count of available seats
    """
