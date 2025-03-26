import pydantic
import typing

from .me_org_output import MeOrgOutput


class MeOutput(pydantic.BaseModel):
    """
    MeOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_schedule_id: typing.Optional[float] = pydantic.Field(
        alias="defaultScheduleId",
    )
    email_field: str = pydantic.Field(
        alias="email",
    )
    id: float = pydantic.Field(
        alias="id",
    )
    organization: typing.Optional[MeOrgOutput] = pydantic.Field(
        alias="organization", default=None
    )
    organization_id: typing.Optional[float] = pydantic.Field(
        alias="organizationId",
    )
    time_format: float = pydantic.Field(
        alias="timeFormat",
    )
    time_zone: str = pydantic.Field(
        alias="timeZone",
    )
    username: str = pydantic.Field(
        alias="username",
    )
    week_start: str = pydantic.Field(
        alias="weekStart",
    )
