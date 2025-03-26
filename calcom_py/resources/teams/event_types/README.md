
### delete <a name="delete"></a>
Delete a team event type



**API Endpoint**: `DELETE /v2/teams/{teamId}/event-types/{eventTypeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.event_types.delete(event_type_id=123.45, team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.teams.event_types.delete(event_type_id=123.45, team_id=123.45)
```

### list <a name="list"></a>
Get a team event type



**API Endpoint**: `GET /v2/teams/{teamId}/event-types`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.event_types.list(team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.teams.event_types.list(team_id=123.45)
```

### get <a name="get"></a>
Get an event type



**API Endpoint**: `GET /v2/teams/{teamId}/event-types/{eventTypeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.event_types.get(event_type_id=123.45, team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.teams.event_types.get(event_type_id=123.45, team_id=123.45)
```

### patch <a name="patch"></a>
Update a team event type



**API Endpoint**: `PATCH /v2/teams/{teamId}/event-types/{eventTypeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.event_types.patch(
    event_type_id=123.45,
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
res = await client.teams.event_types.patch(
    event_type_id=123.45,
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



**API Endpoint**: `POST /v2/teams/{teamId}/event-types`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.event_types.create(
    hosts=[{"user_id": 123.45}],
    length_in_minutes=60.0,
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
res = await client.teams.event_types.create(
    hosts=[{"user_id": 123.45}],
    length_in_minutes=60.0,
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
