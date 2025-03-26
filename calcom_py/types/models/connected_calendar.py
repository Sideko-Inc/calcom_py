import pydantic
import typing

from .calendar import Calendar
from .integration import Integration
from .primary import Primary


class ConnectedCalendar(pydantic.BaseModel):
    """
    ConnectedCalendar
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    calendars: typing.Optional[typing.List[Calendar]] = pydantic.Field(
        alias="calendars", default=None
    )
    credential_id: float = pydantic.Field(
        alias="credentialId",
    )
    delegation_credential_id: typing.Optional[str] = pydantic.Field(
        alias="delegationCredentialId", default=None
    )
    integration: Integration = pydantic.Field(
        alias="integration",
    )
    primary: typing.Optional[Primary] = pydantic.Field(alias="primary", default=None)
