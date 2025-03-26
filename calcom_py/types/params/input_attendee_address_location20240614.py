import pydantic
import typing_extensions


class InputAttendeeAddressLocation20240614(typing_extensions.TypedDict):
    """
    InputAttendeeAddressLocation20240614
    """

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `attendeeAddress`
    """


class _SerializerInputAttendeeAddressLocation20240614(pydantic.BaseModel):
    """
    Serializer for InputAttendeeAddressLocation20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_field: str = pydantic.Field(
        alias="type",
    )
