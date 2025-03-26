import pydantic
import typing_extensions


class InputPhoneLocation20240614(typing_extensions.TypedDict):
    """
    InputPhoneLocation20240614
    """

    phone: typing_extensions.Required[str]

    public: typing_extensions.Required[bool]

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `phone`
    """


class _SerializerInputPhoneLocation20240614(pydantic.BaseModel):
    """
    Serializer for InputPhoneLocation20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    phone: str = pydantic.Field(
        alias="phone",
    )
    public: bool = pydantic.Field(
        alias="public",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
