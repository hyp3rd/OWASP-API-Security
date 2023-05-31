"""VulnAPI Models."""

from pydantic import \
    BaseModel  # pylint: disable=import-error # pylint: disable=no-name-in-module


class Invite(BaseModel):  # pylint: disable=too-few-public-methods
    """User Invite Model."""
    email: str
    role: str


class Picture(BaseModel):  # pylint: disable=too-few-public-methods
    """Picture Model."""
    picture_url: str
