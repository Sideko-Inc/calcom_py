import pydantic

from .workspace_platform_dto import WorkspacePlatformDto


class DelegationCredentialOutput(pydantic.BaseModel):
    """
    DelegationCredentialOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: str = pydantic.Field(
        alias="createdAt",
    )
    domain: str = pydantic.Field(
        alias="domain",
    )
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    organization_id: float = pydantic.Field(
        alias="organizationId",
    )
    updated_at: str = pydantic.Field(
        alias="updatedAt",
    )
    workspace_platform: WorkspacePlatformDto = pydantic.Field(
        alias="workspacePlatform",
    )
