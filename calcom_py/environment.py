import enum


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    PRODUCTION = "https://api.cal.com"
    MOCK_SERVER = "https://api.sideko.dev/v1/mock/public/calcom/0.1.0"
