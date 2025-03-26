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


class SchedulesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        org_id: float,
        schedule_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteScheduleOutput20240611:
        """
        Delete a schedule

        DELETE /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}

        Args:
            orgId: float
            scheduleId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.schedules.delete(
            org_id=123.0, schedule_id=123.0, user_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetSchedulesOutput20240611:
        """
        Get all schedules

        GET /v2/organizations/{orgId}/users/{userId}/schedules

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
        client.organizations.users.schedules.list(org_id=123.0, user_id=123.0)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules",
            auth_names=["bearerAuth"],
            cast_to=models.GetSchedulesOutput20240611,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        org_id: float,
        schedule_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetScheduleOutput20240611:
        """
        Get a schedule

        GET /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}

        Args:
            orgId: float
            scheduleId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.schedules.get(
            org_id=123.0, schedule_id=123.0, user_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        org_id: float,
        schedule_id: float,
        user_id: float,
        availability: typing.Union[
            typing.Optional[typing.List[params.ScheduleAvailabilityInput20240611]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        is_default: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        overrides: typing.Union[
            typing.Optional[typing.List[params.ScheduleOverrideInput20240611]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        time_zone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateScheduleOutput20240611:
        """
        Update a schedule

        PATCH /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}

        Args:
            availability: typing.List[ScheduleAvailabilityInput20240611]
            isDefault: bool
            name: str
            overrides: typing.List[ScheduleOverrideInput20240611]
            timeZone: str
            orgId: float
            scheduleId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.schedules.patch(
            org_id=123.0,
            schedule_id=123.0,
            user_id=123.0,
            availability=[
                {
                    "days": ["Monday", "Tuesday"],
                    "end_time": "10:00",
                    "start_time": "09:00",
                }
            ],
            is_default=True,
            name="One-on-one coaching",
            overrides=[
                {"date": "2024-05-20", "end_time": "14:00", "start_time": "12:00"}
            ],
            time_zone="Europe/Rome",
        )
        ```
        """
        _json = to_encodable(
            item={
                "availability": availability,
                "is_default": is_default,
                "name": name,
                "overrides": overrides,
                "time_zone": time_zone,
            },
            dump_with=params._SerializerUpdateScheduleInput20240611,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        is_default: bool,
        name: str,
        org_id: float,
        time_zone: str,
        user_id: float,
        availability: typing.Union[
            typing.Optional[typing.List[params.ScheduleAvailabilityInput20240611]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        overrides: typing.Union[
            typing.Optional[typing.List[params.ScheduleOverrideInput20240611]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateScheduleOutput20240611:
        """
        Create a schedule

        POST /v2/organizations/{orgId}/users/{userId}/schedules

        Args:
            availability: Each object contains days and times when the user is available. If not passed, the default availability is Monday to Friday from 09:00 to 17:00.
            overrides: Need to change availability for a specific date? Add an override.
            isDefault: Each user should have 1 default schedule. If you specified `timeZone` when creating managed user, then the default schedule will be created with that timezone.
            Default schedule means that if an event type is not tied to a specific schedule then the default schedule is used.
            name: str
            orgId: float
            timeZone: Timezone is used to calculate available times when an event using the schedule is booked.
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.users.schedules.create(
            is_default=True,
            name="Catch up hours",
            org_id=123.0,
            time_zone="Europe/Rome",
            user_id=123.0,
            availability=[
                {
                    "days": ["Monday", "Tuesday"],
                    "end_time": "19:00",
                    "start_time": "17:00",
                },
                {
                    "days": ["Wednesday", "Thursday"],
                    "end_time": "20:00",
                    "start_time": "16:00",
                },
            ],
            overrides=[
                {"date": "2024-05-20", "end_time": "21:00", "start_time": "18:00"}
            ],
        )
        ```
        """
        _json = to_encodable(
            item={
                "availability": availability,
                "overrides": overrides,
                "is_default": is_default,
                "name": name,
                "time_zone": time_zone,
            },
            dump_with=params._SerializerCreateScheduleInput20240611,
        )
        return self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )


class AsyncSchedulesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        org_id: float,
        schedule_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteScheduleOutput20240611:
        """
        Delete a schedule

        DELETE /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}

        Args:
            orgId: float
            scheduleId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.schedules.delete(
            org_id=123.0, schedule_id=123.0, user_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeleteScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        org_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetSchedulesOutput20240611:
        """
        Get all schedules

        GET /v2/organizations/{orgId}/users/{userId}/schedules

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
        await client.organizations.users.schedules.list(org_id=123.0, user_id=123.0)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules",
            auth_names=["bearerAuth"],
            cast_to=models.GetSchedulesOutput20240611,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        org_id: float,
        schedule_id: float,
        user_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetScheduleOutput20240611:
        """
        Get a schedule

        GET /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}

        Args:
            orgId: float
            scheduleId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.schedules.get(
            org_id=123.0, schedule_id=123.0, user_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            cast_to=models.GetScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        org_id: float,
        schedule_id: float,
        user_id: float,
        availability: typing.Union[
            typing.Optional[typing.List[params.ScheduleAvailabilityInput20240611]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        is_default: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        overrides: typing.Union[
            typing.Optional[typing.List[params.ScheduleOverrideInput20240611]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        time_zone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.UpdateScheduleOutput20240611:
        """
        Update a schedule

        PATCH /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}

        Args:
            availability: typing.List[ScheduleAvailabilityInput20240611]
            isDefault: bool
            name: str
            overrides: typing.List[ScheduleOverrideInput20240611]
            timeZone: str
            orgId: float
            scheduleId: float
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.schedules.patch(
            org_id=123.0,
            schedule_id=123.0,
            user_id=123.0,
            availability=[
                {
                    "days": ["Monday", "Tuesday"],
                    "end_time": "10:00",
                    "start_time": "09:00",
                }
            ],
            is_default=True,
            name="One-on-one coaching",
            overrides=[
                {"date": "2024-05-20", "end_time": "14:00", "start_time": "12:00"}
            ],
            time_zone="Europe/Rome",
        )
        ```
        """
        _json = to_encodable(
            item={
                "availability": availability,
                "is_default": is_default,
                "name": name,
                "overrides": overrides,
                "time_zone": time_zone,
            },
            dump_with=params._SerializerUpdateScheduleInput20240611,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.UpdateScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        is_default: bool,
        name: str,
        org_id: float,
        time_zone: str,
        user_id: float,
        availability: typing.Union[
            typing.Optional[typing.List[params.ScheduleAvailabilityInput20240611]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        overrides: typing.Union[
            typing.Optional[typing.List[params.ScheduleOverrideInput20240611]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreateScheduleOutput20240611:
        """
        Create a schedule

        POST /v2/organizations/{orgId}/users/{userId}/schedules

        Args:
            availability: Each object contains days and times when the user is available. If not passed, the default availability is Monday to Friday from 09:00 to 17:00.
            overrides: Need to change availability for a specific date? Add an override.
            isDefault: Each user should have 1 default schedule. If you specified `timeZone` when creating managed user, then the default schedule will be created with that timezone.
            Default schedule means that if an event type is not tied to a specific schedule then the default schedule is used.
            name: str
            orgId: float
            timeZone: Timezone is used to calculate available times when an event using the schedule is booked.
            userId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.users.schedules.create(
            is_default=True,
            name="Catch up hours",
            org_id=123.0,
            time_zone="Europe/Rome",
            user_id=123.0,
            availability=[
                {
                    "days": ["Monday", "Tuesday"],
                    "end_time": "19:00",
                    "start_time": "17:00",
                },
                {
                    "days": ["Wednesday", "Thursday"],
                    "end_time": "20:00",
                    "start_time": "16:00",
                },
            ],
            overrides=[
                {"date": "2024-05-20", "end_time": "21:00", "start_time": "18:00"}
            ],
        )
        ```
        """
        _json = to_encodable(
            item={
                "availability": availability,
                "overrides": overrides,
                "is_default": is_default,
                "name": name,
                "time_zone": time_zone,
            },
            dump_with=params._SerializerCreateScheduleInput20240611,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v2/organizations/{org_id}/users/{user_id}/schedules",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.CreateScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )
