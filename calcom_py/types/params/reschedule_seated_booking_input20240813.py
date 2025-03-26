import pydantic
import typing
import typing_extensions


class RescheduleSeatedBookingInput20240813(typing_extensions.TypedDict):
    """
    RescheduleSeatedBookingInput20240813
    """

    rescheduled_by: typing_extensions.NotRequired[str]
    """
    Email of the person who is rescheduling the booking - only needed when rescheduling a booking that requires a confirmation.
    If event type owner email is provided then rescheduled booking will be automatically confirmed. If attendee email or no email is passed then the event type
    owner will have to confirm the rescheduled booking.
    """

    seat_uid: typing_extensions.Required[str]
    """
    Uid of the specific seat within booking.
    """

    start: typing_extensions.Required[str]
    """
    Start time in ISO 8601 format for the new booking
    """


class _SerializerRescheduleSeatedBookingInput20240813(pydantic.BaseModel):
    """
    Serializer for RescheduleSeatedBookingInput20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    rescheduled_by: typing.Optional[str] = pydantic.Field(
        alias="rescheduledBy", default=None
    )
    seat_uid: str = pydantic.Field(
        alias="seatUid",
    )
    start: str = pydantic.Field(
        alias="start",
    )
