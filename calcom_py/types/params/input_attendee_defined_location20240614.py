import pydantic
import typing_extensions


class InputAttendeeDefinedLocation20240614(typing_extensions.TypedDict):
    """
    InputAttendeeDefinedLocation20240614
    """

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `attendeeDefined`
    """


class _SerializerInputAttendeeDefinedLocation20240614(pydantic.BaseModel):
    """
    Serializer for InputAttendeeDefinedLocation20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_field: str = pydantic.Field(
        alias="type",
    )
