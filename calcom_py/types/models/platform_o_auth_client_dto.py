import pydantic
import typing
import typing_extensions


class PlatformOAuthClientDto(pydantic.BaseModel):
    """
    PlatformOAuthClientDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    are_default_event_types_enabled: bool = pydantic.Field(
        alias="areDefaultEventTypesEnabled",
    )
    """
    If enabled, when creating a managed user the managed user will have 4 default event types: 30 and 60 minutes without Cal video, 30 and 60 minutes with Cal video. Leave this disabled if you want to create a managed user and then manually create event types for the user.
    """
    are_emails_enabled: bool = pydantic.Field(
        alias="areEmailsEnabled",
    )
    booking_cancel_redirect_uri: typing.Optional[str] = pydantic.Field(
        alias="bookingCancelRedirectUri", default=None
    )
    booking_redirect_uri: typing.Optional[str] = pydantic.Field(
        alias="bookingRedirectUri", default=None
    )
    booking_reschedule_redirect_uri: typing.Optional[str] = pydantic.Field(
        alias="bookingRescheduleRedirectUri", default=None
    )
    created_at: str = pydantic.Field(
        alias="createdAt",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    logo: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="logo", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    organization_id: float = pydantic.Field(
        alias="organizationId",
    )
    permissions: typing.List[
        typing_extensions.Literal[
            "APPS_READ",
            "APPS_WRITE",
            "BOOKING_READ",
            "BOOKING_WRITE",
            "EVENT_TYPE_READ",
            "EVENT_TYPE_WRITE",
            "PROFILE_READ",
            "PROFILE_WRITE",
            "SCHEDULE_READ",
            "SCHEDULE_WRITE",
        ]
    ] = pydantic.Field(
        alias="permissions",
    )
    """
    Array of permission keys like ["BOOKING_READ", "BOOKING_WRITE"]
    """
    redirect_uris: typing.List[str] = pydantic.Field(
        alias="redirectUris",
    )
    secret: str = pydantic.Field(
        alias="secret",
    )
