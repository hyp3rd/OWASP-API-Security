"""VulnAPI Models."""

from pydantic import BaseModel  # pylint: disable=import-error


class Invite(BaseModel):  # pylint: disable=too-few-public-methods
    """User Invite Model."""
    email: str
    role: str
