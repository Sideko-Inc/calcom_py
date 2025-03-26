import pydantic
import typing
import typing_extensions


class RefreshApiKeyInput(typing_extensions.TypedDict):
    """
    RefreshApiKeyInput
    """

    api_key_days_valid: typing_extensions.NotRequired[float]
    """
    For how many days is managed organization api key valid. Defaults to 30 days.
    """

    api_key_never_expires: typing_extensions.NotRequired[bool]
    """
    If true, organization api key never expires.
    """


class _SerializerRefreshApiKeyInput(pydantic.BaseModel):
    """
    Serializer for RefreshApiKeyInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    api_key_days_valid: typing.Optional[float] = pydantic.Field(
        alias="apiKeyDaysValid", default=None
    )
    api_key_never_expires: typing.Optional[bool] = pydantic.Field(
        alias="apiKeyNeverExpires", default=None
    )
