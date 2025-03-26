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


class MembershipsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        membership_id: float,
        org_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipOutputResponseDto:
        """
        Delete a membership

        DELETE /v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId}

        Args:
            membershipId: float
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.memberships.delete(
            membership_id=123.0, org_id=123.0, team_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OrgTeamMembershipOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        org_id: float,
        team_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipsOutputResponseDto:
        """
        Get all memberships

        GET /v2/organizations/{orgId}/teams/{teamId}/memberships

        Args:
            skip: The number of items to skip
            take: The number of items to return
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.memberships.list(org_id=123.0, team_id=123.0)
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
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.OrgTeamMembershipsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        membership_id: float,
        org_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipOutputResponseDto:
        """
        Get a membership

        GET /v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId}

        Args:
            membershipId: float
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.memberships.get(
            membership_id=123.0, org_id=123.0, team_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OrgTeamMembershipOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        membership_id: float,
        org_id: float,
        team_id: float,
        accepted: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disable_impersonation: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        role: typing.Union[
            typing.Optional[typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipOutputResponseDto:
        """
        Update a membership

        PATCH /v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId}

        Args:
            accepted: bool
            disableImpersonation: bool
            role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
            membershipId: float
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.memberships.patch(
            membership_id=123.0, org_id=123.0, team_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={
                "accepted": accepted,
                "disable_impersonation": disable_impersonation,
                "role": role,
            },
            dump_with=params._SerializerUpdateOrgTeamMembershipDto,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OrgTeamMembershipOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        org_id: float,
        role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"],
        team_id: float,
        user_id: float,
        accepted: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disable_impersonation: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipOutputResponseDto:
        """
        Create a membership

        POST /v2/organizations/{orgId}/teams/{teamId}/memberships

        Args:
            accepted: bool
            disableImpersonation: bool
            orgId: float
            role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
            teamId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.memberships.create(
            org_id=123.0, role="ADMIN", team_id=123.0, user_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={
                "accepted": accepted,
                "disable_impersonation": disable_impersonation,
                "role": role,
                "user_id": user_id,
            },
            dump_with=params._SerializerCreateOrgTeamMembershipDto,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OrgTeamMembershipOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncMembershipsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        membership_id: float,
        org_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipOutputResponseDto:
        """
        Delete a membership

        DELETE /v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId}

        Args:
            membershipId: float
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.memberships.delete(
            membership_id=123.0, org_id=123.0, team_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OrgTeamMembershipOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        org_id: float,
        team_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipsOutputResponseDto:
        """
        Get all memberships

        GET /v2/organizations/{orgId}/teams/{teamId}/memberships

        Args:
            skip: The number of items to skip
            take: The number of items to return
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.memberships.list(org_id=123.0, team_id=123.0)
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
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.OrgTeamMembershipsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        membership_id: float,
        org_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipOutputResponseDto:
        """
        Get a membership

        GET /v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId}

        Args:
            membershipId: float
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.memberships.get(
            membership_id=123.0, org_id=123.0, team_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OrgTeamMembershipOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        membership_id: float,
        org_id: float,
        team_id: float,
        accepted: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disable_impersonation: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        role: typing.Union[
            typing.Optional[typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipOutputResponseDto:
        """
        Update a membership

        PATCH /v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId}

        Args:
            accepted: bool
            disableImpersonation: bool
            role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
            membershipId: float
            orgId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.memberships.patch(
            membership_id=123.0, org_id=123.0, team_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={
                "accepted": accepted,
                "disable_impersonation": disable_impersonation,
                "role": role,
            },
            dump_with=params._SerializerUpdateOrgTeamMembershipDto,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OrgTeamMembershipOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        org_id: float,
        role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"],
        team_id: float,
        user_id: float,
        accepted: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        disable_impersonation: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamMembershipOutputResponseDto:
        """
        Create a membership

        POST /v2/organizations/{orgId}/teams/{teamId}/memberships

        Args:
            accepted: bool
            disableImpersonation: bool
            orgId: float
            role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
            teamId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.memberships.create(
            org_id=123.0, role="ADMIN", team_id=123.0, user_id=123.0
        )
        ```
        """
        _json = to_encodable(
            item={
                "accepted": accepted,
                "disable_impersonation": disable_impersonation,
                "role": role,
                "user_id": user_id,
            },
            dump_with=params._SerializerCreateOrgTeamMembershipDto,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/memberships",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OrgTeamMembershipOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
