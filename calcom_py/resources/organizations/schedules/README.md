
### list <a name="list"></a>
Get all schedules



**API Endpoint**: `GET /v2/organizations/{orgId}/schedules`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.schedules.list(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.schedules.list(org_id=123.45)
```
