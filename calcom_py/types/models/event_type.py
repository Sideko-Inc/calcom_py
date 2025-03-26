import pydantic


class EventType(pydantic.BaseModel):
    """
    EventType
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: float = pydantic.Field(
        alias="id",
    )
    slug: str = pydantic.Field(
        alias="slug",
    )
