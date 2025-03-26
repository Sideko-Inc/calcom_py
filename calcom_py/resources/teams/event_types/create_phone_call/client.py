import typing
import typing_extensions

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from calcom_py.types import models, params


class CreatePhoneCallClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        cal_api_key: str,
        enabled: typing.Dict[str, typing.Any],
        event_type_id: float,
        number_to_call: str,
        team_id: float,
        template_type: typing_extensions.Literal[
            "CHECK_IN_APPOINTMENT", "CUSTOM_TEMPLATE"
        ],
        your_phone_number: str,
        begin_message: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        general_prompt: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        guest_company: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        guest_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        guest_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        scheduler_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreatePhoneCallOutput:
        """
        Create a phone call

        POST /v2/teams/{teamId}/event-types/{eventTypeId}/create-phone-call

        Args:
            beginMessage: Begin message
            generalPrompt: General prompt
            guestCompany: Guest company
            guestEmail: Guest email
            guestName: Guest name
            schedulerName: Scheduler name
            calApiKey: CAL API Key
            enabled: Enabled status
            eventTypeId: float
            numberToCall: Number to call
            teamId: float
            templateType: Template type
            yourPhoneNumber: Your phone number
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.event_types.create_phone_call.create(
            cal_api_key="string",
            enabled={},
            event_type_id=123.0,
            number_to_call="string",
            team_id=123.0,
            template_type="CHECK_IN_APPOINTMENT",
            your_phone_number="string",
        )
        ```
        """
        _json = to_encodable(
            item={
                "begin_message": begin_message,
                "general_prompt": general_prompt,
                "guest_company": guest_company,
                "guest_email": guest_email,
                "guest_name": guest_name,
                "scheduler_name": scheduler_name,
                "cal_api_key": cal_api_key,
                "enabled": enabled,
                "number_to_call": number_to_call,
                "template_type": template_type,
                "your_phone_number": your_phone_number,
            },
            dump_with=params._SerializerCreatePhoneCallInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/teams/{team_id}/event-types/{event_type_id}/create-phone-call",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreatePhoneCallOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncCreatePhoneCallClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        cal_api_key: str,
        enabled: typing.Dict[str, typing.Any],
        event_type_id: float,
        number_to_call: str,
        team_id: float,
        template_type: typing_extensions.Literal[
            "CHECK_IN_APPOINTMENT", "CUSTOM_TEMPLATE"
        ],
        your_phone_number: str,
        begin_message: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        general_prompt: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        guest_company: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        guest_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        guest_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        scheduler_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreatePhoneCallOutput:
        """
        Create a phone call

        POST /v2/teams/{teamId}/event-types/{eventTypeId}/create-phone-call

        Args:
            beginMessage: Begin message
            generalPrompt: General prompt
            guestCompany: Guest company
            guestEmail: Guest email
            guestName: Guest name
            schedulerName: Scheduler name
            calApiKey: CAL API Key
            enabled: Enabled status
            eventTypeId: float
            numberToCall: Number to call
            teamId: float
            templateType: Template type
            yourPhoneNumber: Your phone number
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.event_types.create_phone_call.create(
            cal_api_key="string",
            enabled={},
            event_type_id=123.0,
            number_to_call="string",
            team_id=123.0,
            template_type="CHECK_IN_APPOINTMENT",
            your_phone_number="string",
        )
        ```
        """
        _json = to_encodable(
            item={
                "begin_message": begin_message,
                "general_prompt": general_prompt,
                "guest_company": guest_company,
                "guest_email": guest_email,
                "guest_name": guest_name,
                "scheduler_name": scheduler_name,
                "cal_api_key": cal_api_key,
                "enabled": enabled,
                "number_to_call": number_to_call,
                "template_type": template_type,
                "your_phone_number": your_phone_number,
            },
            dump_with=params._SerializerCreatePhoneCallInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/teams/{team_id}/event-types/{event_type_id}/create-phone-call",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreatePhoneCallOutput,
            request_options=request_options or default_request_options(),
        )
