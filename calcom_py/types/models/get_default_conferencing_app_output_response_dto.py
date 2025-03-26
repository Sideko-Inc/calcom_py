import pydantic
import typing
import typing_extensions

from .default_conferencing_apps_output_dto import DefaultConferencingAppsOutputDto


class GetDefaultConferencingAppOutputResponseDto(pydantic.BaseModel):
    """
    GetDefaultConferencingAppOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[DefaultConferencingAppsOutputDto] = pydantic.Field(
        alias="data", default=None
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
