import pydantic
import typing


class ManagedOrganizationWithApiKeyOutput(pydantic.BaseModel):
    """
    ManagedOrganizationWithApiKeyOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    api_key: str = pydantic.Field(
        alias="apiKey",
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
