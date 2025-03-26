import pydantic
import typing
import typing_extensions


class UpdateOrganizationAttributeOptionInput(typing_extensions.TypedDict):
    """
    UpdateOrganizationAttributeOptionInput
    """

    slug: typing_extensions.NotRequired[str]

    value: typing_extensions.NotRequired[str]


class _SerializerUpdateOrganizationAttributeOptionInput(pydantic.BaseModel):
    """
    Serializer for UpdateOrganizationAttributeOptionInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
