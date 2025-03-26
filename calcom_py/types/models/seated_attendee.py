import pydantic
import typing
import typing_extensions


class SeatedAttendee(pydantic.BaseModel):
    """
    SeatedAttendee
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    absent: bool = pydantic.Field(
        alias="absent",
    )
    booking_fields_responses: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="bookingFieldsResponses",
    )
    """
    Booking field responses consisting of an object with booking field slug as keys and user response as values.
    """
    email_field: str = pydantic.Field(
        alias="email",
    )
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
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="phoneNumber", default=None
    )
    seat_uid: str = pydantic.Field(
        alias="seatUid",
    )
    time_zone: str = pydantic.Field(
        alias="timeZone",
    )
