
### delete_all <a name="delete_all"></a>
Delete all webhooks



**API Endpoint**: `DELETE /v2/oauth-clients/{clientId}/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.webhooks.delete_all(client_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.webhooks.delete_all(client_id="string")
```

### delete <a name="delete"></a>
Delete a webhook



**API Endpoint**: `DELETE /v2/oauth-clients/{clientId}/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.webhooks.delete(client_id="string", webhook_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.webhooks.delete(
    client_id="string", webhook_id="string"
)
```

### list <a name="list"></a>
Get all webhooks



**API Endpoint**: `GET /v2/oauth-clients/{clientId}/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.webhooks.list(client_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.webhooks.list(client_id="string")
```

### get <a name="get"></a>
Get a webhook



**API Endpoint**: `GET /v2/oauth-clients/{clientId}/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.webhooks.get(client_id="string", webhook_id="string")
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.oauth_clients.webhooks.get(client_id="string", webhook_id="string")
```

### patch <a name="patch"></a>
Update a webhook



**API Endpoint**: `PATCH /v2/oauth-clients/{clientId}/webhooks/{webhookId}`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.webhooks.patch(
    client_id="string",
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
res = await client.oauth_clients.webhooks.patch(
    client_id="string",
    webhook_id="string",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
)
```

### create <a name="create"></a>
Create a webhook



**API Endpoint**: `POST /v2/oauth-clients/{clientId}/webhooks`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.oauth_clients.webhooks.create(
    active=True,
    client_id="string",
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
res = await client.oauth_clients.webhooks.create(
    active=True,
    client_id="string",
    subscriber_url="string",
    triggers="AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
    payload_template='{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
)
```
