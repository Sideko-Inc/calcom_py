import pydantic
import typing


class OrgTeamOutputDto(pydantic.BaseModel):
    """
    OrgTeamOutputDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_icon_logo: typing.Optional[str] = pydantic.Field(
        alias="appIconLogo", default=None
    )
    app_logo: typing.Optional[str] = pydantic.Field(alias="appLogo", default=None)
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
    id: float = pydantic.Field(
        alias="id",
    )
    is_organization: bool = pydantic.Field(
        alias="isOrganization",
    )
    is_private: typing.Optional[bool] = pydantic.Field(alias="isPrivate", default=None)
    logo_url: typing.Optional[str] = pydantic.Field(alias="logoUrl", default=None)
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    parent_id: typing.Optional[float] = pydantic.Field(alias="parentId", default=None)
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    theme: typing.Optional[str] = pydantic.Field(alias="theme", default=None)
    time_format: typing.Optional[float] = pydantic.Field(
        alias="timeFormat", default=None
    )
    time_zone: typing.Optional[str] = pydantic.Field(alias="timeZone", default=None)
    week_start: typing.Optional[str] = pydantic.Field(alias="weekStart", default=None)
