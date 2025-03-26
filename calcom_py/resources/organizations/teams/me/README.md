
### get <a name="get"></a>
Get teams membership for user



**API Endpoint**: `GET /v2/organizations/{orgId}/teams/me`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.me.get(org_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.me.get(org_id=123.45)
```
