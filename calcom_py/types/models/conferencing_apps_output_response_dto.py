import pydantic
import typing
import typing_extensions

from .conferencing_apps_output_dto import ConferencingAppsOutputDto


class ConferencingAppsOutputResponseDto(pydantic.BaseModel):
    """
    ConferencingAppsOutputResponseDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[ConferencingAppsOutputDto] = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
