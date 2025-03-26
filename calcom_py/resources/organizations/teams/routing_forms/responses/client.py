import typing

from calcom_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from calcom_py.types import models


class ResponsesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        org_id: float,
        routing_form_id: str,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetRoutingFormResponsesOutput:
        """
        Get routing form responses

        GET /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{routingFormId}/responses

        Args:
            orgId: float
            routingFormId: str
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organizations.teams.routing_forms.responses.list(
            org_id=123.0, routing_form_id="string", team_id=123.0
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/routing-forms/{routing_form_id}/responses",
            auth_names=["bearerAuth"],
            cast_to=models.GetRoutingFormResponsesOutput,
            request_options=request_options or default_request_options(),
        )


class AsyncResponsesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        org_id: float,
        routing_form_id: str,
        team_id: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetRoutingFormResponsesOutput:
        """
        Get routing form responses

        GET /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{routingFormId}/responses

        Args:
            orgId: float
            routingFormId: str
            teamId: float
            request_options: Additional options to customize the HTTP request

        Returns:


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organizations.teams.routing_forms.responses.list(
            org_id=123.0, routing_form_id="string", team_id=123.0
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/v2/organizations/{org_id}/teams/{team_id}/routing-forms/{routing_form_id}/responses",
            auth_names=["bearerAuth"],
            cast_to=models.GetRoutingFormResponsesOutput,
            request_options=request_options or default_request_options(),
        )
