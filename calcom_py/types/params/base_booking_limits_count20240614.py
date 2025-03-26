import pydantic
import typing
import typing_extensions


class BaseBookingLimitsCount20240614(typing_extensions.TypedDict):
    """
    BaseBookingLimitsCount20240614
    """

    day: typing_extensions.NotRequired[float]
    """
    The number of bookings per day
    """

    disabled: typing_extensions.NotRequired[bool]

    month: typing_extensions.NotRequired[float]
    """
    The number of bookings per month
    """

    week: typing_extensions.NotRequired[float]
    """
    The number of bookings per week
    """

    year: typing_extensions.NotRequired[float]
    """
    The number of bookings per year
    """


class _SerializerBaseBookingLimitsCount20240614(pydantic.BaseModel):
    """
    Serializer for BaseBookingLimitsCount20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    day: typing.Optional[float] = pydantic.Field(alias="day", default=None)
    disabled: typing.Optional[bool] = pydantic.Field(alias="disabled", default=None)
    month: typing.Optional[float] = pydantic.Field(alias="month", default=None)
    week: typing.Optional[float] = pydantic.Field(alias="week", default=None)
    year: typing.Optional[float] = pydantic.Field(alias="year", default=None)
