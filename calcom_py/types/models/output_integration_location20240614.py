import pydantic
import typing
import typing_extensions


class OutputIntegrationLocation20240614(pydantic.BaseModel):
    """
    OutputIntegrationLocation20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credential_id: typing.Optional[float] = pydantic.Field(
        alias="credentialId", default=None
    )
    """
    Credential ID associated with the integration
    """
    integration: typing_extensions.Literal[
        "around-video",
        "cal-video",
        "campfire-video",
        "demodesk-video",
        "discord-video",
        "eightxeight-video",
        "element-call-video",
        "facetime-video",
        "google-meet",
        "huddle",
        "jelly-conferencing",
        "jelly-video",
        "jitsi",
        "mirotalk-video",
        "office365-video",
        "ping-video",
        "riverside-video",
        "roam-video",
        "salesroom-video",
        "shimmer-video",
        "signal-video",
        "sirius-video",
        "skype-video",
        "sylaps-video",
        "tandem",
        "telegram-video",
        "webex-video",
        "whatsapp-video",
        "whereby-video",
        "zoom",
    ] = pydantic.Field(
        alias="integration",
    )
    link: typing.Optional[str] = pydantic.Field(alias="link", default=None)
    type_field: typing_extensions.Literal[
        "address",
        "attendeeAddress",
        "attendeeDefined",
        "attendeePhone",
        "conferencing",
        "integration",
        "link",
        "organizersDefaultApp",
        "phone",
        "unknown",
    ] = pydantic.Field(
        alias="type",
    )
    """
    Only allowed value for type is `integration`
    """
