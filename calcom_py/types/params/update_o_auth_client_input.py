import pydantic
import typing
import typing_extensions


class UpdateOAuthClientInput(typing_extensions.TypedDict):
    """
    UpdateOAuthClientInput
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

    name: typing_extensions.NotRequired[str]

    redirect_uris: typing_extensions.NotRequired[typing.List[str]]


class _SerializerUpdateOAuthClientInput(pydantic.BaseModel):
    """
    Serializer for UpdateOAuthClientInput handling case conversions
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
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    redirect_uris: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="redirectUris", default=None
    )
