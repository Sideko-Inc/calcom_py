import pydantic
import typing


class DefaultConferencingAppsOutputDto(pydantic.BaseModel):
    """
    DefaultConferencingAppsOutputDto
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_link: typing.Optional[str] = pydantic.Field(alias="appLink", default=None)
    app_slug: typing.Optional[str] = pydantic.Field(alias="appSlug", default=None)
