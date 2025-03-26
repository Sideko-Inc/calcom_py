import pydantic
import typing


class ConferencingAppsOutputDto(pydantic.BaseModel):
    """
    ConferencingAppsOutputDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: float = pydantic.Field(
        alias="id",
    )
    """
    Id of the conferencing app credentials
    """
    invalid: typing.Optional[bool] = pydantic.Field(alias="invalid", default=None)
    """
    Whether if the connection is working or not.
    """
    type_field: str = pydantic.Field(
        alias="type",
    )
    """
    Type of conferencing app
    """
    user_id: float = pydantic.Field(
        alias="userId",
    )
    """
    Id of the user associated to the conferencing app
    """
