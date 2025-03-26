import pydantic
import typing_extensions


class BookingInputAttendeePhoneLocation20240813(typing_extensions.TypedDict):
    """
    BookingInputAttendeePhoneLocation20240813
    """

    phone: typing_extensions.Required[str]

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `attendeePhone`
    """


class _SerializerBookingInputAttendeePhoneLocation20240813(pydantic.BaseModel):
    """
    Serializer for BookingInputAttendeePhoneLocation20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    phone: str = pydantic.Field(
        alias="phone",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
