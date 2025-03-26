import pydantic
import typing_extensions


class OutputPhoneLocation20240614(pydantic.BaseModel):
    """
    OutputPhoneLocation20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    phone: str = pydantic.Field(
        alias="phone",
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
    only allowed value for type is `phone`
    """
