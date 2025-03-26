import pydantic
import typing


class SelectedCalendarOutputDto(pydantic.BaseModel):
    """
    SelectedCalendarOutputDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credential_id: typing.Optional[float] = pydantic.Field(
        alias="credentialId",
    )
    external_id: str = pydantic.Field(
        alias="externalId",
    )
    integration: str = pydantic.Field(
        alias="integration",
    )
    user_id: float = pydantic.Field(
        alias="userId",
    )
