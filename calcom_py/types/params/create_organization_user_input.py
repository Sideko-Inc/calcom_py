import pydantic
import typing
import typing_extensions


class CreateOrganizationUserInput(typing_extensions.TypedDict):
    """
    CreateOrganizationUserInput
    """

    app_theme: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Application theme
    """

    auto_accept: typing_extensions.NotRequired[bool]

    avatar_url: typing_extensions.NotRequired[str]
    """
    Avatar URL
    """

    brand_color: typing_extensions.NotRequired[str]
    """
    Brand color in HEX format
    """

    dark_brand_color: typing_extensions.NotRequired[str]
    """
    Dark brand color in HEX format
    """

    default_schedule_id: typing_extensions.NotRequired[float]
    """
    Default schedule ID
    """

    email_field: typing_extensions.Required[str]
    """
    User email address
    """

    hide_branding: typing_extensions.NotRequired[bool]
    """
    Hide branding
    """

    locale_field: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Locale
    """

    organization_role: typing_extensions.NotRequired[
        typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
    ]

    theme: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Theme
    """

    time_format: typing_extensions.NotRequired[float]
    """
    Time format
    """

    time_zone: typing_extensions.NotRequired[str]
    """
    Time zone
    """

    username: typing_extensions.NotRequired[str]
    """
    Username
    """

    weekday: typing_extensions.NotRequired[str]
    """
    Preferred weekday
    """


class _SerializerCreateOrganizationUserInput(pydantic.BaseModel):
    """
    Serializer for CreateOrganizationUserInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_theme: typing.Optional[str] = pydantic.Field(alias="appTheme", default=None)
    auto_accept: typing.Optional[bool] = pydantic.Field(
        alias="autoAccept", default=None
    )
    avatar_url: typing.Optional[str] = pydantic.Field(alias="avatarUrl", default=None)
    brand_color: typing.Optional[str] = pydantic.Field(alias="brandColor", default=None)
    dark_brand_color: typing.Optional[str] = pydantic.Field(
        alias="darkBrandColor", default=None
    )
    default_schedule_id: typing.Optional[float] = pydantic.Field(
        alias="defaultScheduleId", default=None
    )
    email_field: str = pydantic.Field(
        alias="email",
    )
    hide_branding: typing.Optional[bool] = pydantic.Field(
        alias="hideBranding", default=None
    )
    locale_field: typing.Optional[str] = pydantic.Field(alias="locale", default=None)
    organization_role: typing.Optional[
        typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
    ] = pydantic.Field(alias="organizationRole", default=None)
    theme: typing.Optional[str] = pydantic.Field(alias="theme", default=None)
    time_format: typing.Optional[float] = pydantic.Field(
        alias="timeFormat", default=None
    )
    time_zone: typing.Optional[str] = pydantic.Field(alias="timeZone", default=None)
    username: typing.Optional[str] = pydantic.Field(alias="username", default=None)
    weekday: typing.Optional[str] = pydantic.Field(alias="weekday", default=None)
