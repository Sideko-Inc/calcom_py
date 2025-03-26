import pydantic
import typing


class Calendar(pydantic.BaseModel):
    """
    Calendar
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credential_id: float = pydantic.Field(
        alias="credentialId",
    )
    delegation_credential_id: typing.Optional[str] = pydantic.Field(
        alias="delegationCredentialId", default=None
    )
    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    external_id: str = pydantic.Field(
        alias="externalId",
    )
    integration: typing.Optional[str] = pydantic.Field(
        alias="integration", default=None
    )
    is_selected: bool = pydantic.Field(
        alias="isSelected",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    primary: typing.Optional[bool] = pydantic.Field(alias="primary", default=None)
    read_only: bool = pydantic.Field(
        alias="readOnly",
    )
