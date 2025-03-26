import pydantic
import typing_extensions


class InputAddressLocation20240614(typing_extensions.TypedDict):
    """
    InputAddressLocation20240614
    """

    address: typing_extensions.Required[str]

    public: typing_extensions.Required[bool]

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `address`
    """


class _SerializerInputAddressLocation20240614(pydantic.BaseModel):
    """
    Serializer for InputAddressLocation20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: str = pydantic.Field(
        alias="address",
    )
    public: bool = pydantic.Field(
        alias="public",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
