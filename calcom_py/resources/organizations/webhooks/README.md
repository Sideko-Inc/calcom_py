
### delete <a name="delete"></a>
Delete a webhook



**API Endpoint**: `DELETE /v2/organizations/{orgId}/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.webhooks.delete(org_id=123.45, webhook_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.webhooks.delete(org_id=123.45, webhook_id="string")
```

### list <a name="list"></a>
Get all webhooks



**API Endpoint**: `GET /v2/organizations/{orgId}/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.webhooks.list(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.webhooks.list(org_id=123.45)
```

### get <a name="get"></a>
Get a webhook



**API Endpoint**: `GET /v2/organizations/{orgId}/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.webhooks.get(org_id=123.45, webhook_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.webhooks.get(org_id=123.45, webhook_id="string")
```

### patch <a name="patch"></a>
Update a webhook



**API Endpoint**: `PATCH /v2/organizations/{orgId}/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.webhooks.patch(
    org_id=123.45,
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
res = await client.organizations.webhooks.patch(
    org_id=123.45,
    webhook_id="string",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
)
```

### create <a name="create"></a>
Create a webhook



**API Endpoint**: `POST /v2/organizations/{orgId}/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.webhooks.create(
    active=True,
    org_id=123.45,
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
res = await client.organizations.webhooks.create(
    active=True,
    org_id=123.45,
    subscriber_url="string",
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
)
```
