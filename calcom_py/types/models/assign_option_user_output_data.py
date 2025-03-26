import pydantic


class AssignOptionUserOutputData(pydantic.BaseModel):
    """
    AssignOptionUserOutputData
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attribute_option_id: str = pydantic.Field(
        alias="attributeOptionId",
    )
    """
    The value of the option
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The ID of the option assigned to the user
    """
    member_id: float = pydantic.Field(
        alias="memberId",
    )
    """
    The ID form the org membership for the user
    """
