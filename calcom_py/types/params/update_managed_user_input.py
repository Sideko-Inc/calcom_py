import pydantic
import typing
import typing_extensions


class UpdateManagedUserInput(typing_extensions.TypedDict):
    """
    UpdateManagedUserInput
    """

    avatar_url: typing_extensions.NotRequired[str]
    """
    URL of the user's avatar image
    """

    default_schedule_id: typing_extensions.NotRequired[float]

    email_field: typing_extensions.NotRequired[str]

    locale_field: typing_extensions.NotRequired[
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

    name: typing_extensions.NotRequired[str]

    time_format: typing_extensions.NotRequired[float]
    """
    Must be 12 or 24
    """

    time_zone: typing_extensions.NotRequired[str]

    week_start: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
        ]
    ]


class _SerializerUpdateManagedUserInput(pydantic.BaseModel):
    """
    Serializer for UpdateManagedUserInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    avatar_url: typing.Optional[str] = pydantic.Field(alias="avatarUrl", default=None)
    default_schedule_id: typing.Optional[float] = pydantic.Field(
        alias="defaultScheduleId", default=None
    )
    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    locale_field: typing.Optional[
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
    ] = pydantic.Field(alias="locale", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    time_format: typing.Optional[float] = pydantic.Field(
        alias="timeFormat", default=None
    )
    time_zone: typing.Optional[str] = pydantic.Field(alias="timeZone", default=None)
    week_start: typing.Optional[
        typing_extensions.Literal[
            "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
        ]
    ] = pydantic.Field(alias="weekStart", default=None)
