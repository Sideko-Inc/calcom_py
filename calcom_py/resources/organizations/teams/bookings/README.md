
### list <a name="list"></a>
Get organization team bookings



**API Endpoint**: `GET /v2/organizations/{orgId}/teams/{teamId}/bookings`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.bookings.list(org_id=123.45, team_id=123.45)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.bookings.list(org_id=123.45, team_id=123.45)
```
