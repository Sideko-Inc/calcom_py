import pydantic
import typing_extensions


class RefreshTokenInput(typing_extensions.TypedDict):
    """
    RefreshTokenInput
    """

    refresh_token: typing_extensions.Required[str]
    """
    Managed user's refresh token.
    """


class _SerializerRefreshTokenInput(pydantic.BaseModel):
    """
    Serializer for RefreshTokenInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    refresh_token: str = pydantic.Field(
        alias="refreshToken",
    )
