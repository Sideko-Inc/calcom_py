import pydantic
import typing
import typing_extensions


class Attendee(typing_extensions.TypedDict):
    """
    Attendee
    """

    email_field: typing_extensions.NotRequired[str]
    """
    The email of the attendee.
    """

    language: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "ar",
            "az",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "es-419",
            "et",
            "eu",
            "fi",
            "fr",
            "he",
            "hr",
            "hu",
            "id",
            "it",
            "iw",
            "ja",
            "km",
            "ko",
            "lv",
            "nl",
            "no",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sr",
            "sv",
            "ta",
            "th",
            "tr",
            "uk",
            "vi",
            "zh-CN",
            "zh-TW",
        ]
    ]
    """
    The preferred language of the attendee. Used for booking confirmation.
    """

    name: typing_extensions.Required[str]
    """
    The name of the attendee.
    """

    phone_number: typing_extensions.NotRequired[str]
    """
    The phone number of the attendee in international format.
    """

    time_zone: typing_extensions.Required[str]
    """
    The time zone of the attendee.
    """


class _SerializerAttendee(pydantic.BaseModel):
    """
    Serializer for Attendee handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    language: typing.Optional[
        typing_extensions.Literal[
            "ar",
            "az",
            "bg",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "es-419",
            "et",
            "eu",
            "fi",
            "fr",
            "he",
            "hr",
            "hu",
            "id",
            "it",
            "iw",
            "ja",
            "km",
            "ko",
            "lv",
            "nl",
            "no",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sr",
            "sv",
            "ta",
            "th",
            "tr",
            "uk",
            "vi",
            "zh-CN",
            "zh-TW",
        ]
    ] = pydantic.Field(alias="language", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="phoneNumber", default=None
    )
    time_zone: str = pydantic.Field(
        alias="timeZone",
    )
