import pydantic
import typing
import typing_extensions


class UpdateOrganizationAttributeInput(typing_extensions.TypedDict):
    """
    UpdateOrganizationAttributeInput
    """

    enabled: typing_extensions.NotRequired[bool]

    name: typing_extensions.NotRequired[str]

    slug: typing_extensions.NotRequired[str]

    type_field: typing_extensions.NotRequired[
        typing_extensions.Literal["MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"]
    ]


class _SerializerUpdateOrganizationAttributeInput(pydantic.BaseModel):
    """
    Serializer for UpdateOrganizationAttributeInput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    type_field: typing.Optional[
        typing_extensions.Literal["MULTI_SELECT", "NUMBER", "SINGLE_SELECT", "TEXT"]
    ] = pydantic.Field(alias="type", default=None)
