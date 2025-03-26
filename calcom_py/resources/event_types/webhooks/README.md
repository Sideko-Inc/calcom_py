
### delete_all <a name="delete_all"></a>
Delete all webhooks



**API Endpoint**: `DELETE /v2/event-types/{eventTypeId}/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.webhooks.delete_all(event_type_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.event_types.webhooks.delete_all(event_type_id=123.45)
```

### delete <a name="delete"></a>
Delete a webhook



**API Endpoint**: `DELETE /v2/event-types/{eventTypeId}/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.webhooks.delete(event_type_id=123.45, webhook_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.event_types.webhooks.delete(
    event_type_id=123.45, webhook_id="string"
)
```

### list <a name="list"></a>
Get all webhooks



**API Endpoint**: `GET /v2/event-types/{eventTypeId}/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.webhooks.list(event_type_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.event_types.webhooks.list(event_type_id=123.45)
```

### get <a name="get"></a>
Get a webhook



**API Endpoint**: `GET /v2/event-types/{eventTypeId}/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.webhooks.get(event_type_id=123.45, webhook_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.event_types.webhooks.get(event_type_id=123.45, webhook_id="string")
```

### patch <a name="patch"></a>
Update a webhook



**API Endpoint**: `PATCH /v2/event-types/{eventTypeId}/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.webhooks.patch(
    event_type_id=123.45,
    webhook_id="string",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.event_types.webhooks.patch(
    event_type_id=123.45,
    webhook_id="string",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
)
```

### create <a name="create"></a>
Create a webhook



**API Endpoint**: `POST /v2/event-types/{eventTypeId}/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.event_types.webhooks.create(
    active=True,
    event_type_id=123.45,
    subscriber_url="string",
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.event_types.webhooks.create(
    active=True,
    event_type_id=123.45,
    subscriber_url="string",
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
)
```
