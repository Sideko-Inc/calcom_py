import pydantic
import typing_extensions


class OutputUnknownLocation20240614(pydantic.BaseModel):
    """
    OutputUnknownLocation20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    location: str = pydantic.Field(
        alias="location",
    )
    type_field: typing_extensions.Literal[
        "address",
        "attendeeAddress",
        "attendeeDefined",
        "attendeePhone",
        "conferencing",
        "integration",
        "link",
        "organizersDefaultApp",
        "phone",
        "unknown",
    ] = pydantic.Field(
        alias="type",
    )
    """
    only allowed value for type is `unknown`
    """
