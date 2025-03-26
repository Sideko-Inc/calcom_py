import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from calcom_py.types import models, params


class DelegationCredentialsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def patch(
        self,
        *,
        credential_id: str,
        org_id: float,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        service_account_key: typing.Union[
            typing.Optional[typing.List[params.GoogleServiceAccountKeyInput]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateDelegationCredentialOutput:
        """
        Update delegation credentials of your organization.

        PATCH /v2/organizations/{orgId}/delegation-credentials/{credentialId}

        Args:
            enabled: bool
            serviceAccountKey: typing.List[GoogleServiceAccountKeyInput]
            credentialId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.delegation_credentials.patch(
            credential_id="string", org_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={"enabled": enabled, "service_account_key": service_account_key},
            dump_with=params._SerializerUpdateDelegationCredentialInput,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/delegation-credentials/{credential_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateDelegationCredentialOutput,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        domain: str,
        org_id: float,
        service_account_key: typing.List[params.GoogleServiceAccountKeyInput],
        workspace_platform_slug: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateDelegationCredentialOutput:
        """
        Save delegation credentials for your organization.

        POST /v2/organizations/{orgId}/delegation-credentials

        Args:
            domain: str
            orgId: float
            serviceAccountKey: typing.List[GoogleServiceAccountKeyInput]
            workspacePlatformSlug: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.delegation_credentials.create(
            domain="string",
            org_id=123.0,
            service_account_key=[
                {
                    "client_email": "string",
                    "client_id": "string",
                    "private_key": "string",
                }
            ],
            workspace_platform_slug="string",
        )
        ```
        """
        _json = to_encodable(
            item={
                "domain": domain,
                "service_account_key": service_account_key,
                "workspace_platform_slug": workspace_platform_slug,
            },
            dump_with=params._SerializerCreateDelegationCredentialInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/delegation-credentials",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateDelegationCredentialOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncDelegationCredentialsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def patch(
        self,
        *,
        credential_id: str,
        org_id: float,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        service_account_key: typing.Union[
            typing.Optional[typing.List[params.GoogleServiceAccountKeyInput]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateDelegationCredentialOutput:
        """
        Update delegation credentials of your organization.

        PATCH /v2/organizations/{orgId}/delegation-credentials/{credentialId}

        Args:
            enabled: bool
            serviceAccountKey: typing.List[GoogleServiceAccountKeyInput]
            credentialId: str
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.delegation_credentials.patch(
            credential_id="string", org_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={"enabled": enabled, "service_account_key": service_account_key},
            dump_with=params._SerializerUpdateDelegationCredentialInput,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/delegation-credentials/{credential_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateDelegationCredentialOutput,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        domain: str,
        org_id: float,
        service_account_key: typing.List[params.GoogleServiceAccountKeyInput],
        workspace_platform_slug: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateDelegationCredentialOutput:
        """
        Save delegation credentials for your organization.

        POST /v2/organizations/{orgId}/delegation-credentials

        Args:
            domain: str
            orgId: float
            serviceAccountKey: typing.List[GoogleServiceAccountKeyInput]
            workspacePlatformSlug: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.delegation_credentials.create(
            domain="string",
            org_id=123.0,
            service_account_key=[
                {
                    "client_email": "string",
                    "client_id": "string",
                    "private_key": "string",
                }
            ],
            workspace_platform_slug="string",
        )
        ```
        """
        _json = to_encodable(
            item={
                "domain": domain,
                "service_account_key": service_account_key,
                "workspace_platform_slug": workspace_platform_slug,
            },
            dump_with=params._SerializerCreateDelegationCredentialInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/delegation-credentials",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateDelegationCredentialOutput,
            request_options=request_options or default_request_options(),
        )
