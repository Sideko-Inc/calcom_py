import pydantic
import typing


class ManagedOrganizationOutput(pydantic.BaseModel):
    """
    ManagedOrganizationOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: float = pydantic.Field(
        alias="id",
    )
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
