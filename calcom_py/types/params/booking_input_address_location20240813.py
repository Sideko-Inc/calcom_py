import pydantic
import typing_extensions


class BookingInputAddressLocation20240813(typing_extensions.TypedDict):
    """
    BookingInputAddressLocation20240813
    """

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `address` - it refers to address defined by the organizer.
    """


class _SerializerBookingInputAddressLocation20240813(pydantic.BaseModel):
    """
    Serializer for BookingInputAddressLocation20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_field: str = pydantic.Field(
        alias="type",
    )
