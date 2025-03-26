import pydantic
import typing
import typing_extensions

from .booking_output20240813 import BookingOutput20240813
from .get_recurring_seated_booking_output20240813 import (
    GetRecurringSeatedBookingOutput20240813,
)
from .get_seated_booking_output20240813 import GetSeatedBookingOutput20240813
from .recurring_booking_output20240813 import RecurringBookingOutput20240813


class CancelBookingOutput20240813(pydantic.BaseModel):
    """
    CancelBookingOutput20240813
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Union[
        BookingOutput20240813,
        RecurringBookingOutput20240813,
        typing.List[RecurringBookingOutput20240813],
        GetSeatedBookingOutput20240813,
        GetRecurringSeatedBookingOutput20240813,
        typing.List[GetRecurringSeatedBookingOutput20240813],
    ] = pydantic.Field(
        alias="data",
    )
    """
    Booking data, which can be either a BookingOutput object, a RecurringBookingOutput object, or an array of RecurringBookingOutput objects
    """
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
