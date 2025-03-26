import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from calcom_py.resources.organizations.attributes import (
    AsyncAttributesClient,
    AttributesClient,
)
from calcom_py.resources.organizations.delegation_credentials import (
    AsyncDelegationCredentialsClient,
    DelegationCredentialsClient,
)
from calcom_py.resources.organizations.memberships import (
    AsyncMembershipsClient,
    MembershipsClient,
)
from calcom_py.resources.organizations.ooo import AsyncOooClient, OooClient
from calcom_py.resources.organizations.schedules import (
    AsyncSchedulesClient,
    SchedulesClient,
)
from calcom_py.resources.organizations.teams import AsyncTeamsClient, TeamsClient
from calcom_py.resources.organizations.users import AsyncUsersClient, UsersClient
from calcom_py.resources.organizations.webhooks import (
    AsyncWebhooksClient,
    WebhooksClient,
)
from calcom_py.types import models, params


class OrganizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.attributes = AttributesClient(base_client=self._base_client)
        self.memberships = MembershipsClient(base_client=self._base_client)
        self.teams = TeamsClient(base_client=self._base_client)
        self.users = UsersClient(base_client=self._base_client)
        self.webhooks = WebhooksClient(base_client=self._base_client)
        self.ooo = OooClient(base_client=self._base_client)
        self.schedules = SchedulesClient(base_client=self._base_client)
        self.delegation_credentials = DelegationCredentialsClient(
            base_client=self._base_client
        )

    def delete(
        self,
        *,
        managed_organization_id: float,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedOrganizationOutput:
        """
        Delete an organization within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        DELETE /v2/organizations/{orgId}/organizations/{managedOrganizationId}

        Args:
            managedOrganizationId: float
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.delete(managed_organization_id=123.0, org_id=123.0)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/organizations/{managed_organization_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedOrganizationOutput,
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, org_id: float, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetManagedOrganizationsOutput:
        """
        Get all organizations within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        GET /v2/organizations/{orgId}/organizations

        Args:
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.list(org_id=123.0)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/organizations",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedOrganizationsOutput,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        managed_organization_id: float,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedOrganizationOutput:
        """
        Get an organization within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        GET /v2/organizations/{orgId}/organizations/{managedOrganizationId}

        Args:
            managedOrganizationId: float
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.get(managed_organization_id=123.0, org_id=123.0)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/organizations/{managed_organization_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedOrganizationOutput,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        managed_organization_id: float,
        org_id: float,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedOrganizationOutput:
        """
        Update an organization within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        PATCH /v2/organizations/{orgId}/organizations/{managedOrganizationId}

        Args:
            metadata: You can store any additional data you want here.
        Metadata must have at most 50 keys, each key up to 40 characters.
        Values can be strings (up to 500 characters), numbers, or booleans.
            name: Name of the organization
            managedOrganizationId: float
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.patch(
            managed_organization_id=123.0,
            org_id=123.0,
            metadata={"key": "value"},
            name="CalTeam",
        )
        ```
        """
        _json = to_encodable(
            item={"metadata": metadata, "name": name},
            dump_with=params._SerializerUpdateOrganizationInput,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/organizations/{managed_organization_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetManagedOrganizationOutput,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        org_id: float,
        api_key_days_valid: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        api_key_never_expires: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateManagedOrganizationOutput:
        """
        Create an organization within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        POST /v2/organizations/{orgId}/organizations

        Args:
            apiKeyDaysValid: For how many days is managed organization api key valid. Defaults to 30 days.
            apiKeyNeverExpires: If true, organization api key never expires.
            metadata: You can store any additional data you want here.
        Metadata must have at most 50 keys, each key up to 40 characters.
        Values can be strings (up to 500 characters), numbers, or booleans.
            name: Name of the organization
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.create(
            name="CalTeam",
            org_id=123.0,
            api_key_days_valid=60.0,
            api_key_never_expires=True,
            metadata={"key": "value"},
        )
        ```
        """
        _json = to_encodable(
            item={
                "api_key_days_valid": api_key_days_valid,
                "api_key_never_expires": api_key_never_expires,
                "metadata": metadata,
                "name": name,
            },
            dump_with=params._SerializerCreateOrganizationInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/organizations",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateManagedOrganizationOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncOrganizationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.attributes = AsyncAttributesClient(base_client=self._base_client)
        self.memberships = AsyncMembershipsClient(base_client=self._base_client)
        self.teams = AsyncTeamsClient(base_client=self._base_client)
        self.users = AsyncUsersClient(base_client=self._base_client)
        self.webhooks = AsyncWebhooksClient(base_client=self._base_client)
        self.ooo = AsyncOooClient(base_client=self._base_client)
        self.schedules = AsyncSchedulesClient(base_client=self._base_client)
        self.delegation_credentials = AsyncDelegationCredentialsClient(
            base_client=self._base_client
        )

    async def delete(
        self,
        *,
        managed_organization_id: float,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedOrganizationOutput:
        """
        Delete an organization within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        DELETE /v2/organizations/{orgId}/organizations/{managedOrganizationId}

        Args:
            managedOrganizationId: float
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.delete(managed_organization_id=123.0, org_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/organizations/{managed_organization_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedOrganizationOutput,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, org_id: float, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetManagedOrganizationsOutput:
        """
        Get all organizations within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        GET /v2/organizations/{orgId}/organizations

        Args:
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.list(org_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/organizations",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedOrganizationsOutput,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        managed_organization_id: float,
        org_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedOrganizationOutput:
        """
        Get an organization within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        GET /v2/organizations/{orgId}/organizations/{managedOrganizationId}

        Args:
            managedOrganizationId: float
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.get(managed_organization_id=123.0, org_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/organizations/{managed_organization_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetManagedOrganizationOutput,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        managed_organization_id: float,
        org_id: float,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetManagedOrganizationOutput:
        """
        Update an organization within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        PATCH /v2/organizations/{orgId}/organizations/{managedOrganizationId}

        Args:
            metadata: You can store any additional data you want here.
        Metadata must have at most 50 keys, each key up to 40 characters.
        Values can be strings (up to 500 characters), numbers, or booleans.
            name: Name of the organization
            managedOrganizationId: float
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.patch(
            managed_organization_id=123.0,
            org_id=123.0,
            metadata={"key": "value"},
            name="CalTeam",
        )
        ```
        """
        _json = to_encodable(
            item={"metadata": metadata, "name": name},
            dump_with=params._SerializerUpdateOrganizationInput,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/organizations/{managed_organization_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetManagedOrganizationOutput,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        org_id: float,
        api_key_days_valid: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        api_key_never_expires: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateManagedOrganizationOutput:
        """
        Create an organization within an organization

        Requires the user to have at least the 'ORG_ADMIN' role within the organization. Additionally, for platform, the plan must be 'SCALE' or higher to access this endpoint.

        POST /v2/organizations/{orgId}/organizations

        Args:
            apiKeyDaysValid: For how many days is managed organization api key valid. Defaults to 30 days.
            apiKeyNeverExpires: If true, organization api key never expires.
            metadata: You can store any additional data you want here.
        Metadata must have at most 50 keys, each key up to 40 characters.
        Values can be strings (up to 500 characters), numbers, or booleans.
            name: Name of the organization
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.create(
            name="CalTeam",
            org_id=123.0,
            api_key_days_valid=60.0,
            api_key_never_expires=True,
            metadata={"key": "value"},
        )
        ```
        """
        _json = to_encodable(
            item={
                "api_key_days_valid": api_key_days_valid,
                "api_key_never_expires": api_key_never_expires,
                "metadata": metadata,
                "name": name,
            },
            dump_with=params._SerializerCreateOrganizationInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/organizations",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateManagedOrganizationOutput,
            request_options=request_options or default_request_options(),
        )
