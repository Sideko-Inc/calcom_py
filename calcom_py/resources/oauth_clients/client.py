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
from calcom_py.resources.oauth_clients.managed_users import (
    AsyncManagedUsersClient,
    ManagedUsersClient,
)
from calcom_py.resources.oauth_clients.users import AsyncUsersClient, UsersClient
from calcom_py.resources.oauth_clients.webhooks import (
    AsyncWebhooksClient,
    WebhooksClient,
)
from calcom_py.types import models, params


class OauthClientsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.users = UsersClient(base_client=self._base_client)
        self.webhooks = WebhooksClient(base_client=self._base_client)
        self.managed_users = ManagedUsersClient(base_client=self._base_client)

    def delete(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetOAuthClientResponseDto:
        """
        DELETE /v2/oauth-clients/{clientId}

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.delete(client_id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/oauth-clients/{client_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetOAuthClientResponseDto,
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetOAuthClientsResponseDto:
        """
        GET /v2/oauth-clients

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/v2/oauth-clients",
            auth_names=["bearerAuth"],
            cast_to=models.GetOAuthClientsResponseDto,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetOAuthClientResponseDto:
        """
        GET /v2/oauth-clients/{clientId}

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.get(client_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetOAuthClientResponseDto,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        client_id: str,
        are_default_event_types_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        are_emails_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_cancel_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_reschedule_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        redirect_uris: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOAuthClientResponseDto:
        """
        PATCH /v2/oauth-clients/{clientId}

        Args:
            areDefaultEventTypesEnabled: If true, when creating a managed user the managed user will have 4 default event types: 30 and 60 minutes without Cal video, 30 and 60 minutes with Cal video. Set this as false if you want to create a managed user and then manually create event types for the user.
            areEmailsEnabled: bool
            bookingCancelRedirectUri: str
            bookingRedirectUri: str
            bookingRescheduleRedirectUri: str
            logo: str
            name: str
            redirectUris: typing.List[str]
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.patch(client_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "are_default_event_types_enabled": are_default_event_types_enabled,
                "are_emails_enabled": are_emails_enabled,
                "booking_cancel_redirect_uri": booking_cancel_redirect_uri,
                "booking_redirect_uri": booking_redirect_uri,
                "booking_reschedule_redirect_uri": booking_reschedule_redirect_uri,
                "logo": logo,
                "name": name,
                "redirect_uris": redirect_uris,
            },
            dump_with=params._SerializerUpdateOAuthClientInput,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/oauth-clients/{client_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetOAuthClientResponseDto,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        permissions: typing.List[
            typing_extensions.Literal[
                "*",
                "APPS_READ",
                "APPS_WRITE",
                "BOOKING_READ",
                "BOOKING_WRITE",
                "EVENT_TYPE_READ",
                "EVENT_TYPE_WRITE",
                "PROFILE_READ",
                "PROFILE_WRITE",
                "SCHEDULE_READ",
                "SCHEDULE_WRITE",
            ]
        ],
        redirect_uris: typing.List[str],
        are_default_event_types_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        are_emails_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_cancel_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_reschedule_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateOAuthClientResponseDto:
        """
        POST /v2/oauth-clients

        Args:
            areDefaultEventTypesEnabled: If true, when creating a managed user the managed user will have 4 default event types: 30 and 60 minutes without Cal video, 30 and 60 minutes with Cal video. Set this as false if you want to create a managed user and then manually create event types for the user.
            areEmailsEnabled: bool
            bookingCancelRedirectUri: str
            bookingRedirectUri: str
            bookingRescheduleRedirectUri: str
            logo: str
            name: str
            permissions: Array of permission keys like ["BOOKING_READ", "BOOKING_WRITE"]. Use ["*"] to grant all permissions.
            redirectUris: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Create an OAuth client

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.oauth_clients.create(
            name="string", permissions=["*"], redirect_uris=["string"]
        )
        ```
        """
        _json = to_encodable(
            item={
                "are_default_event_types_enabled": are_default_event_types_enabled,
                "are_emails_enabled": are_emails_enabled,
                "booking_cancel_redirect_uri": booking_cancel_redirect_uri,
                "booking_redirect_uri": booking_redirect_uri,
                "booking_reschedule_redirect_uri": booking_reschedule_redirect_uri,
                "logo": logo,
                "name": name,
                "permissions": permissions,
                "redirect_uris": redirect_uris,
            },
            dump_with=params._SerializerCreateOAuthClientInput,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/oauth-clients",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateOAuthClientResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncOauthClientsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.users = AsyncUsersClient(base_client=self._base_client)
        self.webhooks = AsyncWebhooksClient(base_client=self._base_client)
        self.managed_users = AsyncManagedUsersClient(base_client=self._base_client)

    async def delete(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetOAuthClientResponseDto:
        """
        DELETE /v2/oauth-clients/{clientId}

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.delete(client_id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/oauth-clients/{client_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetOAuthClientResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetOAuthClientsResponseDto:
        """
        GET /v2/oauth-clients

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/v2/oauth-clients",
            auth_names=["bearerAuth"],
            cast_to=models.GetOAuthClientsResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetOAuthClientResponseDto:
        """
        GET /v2/oauth-clients/{clientId}

        Args:
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.get(client_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/oauth-clients/{client_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetOAuthClientResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        client_id: str,
        are_default_event_types_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        are_emails_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_cancel_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_reschedule_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        redirect_uris: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOAuthClientResponseDto:
        """
        PATCH /v2/oauth-clients/{clientId}

        Args:
            areDefaultEventTypesEnabled: If true, when creating a managed user the managed user will have 4 default event types: 30 and 60 minutes without Cal video, 30 and 60 minutes with Cal video. Set this as false if you want to create a managed user and then manually create event types for the user.
            areEmailsEnabled: bool
            bookingCancelRedirectUri: str
            bookingRedirectUri: str
            bookingRescheduleRedirectUri: str
            logo: str
            name: str
            redirectUris: typing.List[str]
            clientId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.patch(client_id="string")
        ```
        """
        _json = to_encodable(
            item={
                "are_default_event_types_enabled": are_default_event_types_enabled,
                "are_emails_enabled": are_emails_enabled,
                "booking_cancel_redirect_uri": booking_cancel_redirect_uri,
                "booking_redirect_uri": booking_redirect_uri,
                "booking_reschedule_redirect_uri": booking_reschedule_redirect_uri,
                "logo": logo,
                "name": name,
                "redirect_uris": redirect_uris,
            },
            dump_with=params._SerializerUpdateOAuthClientInput,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/oauth-clients/{client_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetOAuthClientResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        permissions: typing.List[
            typing_extensions.Literal[
                "*",
                "APPS_READ",
                "APPS_WRITE",
                "BOOKING_READ",
                "BOOKING_WRITE",
                "EVENT_TYPE_READ",
                "EVENT_TYPE_WRITE",
                "PROFILE_READ",
                "PROFILE_WRITE",
                "SCHEDULE_READ",
                "SCHEDULE_WRITE",
            ]
        ],
        redirect_uris: typing.List[str],
        are_default_event_types_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        are_emails_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_cancel_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_reschedule_redirect_uri: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateOAuthClientResponseDto:
        """
        POST /v2/oauth-clients

        Args:
            areDefaultEventTypesEnabled: If true, when creating a managed user the managed user will have 4 default event types: 30 and 60 minutes without Cal video, 30 and 60 minutes with Cal video. Set this as false if you want to create a managed user and then manually create event types for the user.
            areEmailsEnabled: bool
            bookingCancelRedirectUri: str
            bookingRedirectUri: str
            bookingRescheduleRedirectUri: str
            logo: str
            name: str
            permissions: Array of permission keys like ["BOOKING_READ", "BOOKING_WRITE"]. Use ["*"] to grant all permissions.
            redirectUris: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Create an OAuth client

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.oauth_clients.create(
            name="string", permissions=["*"], redirect_uris=["string"]
        )
        ```
        """
        _json = to_encodable(
            item={
                "are_default_event_types_enabled": are_default_event_types_enabled,
                "are_emails_enabled": are_emails_enabled,
                "booking_cancel_redirect_uri": booking_cancel_redirect_uri,
                "booking_redirect_uri": booking_redirect_uri,
                "booking_reschedule_redirect_uri": booking_reschedule_redirect_uri,
                "logo": logo,
                "name": name,
                "permissions": permissions,
                "redirect_uris": redirect_uris,
            },
            dump_with=params._SerializerCreateOAuthClientInput,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/oauth-clients",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateOAuthClientResponseDto,
            request_options=request_options or default_request_options(),
        )
