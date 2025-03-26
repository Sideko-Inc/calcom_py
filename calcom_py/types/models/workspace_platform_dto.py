import pydantic


class WorkspacePlatformDto(pydantic.BaseModel):
    """
    WorkspacePlatformDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: str = pydantic.Field(
        alias="name",
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
