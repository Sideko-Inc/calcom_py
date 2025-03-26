import pydantic


class DeleteData20240614(pydantic.BaseModel):
    """
    DeleteData20240614
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: float = pydantic.Field(
        alias="id",
    )
    length_in_minutes: float = pydantic.Field(
        alias="lengthInMinutes",
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
    title: str = pydantic.Field(
        alias="title",
    )
