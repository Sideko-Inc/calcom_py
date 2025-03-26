
### list <a name="list"></a>
Get routing form responses



**API Endpoint**: `GET /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{routingFormId}/responses`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.organizations.teams.routing_forms.responses.list(
    org_id=123.45, routing_form_id="string", team_id=123.45
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.organizations.teams.routing_forms.responses.list(
    org_id=123.45, routing_form_id="string", team_id=123.45
)
```
