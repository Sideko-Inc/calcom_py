import pydantic
import typing_extensions


class BookingInputPhoneLocation20240813(typing_extensions.TypedDict):
    """
    BookingInputPhoneLocation20240813
    """

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `phone` - it refers to phone defined by the organizer.
    """


class _SerializerBookingInputPhoneLocation20240813(pydantic.BaseModel):
    """
    Serializer for BookingInputPhoneLocation20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_field: str = pydantic.Field(
        alias="type",
    )
