import pydantic
import typing_extensions


class InputIntegrationLocation20240614(typing_extensions.TypedDict):
    """
    InputIntegrationLocation20240614
    """

    integration: typing_extensions.Required[
        typing_extensions.Literal["cal-video", "google-meet", "office365-video", "zoom"]
    ]

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `integration`
    """


class _SerializerInputIntegrationLocation20240614(pydantic.BaseModel):
    """
    Serializer for InputIntegrationLocation20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    integration: typing_extensions.Literal[
        "cal-video", "google-meet", "office365-video", "zoom"
    ] = pydantic.Field(
        alias="integration",
    )
    type_field: str = pydantic.Field(
        alias="type",
    )
