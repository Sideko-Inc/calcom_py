import httpx
import typing

from calcom_py.core import AsyncBaseClient, AuthBearer, SyncBaseClient
from calcom_py.environment import Environment
from calcom_py.resources.api_keys import ApiKeysClient, AsyncApiKeysClient
from calcom_py.resources.bookings import AsyncBookingsClient, BookingsClient
from calcom_py.resources.calendars import AsyncCalendarsClient, CalendarsClient
from calcom_py.resources.conferencing import AsyncConferencingClient, ConferencingClient
from calcom_py.resources.destination_calendars import (
    AsyncDestinationCalendarsClient,
    DestinationCalendarsClient,
)
from calcom_py.resources.event_types import AsyncEventTypesClient, EventTypesClient
from calcom_py.resources.me import AsyncMeClient, MeClient
from calcom_py.resources.oauth import AsyncOauthClient, OauthClient
from calcom_py.resources.oauth_clients import (
    AsyncOauthClientsClient,
    OauthClientsClient,
)
from calcom_py.resources.organizations import (
    AsyncOrganizationsClient,
    OrganizationsClient,
)
from calcom_py.resources.provider import AsyncProviderClient, ProviderClient
from calcom_py.resources.schedules import AsyncSchedulesClient, SchedulesClient
from calcom_py.resources.selected_calendars import (
    AsyncSelectedCalendarsClient,
    SelectedCalendarsClient,
)
from calcom_py.resources.slots import AsyncSlotsClient, SlotsClient
from calcom_py.resources.stripe import AsyncStripeClient, StripeClient
from calcom_py.resources.teams import AsyncTeamsClient, TeamsClient
from calcom_py.resources.timezones import AsyncTimezonesClient, TimezonesClient
from calcom_py.resources.webhooks import AsyncWebhooksClient, WebhooksClient


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: Environment = Environment.DEFAULT,
        api_key: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("bearerAuth", AuthBearer(val=api_key))
        self.conferencing = ConferencingClient(base_client=self._base_client)
        self.event_types = EventTypesClient(base_client=self._base_client)
        self.oauth_clients = OauthClientsClient(base_client=self._base_client)
        self.organizations = OrganizationsClient(base_client=self._base_client)
        self.schedules = SchedulesClient(base_client=self._base_client)
        self.selected_calendars = SelectedCalendarsClient(base_client=self._base_client)
        self.slots = SlotsClient(base_client=self._base_client)
        self.teams = TeamsClient(base_client=self._base_client)
        self.webhooks = WebhooksClient(base_client=self._base_client)
        self.bookings = BookingsClient(base_client=self._base_client)
        self.calendars = CalendarsClient(base_client=self._base_client)
        self.me = MeClient(base_client=self._base_client)
        self.provider = ProviderClient(base_client=self._base_client)
        self.stripe = StripeClient(base_client=self._base_client)
        self.timezones = TimezonesClient(base_client=self._base_client)
        self.api_keys = ApiKeysClient(base_client=self._base_client)
        self.oauth = OauthClient(base_client=self._base_client)
        self.destination_calendars = DestinationCalendarsClient(
            base_client=self._base_client
        )


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: Environment = Environment.DEFAULT,
        api_key: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("bearerAuth", AuthBearer(val=api_key))
        self.conferencing = AsyncConferencingClient(base_client=self._base_client)
        self.event_types = AsyncEventTypesClient(base_client=self._base_client)
        self.oauth_clients = AsyncOauthClientsClient(base_client=self._base_client)
        self.organizations = AsyncOrganizationsClient(base_client=self._base_client)
        self.schedules = AsyncSchedulesClient(base_client=self._base_client)
        self.selected_calendars = AsyncSelectedCalendarsClient(
            base_client=self._base_client
        )
        self.slots = AsyncSlotsClient(base_client=self._base_client)
        self.teams = AsyncTeamsClient(base_client=self._base_client)
        self.webhooks = AsyncWebhooksClient(base_client=self._base_client)
        self.bookings = AsyncBookingsClient(base_client=self._base_client)
        self.calendars = AsyncCalendarsClient(base_client=self._base_client)
        self.me = AsyncMeClient(base_client=self._base_client)
        self.provider = AsyncProviderClient(base_client=self._base_client)
        self.stripe = AsyncStripeClient(base_client=self._base_client)
        self.timezones = AsyncTimezonesClient(base_client=self._base_client)
        self.api_keys = AsyncApiKeysClient(base_client=self._base_client)
        self.oauth = AsyncOauthClient(base_client=self._base_client)
        self.destination_calendars = AsyncDestinationCalendarsClient(
            base_client=self._base_client
        )


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")
