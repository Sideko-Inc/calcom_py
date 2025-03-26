import pydantic
import typing
import typing_extensions


class CreateOAuthClientInput(typing_extensions.TypedDict):
    """
    CreateOAuthClientInput
    """

    are_default_event_types_enabled: typing_extensions.NotRequired[bool]
    """
    If true, when creating a managed user the managed user will have 4 default event types: 30 and 60 minutes without Cal video, 30 and 60 minutes with Cal video. Set this as false if you want to create a managed user and then manually create event types for the user.
    """

    are_emails_enabled: typing_extensions.NotRequired[bool]

    booking_cancel_redirect_uri: typing_extensions.NotRequired[str]

    booking_redirect_uri: typing_extensions.NotRequired[str]

    booking_reschedule_redirect_uri: typing_extensions.NotRequired[str]

    logo: typing_extensions.NotRequired[str]

    name: typing_extensions.Required[str]

    permissions: typing_extensions.Required[
        typing.List[
            typing_extensions.Literal[
                "*",
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
        ]
    ]
    """
    Array of permission keys like ["BOOKING_READ", "BOOKING_WRITE"]. Use ["*"] to grant all permissions.
    """

    redirect_uris: typing_extensions.Required[typing.List[str]]


class _SerializerCreateOAuthClientInput(pydantic.BaseModel):
    """
    Serializer for CreateOAuthClientInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    are_default_event_types_enabled: typing.Optional[bool] = pydantic.Field(
        alias="areDefaultEventTypesEnabled", default=None
    )
    are_emails_enabled: typing.Optional[bool] = pydantic.Field(
        alias="areEmailsEnabled", default=None
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
    logo: typing.Optional[str] = pydantic.Field(alias="logo", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    permissions: typing.List[
        typing_extensions.Literal[
            "*",
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
    redirect_uris: typing.List[str] = pydantic.Field(
        alias="redirectUris",
    )
