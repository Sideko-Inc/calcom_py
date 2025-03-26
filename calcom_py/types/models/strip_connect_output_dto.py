import pydantic


class StripConnectOutputDto(pydantic.BaseModel):
    """
    StripConnectOutputDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    auth_url: str = pydantic.Field(
        alias="authUrl",
    )
