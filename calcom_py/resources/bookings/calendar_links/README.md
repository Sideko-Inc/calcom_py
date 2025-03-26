
### list <a name="list"></a>
Get 'Add to Calendar' links for a booking

Retrieve calendar links for a booking that can be used to add the event to various calendar services. Returns links for Google Calendar, Microsoft Office, Microsoft Outlook, and a downloadable ICS file.

**API Endpoint**: `GET /v2/bookings/{bookingUid}/calendar-links`

#### Synchronous Client

```python
from calcom_py import Client
from os import getenv

client = Client(api_key=getenv("API_TOKEN"))
res = client.bookings.calendar_links.list(
    booking_uid="string", cal_api_version="string"
)
```

#### Asynchronous Client

```python
from calcom_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_TOKEN"))
res = await client.bookings.calendar_links.list(
    booking_uid="string", cal_api_version="string"
)
```
