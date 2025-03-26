
### update <a name="update"></a>
Update destination calendars



**API Endpoint**: `PUT /v2/destination-calendars`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.destination_calendars.update(
    external_id="https://caldav.icloud.com/26962146906/calendars/1644422A-1945-4438-BBC0-4F0Q23A57R7S/",
    integration="apple_calendar",
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.destination_calendars.update(
    external_id="https://caldav.icloud.com/26962146906/calendars/1644422A-1945-4438-BBC0-4F0Q23A57R7S/",
    integration="apple_calendar",
)
```
