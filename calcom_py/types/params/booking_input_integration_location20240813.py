import pydantic
import typing_extensions


class BookingInputIntegrationLocation20240813(typing_extensions.TypedDict):
    """
    BookingInputIntegrationLocation20240813
    """

    integration: typing_extensions.Required[
        typing_extensions.Literal[
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
        ]
    ]

    type_field: typing_extensions.Required[str]
    """
    only allowed value for type is `integration`
    """


class _SerializerBookingInputIntegrationLocation20240813(pydantic.BaseModel):
    """
    Serializer for BookingInputIntegrationLocation20240813 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

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
    type_field: str = pydantic.Field(
        alias="type",
    )
