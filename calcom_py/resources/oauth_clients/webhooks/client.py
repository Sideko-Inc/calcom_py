import typing
import typing_extensions

from calcom_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from calcom_py.types import models, params


class WebhooksClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete_all(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeleteManyWebhooksOutputResponseDto:
        """
        Delete all webhooks

        DELETE /v2/oauth-clients/{clientId}/webhooks

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.webhooks.delete_all(client_id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/oauth-clients/{client_id}/webhooks",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteManyWebhooksOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def delete(
        self,
        *,
        client_id: str,
        webhook_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhookOutputResponseDto:
        """
        Delete a webhook

        DELETE /v2/oauth-clients/{clientId}/webhooks/{webhookId}

        Args:
            clientId: str
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.webhooks.delete(client_id="string", webhook_id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/oauth-clients/{client_id}/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OAuthClientWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        client_id: str,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhooksOutputResponseDto:
        """
        Get all webhooks

        GET /v2/oauth-clients/{clientId}/webhooks

        Args:
            skip: The number of items to skip
            take: The number of items to return
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.webhooks.list(client_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(skip, type_utils.NotGiven):
            encode_query_param(
                _query,
                "skip",
                to_encodable(item=skip, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(take, type_utils.NotGiven):
            encode_query_param(
                _query,
                "take",
                to_encodable(item=take, dump_with=float),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}/webhooks",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.OAuthClientWebhooksOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        client_id: str,
        webhook_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhookOutputResponseDto:
        """
        Get a webhook

        GET /v2/oauth-clients/{clientId}/webhooks/{webhookId}

        Args:
            clientId: str
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.webhooks.get(client_id="string", webhook_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OAuthClientWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        client_id: str,
        webhook_id: str,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payload_template: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        subscriber_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        triggers: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
                    "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
                    "BOOKING_CANCELLED",
                    "BOOKING_CREATED",
                    "BOOKING_NO_SHOW_UPDATED",
                    "BOOKING_PAID",
                    "BOOKING_PAYMENT_INITIATED",
                    "BOOKING_REJECTED",
                    "BOOKING_REQUESTED",
                    "BOOKING_RESCHEDULED",
                    "FORM_SUBMITTED",
                    "FORM_SUBMITTED_NO_EVENT",
                    "INSTANT_MEETING",
                    "MEETING_ENDED",
                    "MEETING_STARTED",
                    "OOO_CREATED",
                    "RECORDING_READY",
                    "RECORDING_TRANSCRIPTION_GENERATED",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhookOutputResponseDto:
        """
        Update a webhook

        PATCH /v2/oauth-clients/{clientId}/webhooks/{webhookId}

        Args:
            active: bool
            payloadTemplate: The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
            secret: str
            subscriberUrl: str
            triggers: typing_extensions.Literal["AFTER_GUESTS_CAL_VIDEO_NO_SHOW", "AFTER_HOSTS_CAL_VIDEO_NO_SHOW", "BOOKING_CANCELLED", "BOOKING_CREATED", "BOOKING_NO_SHOW_UPDATED", "BOOKING_PAID", "BOOKING_PAYMENT_INITIATED", "BOOKING_REJECTED", "BOOKING_REQUESTED", "BOOKING_RESCHEDULED", "FORM_SUBMITTED", "FORM_SUBMITTED_NO_EVENT", "INSTANT_MEETING", "MEETING_ENDED", "MEETING_STARTED", "OOO_CREATED", "RECORDING_READY", "RECORDING_TRANSCRIPTION_GENERATED"]
            clientId: str
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.webhooks.patch(
            client_id="string",
            webhook_id="string",
            payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
            triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
        )
        ```
        """
        _json = to_encodable(
            item={
                "active": active,
                "payload_template": payload_template,
                "secret": secret,
                "subscriber_url": subscriber_url,
                "triggers": triggers,
            },
            dump_with=params._SerializerUpdateWebhookInputDto,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/oauth-clients/{client_id}/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OAuthClientWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        active: bool,
        client_id: str,
        subscriber_url: str,
        triggers: typing_extensions.Literal[
            "AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
            "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
            "BOOKING_CANCELLED",
            "BOOKING_CREATED",
            "BOOKING_NO_SHOW_UPDATED",
            "BOOKING_PAID",
            "BOOKING_PAYMENT_INITIATED",
            "BOOKING_REJECTED",
            "BOOKING_REQUESTED",
            "BOOKING_RESCHEDULED",
            "FORM_SUBMITTED",
            "FORM_SUBMITTED_NO_EVENT",
            "INSTANT_MEETING",
            "MEETING_ENDED",
            "MEETING_STARTED",
            "OOO_CREATED",
            "RECORDING_READY",
            "RECORDING_TRANSCRIPTION_GENERATED",
        ],
        payload_template: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhookOutputResponseDto:
        """
        Create a webhook

        POST /v2/oauth-clients/{clientId}/webhooks

        Args:
            payloadTemplate: The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
            secret: str
            active: bool
            clientId: str
            subscriberUrl: str
            triggers: typing_extensions.Literal["AFTER_GUESTS_CAL_VIDEO_NO_SHOW", "AFTER_HOSTS_CAL_VIDEO_NO_SHOW", "BOOKING_CANCELLED", "BOOKING_CREATED", "BOOKING_NO_SHOW_UPDATED", "BOOKING_PAID", "BOOKING_PAYMENT_INITIATED", "BOOKING_REJECTED", "BOOKING_REQUESTED", "BOOKING_RESCHEDULED", "FORM_SUBMITTED", "FORM_SUBMITTED_NO_EVENT", "INSTANT_MEETING", "MEETING_ENDED", "MEETING_STARTED", "OOO_CREATED", "RECORDING_READY", "RECORDING_TRANSCRIPTION_GENERATED"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.webhooks.create(
            active=True,
            client_id="string",
            subscriber_url="string",
            triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
            payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
        )
        ```
        """
        _json = to_encodable(
            item={
                "payload_template": payload_template,
                "secret": secret,
                "active": active,
                "subscriber_url": subscriber_url,
                "triggers": triggers,
            },
            dump_with=params._SerializerCreateWebhookInputDto,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/oauth-clients/{client_id}/webhooks",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OAuthClientWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncWebhooksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete_all(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeleteManyWebhooksOutputResponseDto:
        """
        Delete all webhooks

        DELETE /v2/oauth-clients/{clientId}/webhooks

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.webhooks.delete_all(client_id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/oauth-clients/{client_id}/webhooks",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteManyWebhooksOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def delete(
        self,
        *,
        client_id: str,
        webhook_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhookOutputResponseDto:
        """
        Delete a webhook

        DELETE /v2/oauth-clients/{clientId}/webhooks/{webhookId}

        Args:
            clientId: str
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.webhooks.delete(
            client_id="string", webhook_id="string"
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/oauth-clients/{client_id}/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OAuthClientWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        client_id: str,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhooksOutputResponseDto:
        """
        Get all webhooks

        GET /v2/oauth-clients/{clientId}/webhooks

        Args:
            skip: The number of items to skip
            take: The number of items to return
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.webhooks.list(client_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(skip, type_utils.NotGiven):
            encode_query_param(
                _query,
                "skip",
                to_encodable(item=skip, dump_with=float),
                style="form",
                explode=True,
            )
        if not isinstance(take, type_utils.NotGiven):
            encode_query_param(
                _query,
                "take",
                to_encodable(item=take, dump_with=float),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}/webhooks",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.OAuthClientWebhooksOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        client_id: str,
        webhook_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhookOutputResponseDto:
        """
        Get a webhook

        GET /v2/oauth-clients/{clientId}/webhooks/{webhookId}

        Args:
            clientId: str
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.webhooks.get(client_id="string", webhook_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OAuthClientWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        client_id: str,
        webhook_id: str,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payload_template: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        subscriber_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        triggers: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
                    "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
                    "BOOKING_CANCELLED",
                    "BOOKING_CREATED",
                    "BOOKING_NO_SHOW_UPDATED",
                    "BOOKING_PAID",
                    "BOOKING_PAYMENT_INITIATED",
                    "BOOKING_REJECTED",
                    "BOOKING_REQUESTED",
                    "BOOKING_RESCHEDULED",
                    "FORM_SUBMITTED",
                    "FORM_SUBMITTED_NO_EVENT",
                    "INSTANT_MEETING",
                    "MEETING_ENDED",
                    "MEETING_STARTED",
                    "OOO_CREATED",
                    "RECORDING_READY",
                    "RECORDING_TRANSCRIPTION_GENERATED",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhookOutputResponseDto:
        """
        Update a webhook

        PATCH /v2/oauth-clients/{clientId}/webhooks/{webhookId}

        Args:
            active: bool
            payloadTemplate: The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
            secret: str
            subscriberUrl: str
            triggers: typing_extensions.Literal["AFTER_GUESTS_CAL_VIDEO_NO_SHOW", "AFTER_HOSTS_CAL_VIDEO_NO_SHOW", "BOOKING_CANCELLED", "BOOKING_CREATED", "BOOKING_NO_SHOW_UPDATED", "BOOKING_PAID", "BOOKING_PAYMENT_INITIATED", "BOOKING_REJECTED", "BOOKING_REQUESTED", "BOOKING_RESCHEDULED", "FORM_SUBMITTED", "FORM_SUBMITTED_NO_EVENT", "INSTANT_MEETING", "MEETING_ENDED", "MEETING_STARTED", "OOO_CREATED", "RECORDING_READY", "RECORDING_TRANSCRIPTION_GENERATED"]
            clientId: str
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.webhooks.patch(
            client_id="string",
            webhook_id="string",
            payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
            triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
        )
        ```
        """
        _json = to_encodable(
            item={
                "active": active,
                "payload_template": payload_template,
                "secret": secret,
                "subscriber_url": subscriber_url,
                "triggers": triggers,
            },
            dump_with=params._SerializerUpdateWebhookInputDto,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/oauth-clients/{client_id}/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OAuthClientWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        active: bool,
        client_id: str,
        subscriber_url: str,
        triggers: typing_extensions.Literal[
            "AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
            "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
            "BOOKING_CANCELLED",
            "BOOKING_CREATED",
            "BOOKING_NO_SHOW_UPDATED",
            "BOOKING_PAID",
            "BOOKING_PAYMENT_INITIATED",
            "BOOKING_REJECTED",
            "BOOKING_REQUESTED",
            "BOOKING_RESCHEDULED",
            "FORM_SUBMITTED",
            "FORM_SUBMITTED_NO_EVENT",
            "INSTANT_MEETING",
            "MEETING_ENDED",
            "MEETING_STARTED",
            "OOO_CREATED",
            "RECORDING_READY",
            "RECORDING_TRANSCRIPTION_GENERATED",
        ],
        payload_template: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OAuthClientWebhookOutputResponseDto:
        """
        Create a webhook

        POST /v2/oauth-clients/{clientId}/webhooks

        Args:
            payloadTemplate: The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
            secret: str
            active: bool
            clientId: str
            subscriberUrl: str
            triggers: typing_extensions.Literal["AFTER_GUESTS_CAL_VIDEO_NO_SHOW", "AFTER_HOSTS_CAL_VIDEO_NO_SHOW", "BOOKING_CANCELLED", "BOOKING_CREATED", "BOOKING_NO_SHOW_UPDATED", "BOOKING_PAID", "BOOKING_PAYMENT_INITIATED", "BOOKING_REJECTED", "BOOKING_REQUESTED", "BOOKING_RESCHEDULED", "FORM_SUBMITTED", "FORM_SUBMITTED_NO_EVENT", "INSTANT_MEETING", "MEETING_ENDED", "MEETING_STARTED", "OOO_CREATED", "RECORDING_READY", "RECORDING_TRANSCRIPTION_GENERATED"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.webhooks.create(
            active=True,
            client_id="string",
            subscriber_url="string",
            triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
            payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
        )
        ```
        """
        _json = to_encodable(
            item={
                "payload_template": payload_template,
                "secret": secret,
                "active": active,
                "subscriber_url": subscriber_url,
                "triggers": triggers,
            },
            dump_with=params._SerializerCreateWebhookInputDto,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/oauth-clients/{client_id}/webhooks",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OAuthClientWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
