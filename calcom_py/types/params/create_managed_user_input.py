import pydantic
import typing
import typing_extensions


class CreateManagedUserInput(typing_extensions.TypedDict):
    """
    CreateManagedUserInput
    """

    avatar_url: typing_extensions.NotRequired[str]
    """
    URL of the user's avatar image
    """

    email_field: typing_extensions.Required[str]

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

    name: typing_extensions.Required[str]
    """
    Managed user's name is used in emails
    """

    time_format: typing_extensions.NotRequired[float]
    """
    Must be a number 12 or 24
    """

    time_zone: typing_extensions.NotRequired[str]
    """
    Timezone is used to create user's default schedule from Monday to Friday from 9AM to 5PM. If it is not passed then user does not have
          a default schedule and it must be created manually via the /schedules endpoint. Until the schedule is created, the user can't access availability atom to set his / her availability nor booked.
          It will default to Europe/London if not passed.
    """

    week_start: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
        ]
    ]


class _SerializerCreateManagedUserInput(pydantic.BaseModel):
    """
    Serializer for CreateManagedUserInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    avatar_url: typing.Optional[str] = pydantic.Field(alias="avatarUrl", default=None)
    email_field: str = pydantic.Field(
        alias="email",
    )
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
    name: str = pydantic.Field(
        alias="name",
    )
    time_format: typing.Optional[float] = pydantic.Field(
        alias="timeFormat", default=None
    )
    time_zone: typing.Optional[str] = pydantic.Field(alias="timeZone", default=None)
    week_start: typing.Optional[
        typing_extensions.Literal[
            "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
        ]
    ] = pydantic.Field(alias="weekStart", default=None)
