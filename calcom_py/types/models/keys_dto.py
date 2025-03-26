import pydantic


class KeysDto(pydantic.BaseModel):
    """
    KeysDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    access_token: str = pydantic.Field(
        alias="accessToken",
    )
    access_token_expires_at: float = pydantic.Field(
        alias="accessTokenExpiresAt",
    )
    refresh_token: str = pydantic.Field(
        alias="refreshToken",
    )
