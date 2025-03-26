import pydantic


class EventTypeColor20240614(pydantic.BaseModel):
    """
    EventTypeColor20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    dark_theme_hex: str = pydantic.Field(
        alias="darkThemeHex",
    )
    """
    Color used for event types in dark theme
    """
    light_theme_hex: str = pydantic.Field(
        alias="lightThemeHex",
    )
    """
    Color used for event types in light theme
    """
