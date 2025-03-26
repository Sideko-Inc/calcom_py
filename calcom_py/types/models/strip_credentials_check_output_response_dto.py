import pydantic


class StripCredentialsCheckOutputResponseDto(pydantic.BaseModel):
    """
    StripCredentialsCheckOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: str = pydantic.Field(
        alias="status",
    )
