import pydantic
import typing
import typing_extensions


class BaseBookingLimitsDuration20240614(typing_extensions.TypedDict):
    """
    BaseBookingLimitsDuration20240614
    """

    day: typing_extensions.NotRequired[float]
    """
    The duration of bookings per day (must be a multiple of 15)
    """

    month: typing_extensions.NotRequired[float]
    """
    The duration of bookings per month (must be a multiple of 15)
    """

    week: typing_extensions.NotRequired[float]
    """
    The duration of bookings per week (must be a multiple of 15)
    """

    year: typing_extensions.NotRequired[float]
    """
    The duration of bookings per year (must be a multiple of 15)
    """


class _SerializerBaseBookingLimitsDuration20240614(pydantic.BaseModel):
    """
    Serializer for BaseBookingLimitsDuration20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    day: typing.Optional[float] = pydantic.Field(alias="day", default=None)
    month: typing.Optional[float] = pydantic.Field(alias="month", default=None)
    week: typing.Optional[float] = pydantic.Field(alias="week", default=None)
    year: typing.Optional[float] = pydantic.Field(alias="year", default=None)
