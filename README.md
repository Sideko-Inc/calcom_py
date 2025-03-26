
# Cal.com API v2 Python SDK

### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
```

### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
```

## Module Documentation and Snippets

### [api_keys.refresh](calcom_py/resources/api_keys/refresh/README.md)

* [create](calcom_py/resources/api_keys/refresh/README.md#create) - Refresh API Key

### [bookings](calcom_py/resources/bookings/README.md)

* [cancel](calcom_py/resources/bookings/README.md#cancel) - Cancel a booking
* [confirm](calcom_py/resources/bookings/README.md#confirm) - Confirm booking that requires a confirmation
* [create](calcom_py/resources/bookings/README.md#create) - Create a booking
* [decline](calcom_py/resources/bookings/README.md#decline) - Decline booking that requires a confirmation
* [get](calcom_py/resources/bookings/README.md#get) - Get a booking
* [list](calcom_py/resources/bookings/README.md#list) - Get all bookings
* [mark_absent](calcom_py/resources/bookings/README.md#mark_absent) - Mark a booking absence
* [reassign](calcom_py/resources/bookings/README.md#reassign) - Automatically reassign booking to a new host
* [reassign_to_user](calcom_py/resources/bookings/README.md#reassign_to_user) - Reassign a booking to a specific user
* [reschedule](calcom_py/resources/bookings/README.md#reschedule) - Reschedule a booking

### [bookings.calendar_links](calcom_py/resources/bookings/calendar_links/README.md)

* [list](calcom_py/resources/bookings/calendar_links/README.md#list) - Get 'Add to Calendar' links for a booking

### [calendars](calcom_py/resources/calendars/README.md)

* [check](calcom_py/resources/calendars/README.md#check) - Check a calendar connection
* [connect](calcom_py/resources/calendars/README.md#connect) - Get oAuth connect URL
* [disconnect](calcom_py/resources/calendars/README.md#disconnect) - Disconnect a calendar
* [get_busy](calcom_py/resources/calendars/README.md#get_busy) - Get busy times
* [list](calcom_py/resources/calendars/README.md#list) - Get all calendars
* [save](calcom_py/resources/calendars/README.md#save) - Save an oAuth calendar credentials

### [calendars.credentials](calcom_py/resources/calendars/credentials/README.md)

* [create](calcom_py/resources/calendars/credentials/README.md#create) - Sync credentials

### [calendars.ics_feed](calcom_py/resources/calendars/ics_feed/README.md)

* [check](calcom_py/resources/calendars/ics_feed/README.md#check) - Check an ICS feed
* [save](calcom_py/resources/calendars/ics_feed/README.md#save) - Save an ICS feed

### [conferencing](calcom_py/resources/conferencing/README.md)

* [connect](calcom_py/resources/conferencing/README.md#connect) - Connect your conferencing application
* [default](calcom_py/resources/conferencing/README.md#default) - Set your default conferencing application
* [disconnect](calcom_py/resources/conferencing/README.md#disconnect) - Disconnect your conferencing application
* [list](calcom_py/resources/conferencing/README.md#list) - List your conferencing applications
* [list_1](calcom_py/resources/conferencing/README.md#list_1) - Get your default conferencing application

### [conferencing.oauth](calcom_py/resources/conferencing/oauth/README.md)

* [auth_url](calcom_py/resources/conferencing/oauth/README.md#auth_url) - Get OAuth conferencing app auth url
* [callback](calcom_py/resources/conferencing/oauth/README.md#callback) - conferencing apps oauths callback

### [destination_calendars](calcom_py/resources/destination_calendars/README.md)

* [update](calcom_py/resources/destination_calendars/README.md#update) - Update destination calendars

### [event_types](calcom_py/resources/event_types/README.md)

* [create](calcom_py/resources/event_types/README.md#create) - Create an event type
* [delete](calcom_py/resources/event_types/README.md#delete) - Delete an event type
* [get](calcom_py/resources/event_types/README.md#get) - Get an event type
* [list](calcom_py/resources/event_types/README.md#list) - Get all event types
* [patch](calcom_py/resources/event_types/README.md#patch) - Update an event type

### [event_types.webhooks](calcom_py/resources/event_types/webhooks/README.md)

* [create](calcom_py/resources/event_types/webhooks/README.md#create) - Create a webhook
* [delete](calcom_py/resources/event_types/webhooks/README.md#delete) - Delete a webhook
* [delete_all](calcom_py/resources/event_types/webhooks/README.md#delete_all) - Delete all webhooks
* [get](calcom_py/resources/event_types/webhooks/README.md#get) - Get a webhook
* [list](calcom_py/resources/event_types/webhooks/README.md#list) - Get all webhooks
* [patch](calcom_py/resources/event_types/webhooks/README.md#patch) - Update a webhook

### [me](calcom_py/resources/me/README.md)

* [get](calcom_py/resources/me/README.md#get) - Get my profile
* [patch](calcom_py/resources/me/README.md#patch) - Update my profile

### [oauth](calcom_py/resources/oauth/README.md)

* [refresh](calcom_py/resources/oauth/README.md#refresh) - Refresh managed user tokens

### [oauth_clients](calcom_py/resources/oauth_clients/README.md)

* [create](calcom_py/resources/oauth_clients/README.md#create) - POST /v2/oauth-clients
* [delete](calcom_py/resources/oauth_clients/README.md#delete) - DELETE /v2/oauth-clients/{clientId}
* [get](calcom_py/resources/oauth_clients/README.md#get) - GET /v2/oauth-clients/{clientId}
* [list](calcom_py/resources/oauth_clients/README.md#list) - GET /v2/oauth-clients
* [patch](calcom_py/resources/oauth_clients/README.md#patch) - PATCH /v2/oauth-clients/{clientId}

### [oauth_clients.managed_users](calcom_py/resources/oauth_clients/managed_users/README.md)

* [list](calcom_py/resources/oauth_clients/managed_users/README.md#list) - GET /v2/oauth-clients/{clientId}/managed-users

### [oauth_clients.users](calcom_py/resources/oauth_clients/users/README.md)

* [create](calcom_py/resources/oauth_clients/users/README.md#create) - Create a managed user
* [delete](calcom_py/resources/oauth_clients/users/README.md#delete) - Delete a managed user
* [get](calcom_py/resources/oauth_clients/users/README.md#get) - Get a managed user
* [list](calcom_py/resources/oauth_clients/users/README.md#list) - Get all managed users
* [patch](calcom_py/resources/oauth_clients/users/README.md#patch) - Update a managed user

### [oauth_clients.users.force_refresh](calcom_py/resources/oauth_clients/users/force_refresh/README.md)

* [create](calcom_py/resources/oauth_clients/users/force_refresh/README.md#create) - Force refresh tokens

### [oauth_clients.webhooks](calcom_py/resources/oauth_clients/webhooks/README.md)

* [create](calcom_py/resources/oauth_clients/webhooks/README.md#create) - Create a webhook
* [delete](calcom_py/resources/oauth_clients/webhooks/README.md#delete) - Delete a webhook
* [delete_all](calcom_py/resources/oauth_clients/webhooks/README.md#delete_all) - Delete all webhooks
* [get](calcom_py/resources/oauth_clients/webhooks/README.md#get) - Get a webhook
* [list](calcom_py/resources/oauth_clients/webhooks/README.md#list) - Get all webhooks
* [patch](calcom_py/resources/oauth_clients/webhooks/README.md#patch) - Update a webhook

### [organizations](calcom_py/resources/organizations/README.md)

* [create](calcom_py/resources/organizations/README.md#create) - Create an organization within an organization
* [delete](calcom_py/resources/organizations/README.md#delete) - Delete an organization within an organization
* [get](calcom_py/resources/organizations/README.md#get) - Get an organization within an organization
* [list](calcom_py/resources/organizations/README.md#list) - Get all organizations within an organization
* [patch](calcom_py/resources/organizations/README.md#patch) - Update an organization within an organization

### [organizations.attributes](calcom_py/resources/organizations/attributes/README.md)

* [create](calcom_py/resources/organizations/attributes/README.md#create) - Create an attribute
* [delete](calcom_py/resources/organizations/attributes/README.md#delete) - Delete an attribute
* [get](calcom_py/resources/organizations/attributes/README.md#get) - Get an attribute
* [list](calcom_py/resources/organizations/attributes/README.md#list) - Get all attributes
* [patch](calcom_py/resources/organizations/attributes/README.md#patch) - Update an attribute

### [organizations.attributes.options](calcom_py/resources/organizations/attributes/options/README.md)

* [create](calcom_py/resources/organizations/attributes/options/README.md#create) - Create an attribute option
* [create_to_user](calcom_py/resources/organizations/attributes/options/README.md#create_to_user) - Assign an attribute to a user
* [delete](calcom_py/resources/organizations/attributes/options/README.md#delete) - Delete an attribute option
* [delete_from_user](calcom_py/resources/organizations/attributes/options/README.md#delete_from_user) - Unassign an attribute from a user
* [get](calcom_py/resources/organizations/attributes/options/README.md#get) - Get all attribute options for a user
* [list](calcom_py/resources/organizations/attributes/options/README.md#list) - Get all attribute options
* [patch](calcom_py/resources/organizations/attributes/options/README.md#patch) - Update an attribute option

### [organizations.delegation_credentials](calcom_py/resources/organizations/delegation_credentials/README.md)

* [create](calcom_py/resources/organizations/delegation_credentials/README.md#create) - Save delegation credentials for your organization.
* [patch](calcom_py/resources/organizations/delegation_credentials/README.md#patch) - Update delegation credentials of your organization.

### [organizations.memberships](calcom_py/resources/organizations/memberships/README.md)

* [create](calcom_py/resources/organizations/memberships/README.md#create) - Create a membership
* [delete](calcom_py/resources/organizations/memberships/README.md#delete) - Delete a membership
* [get](calcom_py/resources/organizations/memberships/README.md#get) - Get a membership
* [list](calcom_py/resources/organizations/memberships/README.md#list) - Get all memberships
* [patch](calcom_py/resources/organizations/memberships/README.md#patch) - Update a membership

### [organizations.ooo](calcom_py/resources/organizations/ooo/README.md)

* [get](calcom_py/resources/organizations/ooo/README.md#get) - Get all OOO entries of org users

### [organizations.schedules](calcom_py/resources/organizations/schedules/README.md)

* [list](calcom_py/resources/organizations/schedules/README.md#list) - Get all schedules

### [organizations.teams](calcom_py/resources/organizations/teams/README.md)

* [create](calcom_py/resources/organizations/teams/README.md#create) - Create a team
* [delete](calcom_py/resources/organizations/teams/README.md#delete) - Delete a team
* [get](calcom_py/resources/organizations/teams/README.md#get) - Get a team
* [list](calcom_py/resources/organizations/teams/README.md#list) - Get all teams
* [patch](calcom_py/resources/organizations/teams/README.md#patch) - Update a team

### [organizations.teams.bookings](calcom_py/resources/organizations/teams/bookings/README.md)

* [list](calcom_py/resources/organizations/teams/bookings/README.md#list) - Get organization team bookings

### [organizations.teams.event_types](calcom_py/resources/organizations/teams/event_types/README.md)

* [create](calcom_py/resources/organizations/teams/event_types/README.md#create) - Create an event type
* [create_phone_call](calcom_py/resources/organizations/teams/event_types/README.md#create_phone_call) - Create a phone call
* [delete](calcom_py/resources/organizations/teams/event_types/README.md#delete) - Delete a team event type
* [get_one](calcom_py/resources/organizations/teams/event_types/README.md#get_one) - Get an event type
* [list](calcom_py/resources/organizations/teams/event_types/README.md#list) - Get a team event type
* [list_for_team](calcom_py/resources/organizations/teams/event_types/README.md#list_for_team) - Get all team event types
* [patch](calcom_py/resources/organizations/teams/event_types/README.md#patch) - Update a team event type

### [organizations.teams.me](calcom_py/resources/organizations/teams/me/README.md)

* [get](calcom_py/resources/organizations/teams/me/README.md#get) - Get teams membership for user

### [organizations.teams.memberships](calcom_py/resources/organizations/teams/memberships/README.md)

* [create](calcom_py/resources/organizations/teams/memberships/README.md#create) - Create a membership
* [delete](calcom_py/resources/organizations/teams/memberships/README.md#delete) - Delete a membership
* [get](calcom_py/resources/organizations/teams/memberships/README.md#get) - Get a membership
* [list](calcom_py/resources/organizations/teams/memberships/README.md#list) - Get all memberships
* [patch](calcom_py/resources/organizations/teams/memberships/README.md#patch) - Update a membership

### [organizations.teams.routing_forms.responses](calcom_py/resources/organizations/teams/routing_forms/responses/README.md)

* [list](calcom_py/resources/organizations/teams/routing_forms/responses/README.md#list) - Get routing form responses

### [organizations.teams.users.schedules](calcom_py/resources/organizations/teams/users/schedules/README.md)

* [list](calcom_py/resources/organizations/teams/users/schedules/README.md#list) - Get schedules of a team member

### [organizations.users](calcom_py/resources/organizations/users/README.md)

* [create](calcom_py/resources/organizations/users/README.md#create) - Create a user
* [delete](calcom_py/resources/organizations/users/README.md#delete) - Delete a user
* [list](calcom_py/resources/organizations/users/README.md#list) - Get all users
* [patch](calcom_py/resources/organizations/users/README.md#patch) - Update a user

### [organizations.users.ooo](calcom_py/resources/organizations/users/ooo/README.md)

* [create](calcom_py/resources/organizations/users/ooo/README.md#create) - Create an ooo entry for user
* [delete](calcom_py/resources/organizations/users/ooo/README.md#delete) - Delete ooo entry of a user
* [list](calcom_py/resources/organizations/users/ooo/README.md#list) - Get all ooo entries of a user
* [patch](calcom_py/resources/organizations/users/ooo/README.md#patch) - Update ooo entry of a user

### [organizations.users.schedules](calcom_py/resources/organizations/users/schedules/README.md)

* [create](calcom_py/resources/organizations/users/schedules/README.md#create) - Create a schedule
* [delete](calcom_py/resources/organizations/users/schedules/README.md#delete) - Delete a schedule
* [get](calcom_py/resources/organizations/users/schedules/README.md#get) - Get a schedule
* [list](calcom_py/resources/organizations/users/schedules/README.md#list) - Get all schedules
* [patch](calcom_py/resources/organizations/users/schedules/README.md#patch) - Update a schedule

### [organizations.webhooks](calcom_py/resources/organizations/webhooks/README.md)

* [create](calcom_py/resources/organizations/webhooks/README.md#create) - Create a webhook
* [delete](calcom_py/resources/organizations/webhooks/README.md#delete) - Delete a webhook
* [get](calcom_py/resources/organizations/webhooks/README.md#get) - Get a webhook
* [list](calcom_py/resources/organizations/webhooks/README.md#list) - Get all webhooks
* [patch](calcom_py/resources/organizations/webhooks/README.md#patch) - Update a webhook

### [provider](calcom_py/resources/provider/README.md)

* [get](calcom_py/resources/provider/README.md#get) - Get a provider
* [verify_token](calcom_py/resources/provider/README.md#verify_token) - Verify an access token

### [schedules](calcom_py/resources/schedules/README.md)

* [create](calcom_py/resources/schedules/README.md#create) - Create a schedule
* [delete](calcom_py/resources/schedules/README.md#delete) - Delete a schedule
* [get](calcom_py/resources/schedules/README.md#get) - Get a schedule
* [list](calcom_py/resources/schedules/README.md#list) - Get all schedules
* [patch](calcom_py/resources/schedules/README.md#patch) - Update a schedule

### [schedules.default](calcom_py/resources/schedules/default/README.md)

* [list](calcom_py/resources/schedules/default/README.md#list) - Get default schedule

### [selected_calendars](calcom_py/resources/selected_calendars/README.md)

* [create](calcom_py/resources/selected_calendars/README.md#create) - Add a selected calendar
* [delete](calcom_py/resources/selected_calendars/README.md#delete) - Delete a selected calendar

### [slots](calcom_py/resources/slots/README.md)

* [list](calcom_py/resources/slots/README.md#list) - Find out when is an event type ready to be booked.

### [slots.reservations](calcom_py/resources/slots/reservations/README.md)

* [create](calcom_py/resources/slots/reservations/README.md#create) - Reserve a slot
* [delete](calcom_py/resources/slots/reservations/README.md#delete) - DELETE /v2/slots/reservations/{uid}
* [get](calcom_py/resources/slots/reservations/README.md#get) - Get reserved slot
* [patch](calcom_py/resources/slots/reservations/README.md#patch) - Updated reserved a slot

### [stripe](calcom_py/resources/stripe/README.md)

* [save](calcom_py/resources/stripe/README.md#save) - Save stripe credentials

### [stripe.check](calcom_py/resources/stripe/check/README.md)

* [check](calcom_py/resources/stripe/check/README.md#check) - Check stripe connection
* [get](calcom_py/resources/stripe/check/README.md#get) - Check team stripe connection

### [stripe.connect](calcom_py/resources/stripe/connect/README.md)

* [redirect](calcom_py/resources/stripe/connect/README.md#redirect) - Get stripe connect URL

### [teams](calcom_py/resources/teams/README.md)

* [create](calcom_py/resources/teams/README.md#create) - Create a team
* [delete](calcom_py/resources/teams/README.md#delete) - Delete a team
* [get](calcom_py/resources/teams/README.md#get) - Get a team
* [list](calcom_py/resources/teams/README.md#list) - Get teams
* [patch](calcom_py/resources/teams/README.md#patch) - Update a team

### [teams.event_types](calcom_py/resources/teams/event_types/README.md)

* [create](calcom_py/resources/teams/event_types/README.md#create) - Create an event type
* [delete](calcom_py/resources/teams/event_types/README.md#delete) - Delete a team event type
* [get](calcom_py/resources/teams/event_types/README.md#get) - Get an event type
* [list](calcom_py/resources/teams/event_types/README.md#list) - Get a team event type
* [patch](calcom_py/resources/teams/event_types/README.md#patch) - Update a team event type

### [teams.event_types.create_phone_call](calcom_py/resources/teams/event_types/create_phone_call/README.md)

* [create](calcom_py/resources/teams/event_types/create_phone_call/README.md#create) - Create a phone call

### [teams.memberships](calcom_py/resources/teams/memberships/README.md)

* [create](calcom_py/resources/teams/memberships/README.md#create) - Create a membership
* [delete](calcom_py/resources/teams/memberships/README.md#delete) - Delete a membership
* [get](calcom_py/resources/teams/memberships/README.md#get) - Get a membership
* [list](calcom_py/resources/teams/memberships/README.md#list) - Get all memberships
* [patch](calcom_py/resources/teams/memberships/README.md#patch) - Create a membership

### [timezones](calcom_py/resources/timezones/README.md)

* [list](calcom_py/resources/timezones/README.md#list) - Get all timezones

### [webhooks](calcom_py/resources/webhooks/README.md)

* [create](calcom_py/resources/webhooks/README.md#create) - Create a webhook
* [delete](calcom_py/resources/webhooks/README.md#delete) - Delete a webhook
* [get](calcom_py/resources/webhooks/README.md#get) - Get a webhook
* [list](calcom_py/resources/webhooks/README.md#list) - Get all webooks
* [patch](calcom_py/resources/webhooks/README.md#patch) - Update a webhook

<!-- MODULE DOCS END -->
