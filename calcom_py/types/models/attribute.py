import pydantic
import typing
import typing_extensions


class Attribute(pydantic.BaseModel):
    """
    Attribute
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether the attribute is enabled and displayed on their profile
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The ID of the attribute
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The name of the attribute
    """
    slug: str = pydantic.Field(
        alias="slug",
    )
    """
    The slug of the attribute
    """
    team_id: float = pydantic.Field(
        alias="teamId",
    )
    """
    The team ID associated with the attribute
    """
    type_field: typing_extensions.Literal[
        "MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of the attribute
    """
    users_can_edit_relation: typing.Optional[bool] = pydantic.Field(
        alias="usersCanEditRelation", default=None
    )
    """
    Whether users can edit the relation
    """
