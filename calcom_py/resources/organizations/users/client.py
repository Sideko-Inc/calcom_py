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
from calcom_py.resources.organizations.users.ooo import AsyncOooClient, OooClient
from calcom_py.resources.organizations.users.schedules import (
    AsyncSchedulesClient,
    SchedulesClient,
)
from calcom_py.types import models, params


class UsersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.ooo = OooClient(base_client=self._base_client)
        self.schedules = SchedulesClient(base_client=self._base_client)

    def delete(
        self,
        *,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationUserOutput:
        """
        Delete a user

        DELETE /v2/organizations/{orgId}/users/{userId}

        Args:
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.delete(org_id=123.0, user_id=123.0)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetOrganizationUserOutput,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        org_id: float,
        emails: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationUsersResponseDto:
        """
        Get all users

        GET /v2/organizations/{orgId}/users

        Args:
            emails: The email address or an array of email addresses to filter by
            skip: The number of items to skip
            take: The number of items to return
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.list(org_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(emails, type_utils.NotGiven):
            encode_query_param(
                _query,
                "emails",
                to_encodable(item=emails, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
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
            path=f"/v2/organizations/{org_id}/users",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetOrganizationUsersResponseDto,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationUserOutput:
        """
        Update a user

        PATCH /v2/organizations/{orgId}/users/{userId}

        Args:
            data: typing.Dict[str, typing.Any]
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.patch(data={}, org_id=123.0, user_id=123.0)
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetOrganizationUserOutput,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        email_field: str,
        org_id: float,
        app_theme: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_accept: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        avatar_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dark_brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_schedule_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_branding: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        locale_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        organization_role: typing.Union[
            typing.Optional[typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        theme: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_format: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_zone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        weekday: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationUserOutput:
        """
        Create a user

        POST /v2/organizations/{orgId}/users

        Args:
            appTheme: Application theme
            autoAccept: bool
            avatarUrl: Avatar URL
            brandColor: Brand color in HEX format
            darkBrandColor: Dark brand color in HEX format
            defaultScheduleId: Default schedule ID
            hideBranding: Hide branding
            locale: Locale
            organizationRole: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
            theme: Theme
            timeFormat: Time format
            timeZone: Time zone
            username: Username
            weekday: Preferred weekday
            email: User email address
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.create(
            email_field="user@example.com",
            org_id=123.0,
            app_theme="light",
            avatar_url="https://example.com/avatar.jpg",
            brand_color="#FFFFFF",
            dark_brand_color="#000000",
            default_schedule_id=1.0,
            hide_branding=False,
            locale_field="en",
            theme="dark",
            time_format=24.0,
            time_zone="America/New_York",
            username="user123",
            weekday="Monday",
        )
        ```
        """
        _json = to_encodable(
            item={
                "app_theme": app_theme,
                "auto_accept": auto_accept,
                "avatar_url": avatar_url,
                "brand_color": brand_color,
                "dark_brand_color": dark_brand_color,
                "default_schedule_id": default_schedule_id,
                "hide_branding": hide_branding,
                "locale_field": locale_field,
                "organization_role": organization_role,
                "theme": theme,
                "time_format": time_format,
                "time_zone": time_zone,
                "username": username,
                "weekday": weekday,
                "email_field": email_field,
            },
            dump_with=params._SerializerCreateOrganizationUserInput,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/users",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetOrganizationUserOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncUsersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.ooo = AsyncOooClient(base_client=self._base_client)
        self.schedules = AsyncSchedulesClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationUserOutput:
        """
        Delete a user

        DELETE /v2/organizations/{orgId}/users/{userId}

        Args:
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.delete(org_id=123.0, user_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetOrganizationUserOutput,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        org_id: float,
        emails: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationUsersResponseDto:
        """
        Get all users

        GET /v2/organizations/{orgId}/users

        Args:
            emails: The email address or an array of email addresses to filter by
            skip: The number of items to skip
            take: The number of items to return
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.list(org_id=123.0)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(emails, type_utils.NotGiven):
            encode_query_param(
                _query,
                "emails",
                to_encodable(item=emails, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
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
            path=f"/v2/organizations/{org_id}/users",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.GetOrganizationUsersResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationUserOutput:
        """
        Update a user

        PATCH /v2/organizations/{orgId}/users/{userId}

        Args:
            data: typing.Dict[str, typing.Any]
            orgId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.patch(data={}, org_id=123.0, user_id=123.0)
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/users/{user_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetOrganizationUserOutput,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        email_field: str,
        org_id: float,
        app_theme: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_accept: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        avatar_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dark_brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_schedule_id: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_branding: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        locale_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        organization_role: typing.Union[
            typing.Optional[typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        theme: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_format: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        time_zone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        weekday: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetOrganizationUserOutput:
        """
        Create a user

        POST /v2/organizations/{orgId}/users

        Args:
            appTheme: Application theme
            autoAccept: bool
            avatarUrl: Avatar URL
            brandColor: Brand color in HEX format
            darkBrandColor: Dark brand color in HEX format
            defaultScheduleId: Default schedule ID
            hideBranding: Hide branding
            locale: Locale
            organizationRole: typing_extensions.Literal["ADMIN", "MEMBER", "OWNER"]
            theme: Theme
            timeFormat: Time format
            timeZone: Time zone
            username: Username
            weekday: Preferred weekday
            email: User email address
            orgId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.create(
            email_field="user@example.com",
            org_id=123.0,
            app_theme="light",
            avatar_url="https://example.com/avatar.jpg",
            brand_color="#FFFFFF",
            dark_brand_color="#000000",
            default_schedule_id=1.0,
            hide_branding=False,
            locale_field="en",
            theme="dark",
            time_format=24.0,
            time_zone="America/New_York",
            username="user123",
            weekday="Monday",
        )
        ```
        """
        _json = to_encodable(
            item={
                "app_theme": app_theme,
                "auto_accept": auto_accept,
                "avatar_url": avatar_url,
                "brand_color": brand_color,
                "dark_brand_color": dark_brand_color,
                "default_schedule_id": default_schedule_id,
                "hide_branding": hide_branding,
                "locale_field": locale_field,
                "organization_role": organization_role,
                "theme": theme,
                "time_format": time_format,
                "time_zone": time_zone,
                "username": username,
                "weekday": weekday,
                "email_field": email_field,
            },
            dump_with=params._SerializerCreateOrganizationUserInput,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/users",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.GetOrganizationUserOutput,
            request_options=request_options or default_request_options(),
        )
