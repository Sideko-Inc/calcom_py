import pydantic
import typing_extensions


class InputLinkLocation20240614(typing_extensions.TypedDict):
    """
    InputLinkLocation20240614
    """

    link: typing_extensions.Required[str]

    public: typing_extensions.Required[bool]

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `link`
    """


class _SerializerInputLinkLocation20240614(pydantic.BaseModel):
    """
    Serializer for InputLinkLocation20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    link: str = pydantic.Field(
        alias="link",
    )
    public: bool = pydantic.Field(
        alias="public",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
