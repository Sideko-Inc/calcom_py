import pydantic


class ProviderVerifyClientData(pydantic.BaseModel):
    """
    ProviderVerifyClientData
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    client_id: str = pydantic.Field(
        alias="clientId",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    organization_id: float = pydantic.Field(
        alias="organizationId",
    )
