
### delete <a name="delete"></a>
Delete a team event type



**API Endpoint**: `DELETE /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.event_types.delete(
    event_type_id=123.45, org_id=123.45, team_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.event_types.delete(
    event_type_id=123.45, org_id=123.45, team_id=123.45
)
```

### list_for_team <a name="list_for_team"></a>
Get all team event types



**API Endpoint**: `GET /v2/organizations/{orgId}/teams/event-types`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.event_types.list_for_team(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.event_types.list_for_team(org_id=123.45)
```

### list <a name="list"></a>
Get a team event type



**API Endpoint**: `GET /v2/organizations/{orgId}/teams/{teamId}/event-types`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.event_types.list(org_id=123.45, team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.event_types.list(org_id=123.45, team_id=123.45)
```

### get_one <a name="get_one"></a>
Get an event type



**API Endpoint**: `GET /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.event_types.get_one(
    event_type_id=123.45, org_id=123.45, team_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.event_types.get_one(
    event_type_id=123.45, org_id=123.45, team_id=123.45
)
```

### patch <a name="patch"></a>
Update a team event type



**API Endpoint**: `PATCH /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.event_types.patch(
    event_type_id=123.45,
    org_id=123.45,
    team_id=123.45,
    custom_name="{Event type title} between {Organiser} and {Scheduler}",
    description="Discover the culinary wonders of the Argentina by making the best flan ever!",
    length_in_minutes=60.0,
    length_in_minutes_options=["string", "string", "string"],
    slug="learn-the-secrets-of-masterchief",
    success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
    title="Learn the secrets of masterchief!",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.event_types.patch(
    event_type_id=123.45,
    org_id=123.45,
    team_id=123.45,
    custom_name="{Event type title} between {Organiser} and {Scheduler}",
    description="Discover the culinary wonders of the Argentina by making the best flan ever!",
    length_in_minutes=60.0,
    length_in_minutes_options=["string", "string", "string"],
    slug="learn-the-secrets-of-masterchief",
    success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
    title="Learn the secrets of masterchief!",
)
```

### create <a name="create"></a>
Create an event type



**API Endpoint**: `POST /v2/organizations/{orgId}/teams/{teamId}/event-types`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.event_types.create(
    hosts=[{"user_id": 123.45}],
    length_in_minutes=60.0,
    org_id=123.45,
    scheduling_type="collective",
    slug="learn-the-secrets-of-masterchief",
    team_id=123.45,
    title="Learn the secrets of masterchief!",
    custom_name="{Event type title} between {Organiser} and {Scheduler}",
    description="Discover the culinary wonders of the Argentina by making the best flan ever!",
    length_in_minutes_options=["string", "string", "string"],
    success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.event_types.create(
    hosts=[{"user_id": 123.45}],
    length_in_minutes=60.0,
    org_id=123.45,
    scheduling_type="collective",
    slug="learn-the-secrets-of-masterchief",
    team_id=123.45,
    title="Learn the secrets of masterchief!",
    custom_name="{Event type title} between {Organiser} and {Scheduler}",
    description="Discover the culinary wonders of the Argentina by making the best flan ever!",
    length_in_minutes_options=["string", "string", "string"],
    success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
)
```

### create_phone_call <a name="create_phone_call"></a>
Create a phone call



**API Endpoint**: `POST /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}/create-phone-call`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.event_types.create_phone_call(
    cal_api_key="string",
    enabled={},
    event_type_id=123.45,
    number_to_call="string",
    org_id=123.45,
    team_id=123.45,
    template_type="CHECK_IN_APPOINTMENT",
    your_phone_number="string",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.event_types.create_phone_call(
    cal_api_key="string",
    enabled={},
    event_type_id=123.45,
    number_to_call="string",
    org_id=123.45,
    team_id=123.45,
    template_type="CHECK_IN_APPOINTMENT",
    your_phone_number="string",
)
```
