import pydantic
import typing
import typing_extensions


class Attendee(pydantic.BaseModel):
    """
    Attendee
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The email of the attendee.
    """
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
    """
    The preferred language of the attendee. Used for booking confirmation.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The name of the attendee.
    """
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="phoneNumber", default=None
    )
    """
    The phone number of the attendee in international format.
    """
    time_zone: str = pydantic.Field(
        alias="timeZone",
    )
    """
    The time zone of the attendee.
    """
