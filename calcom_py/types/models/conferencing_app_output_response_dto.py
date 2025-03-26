import pydantic
import typing_extensions

from .conferencing_apps_output_dto import ConferencingAppsOutputDto


class ConferencingAppOutputResponseDto(pydantic.BaseModel):
    """
    ConferencingAppOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: ConferencingAppsOutputDto = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
