import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from calcom_py.resources.schedules.default import AsyncDefaultClient, DefaultClient
from calcom_py.types import models, params


class SchedulesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.default = DefaultClient(base_client=self._base_client)

    def delete(
        self,
        *,
        cal_api_version: str,
        schedule_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteScheduleOutput20240611:
        """
        Delete a schedule

        DELETE /v2/schedules/{scheduleId}

        Args:
            cal-api-version: Must be set to 2024-06-11
            scheduleId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.schedules.delete(cal_api_version="string", schedule_id=123.0)
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="DELETE",
            path=f"/v2/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.DeleteScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetSchedulesOutput20240611:
        """
        Get all schedules

        Get all schedules of the authenticated user.

        GET /v2/schedules

        Args:
            cal-api-version: Must be set to 2024-06-11
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.schedules.list(cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="GET",
            path="/v2/schedules",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetSchedulesOutput20240611,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        cal_api_version: str,
        schedule_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetScheduleOutput20240611:
        """
        Get a schedule

        GET /v2/schedules/{scheduleId}

        Args:
            cal-api-version: Must be set to 2024-06-11
            scheduleId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.schedules.get(cal_api_version="string", schedule_id=123.0)
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return self._base_client.request(
            method="GET",
            path=f"/v2/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        cal_api_version: str,
        schedule_id: str,
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

        PATCH /v2/schedules/{scheduleId}

        Args:
            availability: typing.List[ScheduleAvailabilityInput20240611]
            isDefault: bool
            name: str
            overrides: typing.List[ScheduleOverrideInput20240611]
            timeZone: str
            cal-api-version: Must be set to 2024-06-11
            scheduleId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.schedules.patch(
            cal_api_version="string",
            schedule_id="string",
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
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
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
            path=f"/v2/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.UpdateScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        cal_api_version: str,
        is_default: bool,
        name: str,
        time_zone: str,
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


              Create a schedule for the authenticated user.

              The point of creating schedules is for event types to be available at specific times.

              The first goal of schedules is to have a default schedule. If you are platform customer and created managed users, then it is important to note that each managed user should have a default schedule.
              1. If you passed `timeZone` when creating managed user, then the default schedule from Monday to Friday from 9AM to 5PM will be created with that timezone. The managed user can then change the default schedule via the `AvailabilitySettings` atom.
              2. If you did not, then we assume you want the user to have this specific schedule right away. You should create a default schedule by specifying
              `"isDefault": true` in the request body. Until the user has a default schedule the user can't be booked nor manage their schedule via the AvailabilitySettings atom.

              The second goal of schedules is to create another schedule that event types can point to. This is useful for when an event is booked because availability is not checked against the default schedule but instead against that specific schedule.
              After creating a non-default schedule, you can update an event type to point to that schedule via the PATCH `event-types/{eventTypeId}` endpoint.

              When specifying start time and end time for each day use the 24 hour format e.g. 08:00, 15:00 etc.


        POST /v2/schedules

        Args:
            availability: Each object contains days and times when the user is available. If not passed, the default availability is Monday to Friday from 09:00 to 17:00.
            overrides: Need to change availability for a specific date? Add an override.
            cal-api-version: Must be set to 2024-06-11
            isDefault: Each user should have 1 default schedule. If you specified `timeZone` when creating managed user, then the default schedule will be created with that timezone.
            Default schedule means that if an event type is not tied to a specific schedule then the default schedule is used.
            name: str
            timeZone: Timezone is used to calculate available times when an event using the schedule is booked.
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.schedules.create(
            cal_api_version="string",
            is_default=True,
            name="Catch up hours",
            time_zone="Europe/Rome",
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
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
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
            path="/v2/schedules",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.CreateScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )


class AsyncSchedulesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.default = AsyncDefaultClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        cal_api_version: str,
        schedule_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeleteScheduleOutput20240611:
        """
        Delete a schedule

        DELETE /v2/schedules/{scheduleId}

        Args:
            cal-api-version: Must be set to 2024-06-11
            scheduleId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.schedules.delete(cal_api_version="string", schedule_id=123.0)
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="DELETE",
            path=f"/v2/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.DeleteScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        cal_api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetSchedulesOutput20240611:
        """
        Get all schedules

        Get all schedules of the authenticated user.

        GET /v2/schedules

        Args:
            cal-api-version: Must be set to 2024-06-11
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.schedules.list(cal_api_version="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="GET",
            path="/v2/schedules",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetSchedulesOutput20240611,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        cal_api_version: str,
        schedule_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetScheduleOutput20240611:
        """
        Get a schedule

        GET /v2/schedules/{scheduleId}

        Args:
            cal-api-version: Must be set to 2024-06-11
            scheduleId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.schedules.get(cal_api_version="string", schedule_id=123.0)
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
        return await self._base_client.request(
            method="GET",
            path=f"/v2/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            headers=_header,
            cast_to=models.GetScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        cal_api_version: str,
        schedule_id: str,
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

        PATCH /v2/schedules/{scheduleId}

        Args:
            availability: typing.List[ScheduleAvailabilityInput20240611]
            isDefault: bool
            name: str
            overrides: typing.List[ScheduleOverrideInput20240611]
            timeZone: str
            cal-api-version: Must be set to 2024-06-11
            scheduleId: str
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.schedules.patch(
            cal_api_version="string",
            schedule_id="string",
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
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
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
            path=f"/v2/schedules/{schedule_id}",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.UpdateScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        cal_api_version: str,
        is_default: bool,
        name: str,
        time_zone: str,
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


              Create a schedule for the authenticated user.

              The point of creating schedules is for event types to be available at specific times.

              The first goal of schedules is to have a default schedule. If you are platform customer and created managed users, then it is important to note that each managed user should have a default schedule.
              1. If you passed `timeZone` when creating managed user, then the default schedule from Monday to Friday from 9AM to 5PM will be created with that timezone. The managed user can then change the default schedule via the `AvailabilitySettings` atom.
              2. If you did not, then we assume you want the user to have this specific schedule right away. You should create a default schedule by specifying
              `"isDefault": true` in the request body. Until the user has a default schedule the user can't be booked nor manage their schedule via the AvailabilitySettings atom.

              The second goal of schedules is to create another schedule that event types can point to. This is useful for when an event is booked because availability is not checked against the default schedule but instead against that specific schedule.
              After creating a non-default schedule, you can update an event type to point to that schedule via the PATCH `event-types/{eventTypeId}` endpoint.

              When specifying start time and end time for each day use the 24 hour format e.g. 08:00, 15:00 etc.


        POST /v2/schedules

        Args:
            availability: Each object contains days and times when the user is available. If not passed, the default availability is Monday to Friday from 09:00 to 17:00.
            overrides: Need to change availability for a specific date? Add an override.
            cal-api-version: Must be set to 2024-06-11
            isDefault: Each user should have 1 default schedule. If you specified `timeZone` when creating managed user, then the default schedule will be created with that timezone.
            Default schedule means that if an event type is not tied to a specific schedule then the default schedule is used.
            name: str
            timeZone: Timezone is used to calculate available times when an event using the schedule is booked.
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.schedules.create(
            cal_api_version="string",
            is_default=True,
            name="Catch up hours",
            time_zone="Europe/Rome",
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
        _header: typing.Dict[str, str] = {}
        _header["cal-api-version"] = str(cal_api_version)
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
            path="/v2/schedules",
            auth_names=["bearerAuth"],
            headers=_header,
            json=_json,
            cast_to=models.CreateScheduleOutput20240611,
            request_options=request_options or default_request_options(),
        )
