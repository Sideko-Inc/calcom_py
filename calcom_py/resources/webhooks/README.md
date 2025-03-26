
### delete <a name="delete"></a>
Delete a webhook



**API Endpoint**: `DELETE /v2/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.webhooks.delete(webhook_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.webhooks.delete(webhook_id="string")
```

### list <a name="list"></a>
Get all webooks

Gets a paginated list of webhooks for the authenticated user.

**API Endpoint**: `GET /v2/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.webhooks.list()
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.webhooks.list()
```

### get <a name="get"></a>
Get a webhook



**API Endpoint**: `GET /v2/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.webhooks.get(webhook_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.webhooks.get(webhook_id="string")
```

### patch <a name="patch"></a>
Update a webhook



**API Endpoint**: `PATCH /v2/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.webhooks.patch(
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
res = await client.webhooks.patch(
    webhook_id="string",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
)
```

### create <a name="create"></a>
Create a webhook



**API Endpoint**: `POST /v2/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.webhooks.create(
    active=True,
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
res = await client.webhooks.create(
    active=True,
    subscriber_url="string",
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
)
```
