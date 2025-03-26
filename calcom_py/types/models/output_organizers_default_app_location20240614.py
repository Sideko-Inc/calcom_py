import pydantic
import typing_extensions


class OutputOrganizersDefaultAppLocation20240614(pydantic.BaseModel):
    """
    OutputOrganizersDefaultAppLocation20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
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
    only allowed value for type is `organizersDefaultApp`
    """
