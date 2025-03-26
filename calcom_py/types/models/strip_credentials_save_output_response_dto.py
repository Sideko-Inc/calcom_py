import pydantic


class StripCredentialsSaveOutputResponseDto(pydantic.BaseModel):
    """
    StripCredentialsSaveOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    url: str = pydantic.Field(
        alias="url",
    )
