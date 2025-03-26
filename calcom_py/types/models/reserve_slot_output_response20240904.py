import pydantic
import typing_extensions

from .reserve_slot_output20240904 import ReserveSlotOutput20240904


class ReserveSlotOutputResponse20240904(pydantic.BaseModel):
    """
    ReserveSlotOutputResponse20240904
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: ReserveSlotOutput20240904 = pydantic.Field(
        alias="data",
    )
    status: typing_extensions.Literal["error", "success"] = pydantic.Field(
        alias="status",
    )
