import pydantic
import typing
import typing_extensions


class CreateTeamInput(typing_extensions.TypedDict):
    """
    CreateTeamInput
    """

    app_icon_logo: typing_extensions.NotRequired[str]

    app_logo: typing_extensions.NotRequired[str]

    auto_accept_creator: typing_extensions.NotRequired[bool]

    banner_url: typing_extensions.NotRequired[str]
    """
    URL of the teams banner image which is shown on booker
    """

    bio: typing_extensions.NotRequired[str]

    brand_color: typing_extensions.NotRequired[str]

    cal_video_logo: typing_extensions.NotRequired[str]

    dark_brand_color: typing_extensions.NotRequired[str]

    hide_book_a_team_member: typing_extensions.NotRequired[bool]

    hide_branding: typing_extensions.NotRequired[bool]

    is_private: typing_extensions.NotRequired[bool]

    logo_url: typing_extensions.NotRequired[str]
    """
    URL of the teams logo image
    """

    metadata: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    You can store any additional data you want here.
    Metadata must have at most 50 keys, each key up to 40 characters.
    Values can be strings (up to 500 characters), numbers, or booleans.
    """

    name: typing_extensions.Required[str]
    """
    Name of the team
    """

    slug: typing_extensions.NotRequired[str]
    """
    Team slug
    """

    theme: typing_extensions.NotRequired[str]

    time_format: typing_extensions.NotRequired[float]

    time_zone: typing_extensions.NotRequired[str]
    """
    Timezone is used to create teams's default schedule from Monday to Friday from 9AM to 5PM. It will default to Europe/London if not passed.
    """

    week_start: typing_extensions.NotRequired[str]


class _SerializerCreateTeamInput(pydantic.BaseModel):
    """
    Serializer for CreateTeamInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_icon_logo: typing.Optional[str] = pydantic.Field(
        alias="appIconLogo", default=None
    )
    app_logo: typing.Optional[str] = pydantic.Field(alias="appLogo", default=None)
    auto_accept_creator: typing.Optional[bool] = pydantic.Field(
        alias="autoAcceptCreator", default=None
    )
    banner_url: typing.Optional[str] = pydantic.Field(alias="bannerUrl", default=None)
    bio: typing.Optional[str] = pydantic.Field(alias="bio", default=None)
    brand_color: typing.Optional[str] = pydantic.Field(alias="brandColor", default=None)
    cal_video_logo: typing.Optional[str] = pydantic.Field(
        alias="calVideoLogo", default=None
    )
    dark_brand_color: typing.Optional[str] = pydantic.Field(
        alias="darkBrandColor", default=None
    )
    hide_book_a_team_member: typing.Optional[bool] = pydantic.Field(
        alias="hideBookATeamMember", default=None
    )
    hide_branding: typing.Optional[bool] = pydantic.Field(
        alias="hideBranding", default=None
    )
    is_private: typing.Optional[bool] = pydantic.Field(alias="isPrivate", default=None)
    logo_url: typing.Optional[str] = pydantic.Field(alias="logoUrl", default=None)
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    theme: typing.Optional[str] = pydantic.Field(alias="theme", default=None)
    time_format: typing.Optional[float] = pydantic.Field(
        alias="timeFormat", default=None
    )
    time_zone: typing.Optional[str] = pydantic.Field(alias="timeZone", default=None)
    week_start: typing.Optional[str] = pydantic.Field(alias="weekStart", default=None)
