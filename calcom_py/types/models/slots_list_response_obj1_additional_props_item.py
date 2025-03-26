import pydantic
import typing


class SlotsListResponseObj1AdditionalPropsItem(pydantic.BaseModel):
    """
    SlotsListResponseObj1AdditionalPropsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    end: typing.Optional[str] = pydantic.Field(alias="end", default=None)
    start: typing.Optional[str] = pydantic.Field(alias="start", default=None)
