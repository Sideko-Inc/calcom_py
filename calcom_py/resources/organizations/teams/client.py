import typing

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
from calcom_py.resources.organizations.teams.bookings import (
    AsyncBookingsClient,
    BookingsClient,
)
from calcom_py.resources.organizations.teams.event_types import (
    AsyncEventTypesClient,
    EventTypesClient,
)
from calcom_py.resources.organizations.teams.me import AsyncMeClient, MeClient
from calcom_py.resources.organizations.teams.memberships import (
    AsyncMembershipsClient,
    MembershipsClient,
)
from calcom_py.resources.organizations.teams.routing_forms import (
    AsyncRoutingFormsClient,
    RoutingFormsClient,
)
from calcom_py.resources.organizations.teams.users import AsyncUsersClient, UsersClient
from calcom_py.types import models, params


class TeamsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.event_types = EventTypesClient(base_client=self._base_client)
        self.memberships = MembershipsClient(base_client=self._base_client)
        self.me = MeClient(base_client=self._base_client)
        self.bookings = BookingsClient(base_client=self._base_client)
        self.routing_forms = RoutingFormsClient(base_client=self._base_client)
        self.users = UsersClient(base_client=self._base_client)

    def delete(
        self,
        *,
        org_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamOutputResponseDto:
        """
        Delete a team

        DELETE /v2/organizations/{orgId}/teams/{teamId}

        Args:
            orgId: float
            teamId: The team identifier
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.delete(org_id=123.0, team_id=123.0)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/teams/{team_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OrgTeamOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        org_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamsOutputResponseDto:
        """
        Get all teams

        GET /v2/organizations/{orgId}/teams

        Args:
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
        client.organizations.teams.list(org_id=123.0)
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
            path=f"/v2/organizations/{org_id}/teams",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.OrgTeamsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        org_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamOutputResponseDto:
        """
        Get a team

        GET /v2/organizations/{orgId}/teams/{teamId}

        Args:
            orgId: float
            teamId: The team identifier
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.get(org_id=123.0, team_id=123.0)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OrgTeamOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        org_id: float,
        team_id: float,
        app_icon_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        app_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        banner_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bio: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_limits: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cal_video_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dark_brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_book_a_team_member: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_branding: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        include_managed_events_in_limits: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_private: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        logo_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
        week_start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamOutputResponseDto:
        """
        Update a team

        PATCH /v2/organizations/{orgId}/teams/{teamId}

        Args:
            appIconLogo: str
            appLogo: str
            bannerUrl: URL of the teams banner image which is shown on booker
            bio: str
            bookingLimits: str
            brandColor: str
            calVideoLogo: str
            darkBrandColor: str
            hideBookATeamMember: bool
            hideBranding: bool
            includeManagedEventsInLimits: bool
            isPrivate: bool
            logoUrl: URL of the teams logo image
            metadata: You can store any additional data you want here.
        Metadata must have at most 50 keys, each key up to 40 characters.
        Values can be strings (up to 500 characters), numbers, or booleans.
            name: Name of the team
            slug: Team slug
            theme: str
            timeFormat: float
            timeZone: Timezone is used to create teams's default schedule from Monday to Friday from 9AM to 5PM. It will default to Europe/London if not passed.
            weekStart: str
            orgId: float
            teamId: The team identifier
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.patch(
            org_id=123.0,
            team_id=123.0,
            banner_url="https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png",
            logo_url="https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png",
            metadata={"key": "value"},
            name="CalTeam",
            slug="caltel",
            time_zone="America/New_York",
            week_start="Monday",
        )
        ```
        """
        _json = to_encodable(
            item={
                "app_icon_logo": app_icon_logo,
                "app_logo": app_logo,
                "banner_url": banner_url,
                "bio": bio,
                "booking_limits": booking_limits,
                "brand_color": brand_color,
                "cal_video_logo": cal_video_logo,
                "dark_brand_color": dark_brand_color,
                "hide_book_a_team_member": hide_book_a_team_member,
                "hide_branding": hide_branding,
                "include_managed_events_in_limits": include_managed_events_in_limits,
                "is_private": is_private,
                "logo_url": logo_url,
                "metadata": metadata,
                "name": name,
                "slug": slug,
                "theme": theme,
                "time_format": time_format,
                "time_zone": time_zone,
                "week_start": week_start,
            },
            dump_with=params._SerializerUpdateOrgTeamDto,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/teams/{team_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OrgTeamOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        org_id: float,
        x_cal_client_id: str,
        app_icon_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        app_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_accept_creator: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        banner_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bio: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cal_video_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dark_brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_book_a_team_member: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_branding: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_private: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        logo_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
        week_start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamOutputResponseDto:
        """
        Create a team

        POST /v2/organizations/{orgId}/teams

        Args:
            appIconLogo: str
            appLogo: str
            autoAcceptCreator: bool
            bannerUrl: URL of the teams banner image which is shown on booker
            bio: str
            brandColor: str
            calVideoLogo: str
            darkBrandColor: str
            hideBookATeamMember: bool
            hideBranding: bool
            isPrivate: bool
            logoUrl: URL of the teams logo image
            metadata: You can store any additional data you want here.
        Metadata must have at most 50 keys, each key up to 40 characters.
        Values can be strings (up to 500 characters), numbers, or booleans.
            slug: Team slug
            theme: str
            timeFormat: float
            timeZone: Timezone is used to create teams's default schedule from Monday to Friday from 9AM to 5PM. It will default to Europe/London if not passed.
            weekStart: str
            name: Name of the team
            orgId: float
            x-cal-client-id: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.create(
            name="CalTeam",
            org_id=123.0,
            x_cal_client_id="string",
            banner_url="https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png",
            logo_url="https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png",
            metadata={"key": "value"},
            slug="caltel",
            time_zone="America/New_York",
            week_start="Monday",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-cal-client-id"] = str(x_cal_client_id)
        _json = to_encodable(
            item={
                "app_icon_logo": app_icon_logo,
                "app_logo": app_logo,
                "auto_accept_creator": auto_accept_creator,
                "banner_url": banner_url,
                "bio": bio,
                "brand_color": brand_color,
                "cal_video_logo": cal_video_logo,
                "dark_brand_color": dark_brand_color,
                "hide_book_a_team_member": hide_book_a_team_member,
                "hide_branding": hide_branding,
                "is_private": is_private,
                "logo_url": logo_url,
                "metadata": metadata,
                "slug": slug,
                "theme": theme,
                "time_format": time_format,
                "time_zone": time_zone,
                "week_start": week_start,
                "name": name,
            },
            dump_with=params._SerializerCreateOrgTeamDto,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/teams",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.OrgTeamOutputResponseDto,
            request_options=request_options or default_request_options(),
        )


class AsyncTeamsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.event_types = AsyncEventTypesClient(base_client=self._base_client)
        self.memberships = AsyncMembershipsClient(base_client=self._base_client)
        self.me = AsyncMeClient(base_client=self._base_client)
        self.bookings = AsyncBookingsClient(base_client=self._base_client)
        self.routing_forms = AsyncRoutingFormsClient(base_client=self._base_client)
        self.users = AsyncUsersClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        org_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamOutputResponseDto:
        """
        Delete a team

        DELETE /v2/organizations/{orgId}/teams/{teamId}

        Args:
            orgId: float
            teamId: The team identifier
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.delete(org_id=123.0, team_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/teams/{team_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OrgTeamOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        org_id: float,
        skip: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        take: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamsOutputResponseDto:
        """
        Get all teams

        GET /v2/organizations/{orgId}/teams

        Args:
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
        await client.organizations.teams.list(org_id=123.0)
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
            path=f"/v2/organizations/{org_id}/teams",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.OrgTeamsOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        org_id: float,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamOutputResponseDto:
        """
        Get a team

        GET /v2/organizations/{orgId}/teams/{teamId}

        Args:
            orgId: float
            teamId: The team identifier
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.get(org_id=123.0, team_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}",
            auth_names=["bearerAuth"],
            cast_to=models.OrgTeamOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        org_id: float,
        team_id: float,
        app_icon_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        app_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        banner_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bio: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        booking_limits: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cal_video_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dark_brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_book_a_team_member: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_branding: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        include_managed_events_in_limits: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_private: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        logo_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
        week_start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamOutputResponseDto:
        """
        Update a team

        PATCH /v2/organizations/{orgId}/teams/{teamId}

        Args:
            appIconLogo: str
            appLogo: str
            bannerUrl: URL of the teams banner image which is shown on booker
            bio: str
            bookingLimits: str
            brandColor: str
            calVideoLogo: str
            darkBrandColor: str
            hideBookATeamMember: bool
            hideBranding: bool
            includeManagedEventsInLimits: bool
            isPrivate: bool
            logoUrl: URL of the teams logo image
            metadata: You can store any additional data you want here.
        Metadata must have at most 50 keys, each key up to 40 characters.
        Values can be strings (up to 500 characters), numbers, or booleans.
            name: Name of the team
            slug: Team slug
            theme: str
            timeFormat: float
            timeZone: Timezone is used to create teams's default schedule from Monday to Friday from 9AM to 5PM. It will default to Europe/London if not passed.
            weekStart: str
            orgId: float
            teamId: The team identifier
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.patch(
            org_id=123.0,
            team_id=123.0,
            banner_url="https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png",
            logo_url="https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png",
            metadata={"key": "value"},
            name="CalTeam",
            slug="caltel",
            time_zone="America/New_York",
            week_start="Monday",
        )
        ```
        """
        _json = to_encodable(
            item={
                "app_icon_logo": app_icon_logo,
                "app_logo": app_logo,
                "banner_url": banner_url,
                "bio": bio,
                "booking_limits": booking_limits,
                "brand_color": brand_color,
                "cal_video_logo": cal_video_logo,
                "dark_brand_color": dark_brand_color,
                "hide_book_a_team_member": hide_book_a_team_member,
                "hide_branding": hide_branding,
                "include_managed_events_in_limits": include_managed_events_in_limits,
                "is_private": is_private,
                "logo_url": logo_url,
                "metadata": metadata,
                "name": name,
                "slug": slug,
                "theme": theme,
                "time_format": time_format,
                "time_zone": time_zone,
                "week_start": week_start,
            },
            dump_with=params._SerializerUpdateOrgTeamDto,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/teams/{team_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.OrgTeamOutputResponseDto,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        org_id: float,
        x_cal_client_id: str,
        app_icon_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        app_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_accept_creator: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        banner_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bio: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cal_video_logo: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        dark_brand_color: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_book_a_team_member: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        hide_branding: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_private: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        logo_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Dict[str, typing.Any]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
        week_start: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OrgTeamOutputResponseDto:
        """
        Create a team

        POST /v2/organizations/{orgId}/teams

        Args:
            appIconLogo: str
            appLogo: str
            autoAcceptCreator: bool
            bannerUrl: URL of the teams banner image which is shown on booker
            bio: str
            brandColor: str
            calVideoLogo: str
            darkBrandColor: str
            hideBookATeamMember: bool
            hideBranding: bool
            isPrivate: bool
            logoUrl: URL of the teams logo image
            metadata: You can store any additional data you want here.
        Metadata must have at most 50 keys, each key up to 40 characters.
        Values can be strings (up to 500 characters), numbers, or booleans.
            slug: Team slug
            theme: str
            timeFormat: float
            timeZone: Timezone is used to create teams's default schedule from Monday to Friday from 9AM to 5PM. It will default to Europe/London if not passed.
            weekStart: str
            name: Name of the team
            orgId: float
            x-cal-client-id: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.create(
            name="CalTeam",
            org_id=123.0,
            x_cal_client_id="string",
            banner_url="https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png",
            logo_url="https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png",
            metadata={"key": "value"},
            slug="caltel",
            time_zone="America/New_York",
            week_start="Monday",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-cal-client-id"] = str(x_cal_client_id)
        _json = to_encodable(
            item={
                "app_icon_logo": app_icon_logo,
                "app_logo": app_logo,
                "auto_accept_creator": auto_accept_creator,
                "banner_url": banner_url,
                "bio": bio,
                "brand_color": brand_color,
                "cal_video_logo": cal_video_logo,
                "dark_brand_color": dark_brand_color,
                "hide_book_a_team_member": hide_book_a_team_member,
                "hide_branding": hide_branding,
                "is_private": is_private,
                "logo_url": logo_url,
                "metadata": metadata,
                "slug": slug,
                "theme": theme,
                "time_format": time_format,
                "time_zone": time_zone,
                "week_start": week_start,
                "name": name,
            },
            dump_with=params._SerializerCreateOrgTeamDto,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/teams",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.OrgTeamOutputResponseDto,
            request_options=request_options or default_request_options(),
        )
