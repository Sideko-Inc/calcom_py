import pydantic
import typing
import typing_extensions


class CancelBookingInput20240813(typing_extensions.TypedDict):
    """
    CancelBookingInput20240813
    """

    cancel_subsequent_bookings: typing_extensions.NotRequired[bool]
    """
    For recurring non-seated booking - if true, cancel booking with the bookingUid of the individual recurrence and all recurrences that come after it.
    """

    cancellation_reason: typing_extensions.NotRequired[str]


class _SerializerCancelBookingInput20240813(pydantic.BaseModel):
    """
    Serializer for CancelBookingInput20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cancel_subsequent_bookings: typing.Optional[bool] = pydantic.Field(
        alias="cancelSubsequentBookings", default=None
    )
    cancellation_reason: typing.Optional[str] = pydantic.Field(
        alias="cancellationReason", default=None
    )
