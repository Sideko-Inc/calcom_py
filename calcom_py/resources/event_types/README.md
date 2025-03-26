
### delete <a name="delete"></a>
Delete an event type



**API Endpoint**: `DELETE /v2/event-types/{eventTypeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.delete(cal_api_version="string", event_type_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.event_types.delete(cal_api_version="string", event_type_id=123.45)
```

### list <a name="list"></a>
Get all event types



**API Endpoint**: `GET /v2/event-types`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.list(cal_api_version="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.event_types.list(cal_api_version="string")
```

### get <a name="get"></a>
Get an event type



**API Endpoint**: `GET /v2/event-types/{eventTypeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.get(cal_api_version="string", event_type_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.event_types.get(cal_api_version="string", event_type_id="string")
```

### patch <a name="patch"></a>
Update an event type



**API Endpoint**: `PATCH /v2/event-types/{eventTypeId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.patch(
    cal_api_version="string",
    event_type_id=123.45,
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
res = await client.event_types.patch(
    cal_api_version="string",
    event_type_id=123.45,
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



**API Endpoint**: `POST /v2/event-types`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.create(
    cal_api_version="string",
    length_in_minutes=60.0,
    slug="learn-the-secrets-of-masterchief",
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
res = await client.event_types.create(
    cal_api_version="string",
    length_in_minutes=60.0,
    slug="learn-the-secrets-of-masterchief",
    title="Learn the secrets of masterchief!",
    custom_name="{Event type title} between {Organiser} and {Scheduler}",
    description="Discover the culinary wonders of the Argentina by making the best flan ever!",
    length_in_minutes_options=["string", "string", "string"],
    success_redirect_url="https://masterchief.com/argentina/flan/video/9129412",
)
```
