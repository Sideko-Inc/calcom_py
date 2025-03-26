import pydantic
import typing_extensions


class OutputLinkLocation20240614(pydantic.BaseModel):
    """
    OutputLinkLocation20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    link: str = pydantic.Field(
        alias="link",
    )
    public: bool = pydantic.Field(
        alias="public",
    )
    type_field: typing_extensions.Literal[
        "address",
        "attendeeAddress",
        "attendeeDefined",
        "attendeePhone",
        "integration",
        "link",
        "organizersDefaultApp",
        "phone",
    ] = pydantic.Field(
        alias="type",
    )
    """
    only allowed value for type is `link`
    """
