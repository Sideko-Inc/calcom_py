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

    def delete(
        self,
        *,
        webhook_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UserWebhookOutputResponseDto:
        """
        Delete a webhook

        DELETE /v2/webhooks/{webhookId}

        Args:
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.webhooks.delete(webhook_id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            cast_to=models.UserWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UserWebhooksOutputResponseDto:
        """
        Get all webooks

        Gets a paginated list of webhooks for the authenticated user.

        GET /v2/webhooks

        Args:
            skip: The number of items to skip
            take: The number of items to return
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.webhooks.list()
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
            path="/v2/webhooks",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.UserWebhooksOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        webhook_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UserWebhookOutputResponseDto:
        """
        Get a webhook

        GET /v2/webhooks/{webhookId}

        Args:
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.webhooks.get(webhook_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            cast_to=models.UserWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
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
    ) -> models.UserWebhookOutputResponseDto:
        """
        Update a webhook

        PATCH /v2/webhooks/{webhookId}

        Args:
            active: bool
            payloadTemplate: The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
            secret: str
            subscriberUrl: str
            triggers: typing_extensions.Literal["AFTER_GUESTS_CAL_VIDEO_NO_SHOW", "AFTER_HOSTS_CAL_VIDEO_NO_SHOW", "BOOKING_CANCELLED", "BOOKING_CREATED", "BOOKING_NO_SHOW_UPDATED", "BOOKING_PAID", "BOOKING_PAYMENT_INITIATED", "BOOKING_REJECTED", "BOOKING_REQUESTED", "BOOKING_RESCHEDULED", "FORM_SUBMITTED", "FORM_SUBMITTED_NO_EVENT", "INSTANT_MEETING", "MEETING_ENDED", "MEETING_STARTED", "OOO_CREATED", "RECORDING_READY", "RECORDING_TRANSCRIPTION_GENERATED"]
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.webhooks.patch(
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
            path=f"/v2/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UserWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        active: bool,
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
    ) -> models.UserWebhookOutputResponseDto:
        """
        Create a webhook

        POST /v2/webhooks

        Args:
            payloadTemplate: The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
            secret: str
            active: bool
            subscriberUrl: str
            triggers: typing_extensions.Literal["AFTER_GUESTS_CAL_VIDEO_NO_SHOW", "AFTER_HOSTS_CAL_VIDEO_NO_SHOW", "BOOKING_CANCELLED", "BOOKING_CREATED", "BOOKING_NO_SHOW_UPDATED", "BOOKING_PAID", "BOOKING_PAYMENT_INITIATED", "BOOKING_REJECTED", "BOOKING_REQUESTED", "BOOKING_RESCHEDULED", "FORM_SUBMITTED", "FORM_SUBMITTED_NO_EVENT", "INSTANT_MEETING", "MEETING_ENDED", "MEETING_STARTED", "OOO_CREATED", "RECORDING_READY", "RECORDING_TRANSCRIPTION_GENERATED"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.webhooks.create(
            active=True,
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
            path="/v2/webhooks",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UserWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncWebhooksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        webhook_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UserWebhookOutputResponseDto:
        """
        Delete a webhook

        DELETE /v2/webhooks/{webhookId}

        Args:
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.webhooks.delete(webhook_id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            cast_to=models.UserWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UserWebhooksOutputResponseDto:
        """
        Get all webooks

        Gets a paginated list of webhooks for the authenticated user.

        GET /v2/webhooks

        Args:
            skip: The number of items to skip
            take: The number of items to return
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.webhooks.list()
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
            path="/v2/webhooks",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.UserWebhooksOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        webhook_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UserWebhookOutputResponseDto:
        """
        Get a webhook

        GET /v2/webhooks/{webhookId}

        Args:
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.webhooks.get(webhook_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            cast_to=models.UserWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
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
    ) -> models.UserWebhookOutputResponseDto:
        """
        Update a webhook

        PATCH /v2/webhooks/{webhookId}

        Args:
            active: bool
            payloadTemplate: The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
            secret: str
            subscriberUrl: str
            triggers: typing_extensions.Literal["AFTER_GUESTS_CAL_VIDEO_NO_SHOW", "AFTER_HOSTS_CAL_VIDEO_NO_SHOW", "BOOKING_CANCELLED", "BOOKING_CREATED", "BOOKING_NO_SHOW_UPDATED", "BOOKING_PAID", "BOOKING_PAYMENT_INITIATED", "BOOKING_REJECTED", "BOOKING_REQUESTED", "BOOKING_RESCHEDULED", "FORM_SUBMITTED", "FORM_SUBMITTED_NO_EVENT", "INSTANT_MEETING", "MEETING_ENDED", "MEETING_STARTED", "OOO_CREATED", "RECORDING_READY", "RECORDING_TRANSCRIPTION_GENERATED"]
            webhookId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.webhooks.patch(
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
            path=f"/v2/webhooks/{webhook_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UserWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        active: bool,
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
    ) -> models.UserWebhookOutputResponseDto:
        """
        Create a webhook

        POST /v2/webhooks

        Args:
            payloadTemplate: The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information
            secret: str
            active: bool
            subscriberUrl: str
            triggers: typing_extensions.Literal["AFTER_GUESTS_CAL_VIDEO_NO_SHOW", "AFTER_HOSTS_CAL_VIDEO_NO_SHOW", "BOOKING_CANCELLED", "BOOKING_CREATED", "BOOKING_NO_SHOW_UPDATED", "BOOKING_PAID", "BOOKING_PAYMENT_INITIATED", "BOOKING_REJECTED", "BOOKING_REQUESTED", "BOOKING_RESCHEDULED", "FORM_SUBMITTED", "FORM_SUBMITTED_NO_EVENT", "INSTANT_MEETING", "MEETING_ENDED", "MEETING_STARTED", "OOO_CREATED", "RECORDING_READY", "RECORDING_TRANSCRIPTION_GENERATED"]
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.webhooks.create(
            active=True,
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
            path="/v2/webhooks",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UserWebhookOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
