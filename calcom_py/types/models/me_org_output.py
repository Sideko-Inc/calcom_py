import pydantic


class MeOrgOutput(pydantic.BaseModel):
    """
    MeOrgOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: float = pydantic.Field(
        alias="id",
    )
    is_platform: bool = pydantic.Field(
        alias="isPlatform",
    )
