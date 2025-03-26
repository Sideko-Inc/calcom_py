import pydantic
import typing_extensions


class Disabled20240614(typing_extensions.TypedDict):
    """
    Disabled20240614
    """

    disabled: typing_extensions.Required[bool]
    """
    Indicates if the option is disabled
    """


class _SerializerDisabled20240614(pydantic.BaseModel):
    """
    Serializer for Disabled20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    disabled: bool = pydantic.Field(
        alias="disabled",
    )
