import pydantic
import typing
import typing_extensions


class ManagedUserOutput(pydantic.BaseModel):
    """
    ManagedUserOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    avatar_url: typing.Optional[str] = pydantic.Field(alias="avatarUrl", default=None)
    """
    URL of the user's avatar image
    """
    created_date: str = pydantic.Field(
        alias="createdDate",
    )
    default_schedule_id: typing.Optional[float] = pydantic.Field(
        alias="defaultScheduleId",
    )
    email_field: str = pydantic.Field(
        alias="email",
    )
    id: float = pydantic.Field(
        alias="id",
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
    name: typing.Optional[str] = pydantic.Field(
        alias="name",
    )
    time_format: typing.Optional[float] = pydantic.Field(
        alias="timeFormat",
    )
    time_zone: str = pydantic.Field(
        alias="timeZone",
    )
    username: typing.Optional[str] = pydantic.Field(
        alias="username",
    )
    week_start: str = pydantic.Field(
        alias="weekStart",
    )
