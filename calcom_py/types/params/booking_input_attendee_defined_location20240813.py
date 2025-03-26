import pydantic
import typing_extensions


class BookingInputAttendeeDefinedLocation20240813(typing_extensions.TypedDict):
    """
    BookingInputAttendeeDefinedLocation20240813
    """

    location: typing_extensions.Required[str]

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `attendeeDefined`
    """


class _SerializerBookingInputAttendeeDefinedLocation20240813(pydantic.BaseModel):
    """
    Serializer for BookingInputAttendeeDefinedLocation20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    location: str = pydantic.Field(
        alias="location",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
