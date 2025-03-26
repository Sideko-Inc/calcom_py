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
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteTeamMembershipOutput:
        """
        Delete a membership

        DELETE /v2/teams/{teamId}/memberships/{membershipId}

        Args:
            membershipId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.memberships.delete(membership_id=123.0, team_id=123.0)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteTeamMembershipOutput,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        team_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetTeamMembershipsOutput:
        """
        Get all memberships

        GET /v2/teams/{teamId}/memberships

        Args:
            skip: The number of items to skip
            take: The number of items to return
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.memberships.list(team_id=123.0)
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
            path=f"/v2/teams/{team_id}/memberships",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetTeamMembershipsOutput,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        membership_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetTeamMembershipOutput:
        """
        Get a membership

        GET /v2/teams/{teamId}/memberships/{membershipId}

        Args:
            membershipId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.memberships.get(membership_id=123.0, team_id=123.0)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetTeamMembershipOutput,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        membership_id: float,
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
    ) -> models.UpdateTeamMembershipOutput:
        """
        Create a membership

        PATCH /v2/teams/{teamId}/memberships/{membershipId}

        Args:
            accepted: bool
            disableImpersonation: bool
            role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
            membershipId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.teams.memberships.patch(membership_id=123.0, team_id=123.0)
        ```
        """
        _json = to_encodable(
            item={
                "accepted": accepted,
                "disable_impersonation": disable_impersonation,
                "role": role,
            },
            dump_with=params._SerializerUpdateTeamMembershipInput,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateTeamMembershipOutput,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        team_id: float,
        user_id: float,
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
    ) -> models.CreateTeamMembershipOutput:
        """
        Create a membership

        POST /v2/teams/{teamId}/memberships

        Args:
            accepted: bool
            disableImpersonation: bool
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
        client.teams.memberships.create(team_id=123.0, user_id=123.0)
        ```
        """
        _json = to_encodable(
            item={
                "accepted": accepted,
                "disable_impersonation": disable_impersonation,
                "role": role,
                "user_id": user_id,
            },
            dump_with=params._SerializerCreateTeamMembershipInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/teams/{team_id}/memberships",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateTeamMembershipOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncMembershipsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        membership_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteTeamMembershipOutput:
        """
        Delete a membership

        DELETE /v2/teams/{teamId}/memberships/{membershipId}

        Args:
            membershipId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.memberships.delete(membership_id=123.0, team_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteTeamMembershipOutput,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        team_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetTeamMembershipsOutput:
        """
        Get all memberships

        GET /v2/teams/{teamId}/memberships

        Args:
            skip: The number of items to skip
            take: The number of items to return
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.memberships.list(team_id=123.0)
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
            path=f"/v2/teams/{team_id}/memberships",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetTeamMembershipsOutput,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        membership_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetTeamMembershipOutput:
        """
        Get a membership

        GET /v2/teams/{teamId}/memberships/{membershipId}

        Args:
            membershipId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.memberships.get(membership_id=123.0, team_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetTeamMembershipOutput,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        membership_id: float,
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
    ) -> models.UpdateTeamMembershipOutput:
        """
        Create a membership

        PATCH /v2/teams/{teamId}/memberships/{membershipId}

        Args:
            accepted: bool
            disableImpersonation: bool
            role: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
            membershipId: float
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.teams.memberships.patch(membership_id=123.0, team_id=123.0)
        ```
        """
        _json = to_encodable(
            item={
                "accepted": accepted,
                "disable_impersonation": disable_impersonation,
                "role": role,
            },
            dump_with=params._SerializerUpdateTeamMembershipInput,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/teams/{team_id}/memberships/{membership_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateTeamMembershipOutput,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        team_id: float,
        user_id: float,
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
    ) -> models.CreateTeamMembershipOutput:
        """
        Create a membership

        POST /v2/teams/{teamId}/memberships

        Args:
            accepted: bool
            disableImpersonation: bool
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
        await client.teams.memberships.create(team_id=123.0, user_id=123.0)
        ```
        """
        _json = to_encodable(
            item={
                "accepted": accepted,
                "disable_impersonation": disable_impersonation,
                "role": role,
                "user_id": user_id,
            },
            dump_with=params._SerializerCreateTeamMembershipInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/teams/{team_id}/memberships",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateTeamMembershipOutput,
            request_options=request_options or default_request_options(),
        )
