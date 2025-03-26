
### create <a name="create"></a>
Create a phone call



**API Endpoint**: `POST /v2/teams/{teamId}/event-types/{eventTypeId}/create-phone-call`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.teams.event_types.create_phone_call.create(
    cal_api_key="string",
    enabled={},
    event_type_id=123.45,
    number_to_call="string",
    team_id=123.45,
    template_type="CHECK_IN_APPOINTMENT",
    your_phone_number="string",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.teams.event_types.create_phone_call.create(
    cal_api_key="string",
    enabled={},
    event_type_id=123.45,
    number_to_call="string",
    team_id=123.45,
    template_type="CHECK_IN_APPOINTMENT",
    your_phone_number="string",
)
```
