import pydantic


class OptionOutput(pydantic.BaseModel):
    """
    OptionOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attribute_id: str = pydantic.Field(
        alias="attributeId",
    )
    """
    The ID of the attribute
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The ID of the option
    """
    slug: str = pydantic.Field(
        alias="slug",
    )
    """
    The slug of the option
    """
    value: str = pydantic.Field(
        alias="value",
    )
    """
    The value of the option
    """
