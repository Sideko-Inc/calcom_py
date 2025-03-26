import pydantic
import typing

from .profile_output import ProfileOutput


class GetOrgUsersWithProfileOutput(pydantic.BaseModel):
    """
    GetOrgUsersWithProfileOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allow_dynamic_booking: typing.Optional[bool] = pydantic.Field(
        alias="allowDynamicBooking", default=None
    )
    """
    Whether dynamic booking is allowed for the user
    """
    app_theme: typing.Optional[str] = pydantic.Field(alias="appTheme", default=None)
    """
    The app theme of the user
    """
    avatar_url: typing.Optional[str] = pydantic.Field(alias="avatarUrl", default=None)
    """
    The URL of the user's avatar
    """
    bio: typing.Optional[str] = pydantic.Field(alias="bio", default=None)
    """
    The bio of the user
    """
    brand_color: typing.Optional[str] = pydantic.Field(alias="brandColor", default=None)
    """
    The brand color of the user
    """
    created_date: str = pydantic.Field(
        alias="createdDate",
    )
    """
    The date when the user was created
    """
    dark_brand_color: typing.Optional[str] = pydantic.Field(
        alias="darkBrandColor", default=None
    )
    """
    The dark brand color of the user
    """
    default_schedule_id: typing.Optional[float] = pydantic.Field(
        alias="defaultScheduleId", default=None
    )
    """
    The ID of the default schedule for the user
    """
    email_field: str = pydantic.Field(
        alias="email",
    )
    """
    The email of the user
    """
    email_verified: typing.Optional[str] = pydantic.Field(
        alias="emailVerified", default=None
    )
    """
    The date when the email was verified
    """
    hide_branding: bool = pydantic.Field(
        alias="hideBranding",
    )
    """
    Whether to hide branding for the user
    """
    id: float = pydantic.Field(
        alias="id",
    )
    """
    The ID of the user
    """
    invited_to: typing.Optional[float] = pydantic.Field(alias="invitedTo", default=None)
    """
    The ID of the user who invited this user
    """
    locale_field: typing.Optional[str] = pydantic.Field(alias="locale", default=None)
    """
    The locale of the user
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The name of the user
    """
    profile_field: ProfileOutput = pydantic.Field(
        alias="profile",
    )
    theme: typing.Optional[str] = pydantic.Field(alias="theme", default=None)
    """
    The theme of the user
    """
    time_format: typing.Optional[float] = pydantic.Field(
        alias="timeFormat", default=None
    )
    """
    The time format of the user
    """
    time_zone: str = pydantic.Field(
        alias="timeZone",
    )
    """
    The time zone of the user
    """
    username: typing.Optional[str] = pydantic.Field(alias="username", default=None)
    """
    The username of the user
    """
    verified: typing.Optional[bool] = pydantic.Field(alias="verified", default=None)
    """
    Whether the user is verified
    """
    week_start: str = pydantic.Field(
        alias="weekStart",
    )
    """
    The week start day of the user
    """
