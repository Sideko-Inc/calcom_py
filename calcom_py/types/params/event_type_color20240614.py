import pydantic
import typing_extensions


class EventTypeColor20240614(typing_extensions.TypedDict):
    """
    EventTypeColor20240614
    """

    dark_theme_hex: typing_extensions.Required[str]
    """
    Color used for event types in dark theme
    """

    light_theme_hex: typing_extensions.Required[str]
    """
    Color used for event types in light theme
    """


class _SerializerEventTypeColor20240614(pydantic.BaseModel):
    """
    Serializer for EventTypeColor20240614 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dark_theme_hex: str = pydantic.Field(
        alias="darkThemeHex",
    )
    light_theme_hex: str = pydantic.Field(
        alias="lightThemeHex",
    )
