import pydantic
import typing
import typing_extensions


class RescheduleBookingInput20240813(typing_extensions.TypedDict):
    """
    RescheduleBookingInput20240813
    """

    rescheduled_by: typing_extensions.NotRequired[str]
    """
    Email of the person who is rescheduling the booking - only needed when rescheduling a booking that requires a confirmation.
    If event type owner email is provided then rescheduled booking will be automatically confirmed. If attendee email or no email is passed then the event type
    owner will have to confirm the rescheduled booking.
    """

    rescheduling_reason: typing_extensions.NotRequired[str]
    """
    Reason for rescheduling the booking
    """

    start: typing_extensions.Required[str]
    """
    Start time in ISO 8601 format for the new booking
    """


class _SerializerRescheduleBookingInput20240813(pydantic.BaseModel):
    """
    Serializer for RescheduleBookingInput20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    rescheduled_by: typing.Optional[str] = pydantic.Field(
        alias="rescheduledBy", default=None
    )
    rescheduling_reason: typing.Optional[str] = pydantic.Field(
        alias="reschedulingReason", default=None
    )
    start: str = pydantic.Field(
        alias="start",
    )
