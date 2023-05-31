"""API module."""
from enum import Enum
from typing import Optional

from api.rate_limiter import RateLimitMiddleware
from fastapi import FastAPI, Header
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

# from pydantic import ValidationError  # pylint: disable=import-error


class APIVersion(str, Enum):
    """Process State Enum."""
    V1 = "/api/v1"
    V2 = "/api/v2"


# Sample data
shops_data = {
    "shop1": {"revenue_data": {"total_revenue": 1000, "monthly_revenue": 100}},
    "shop2": {"revenue_data": {"total_revenue": 2000, "monthly_revenue": 200}},
    "shop3": {"revenue_data": {"total_revenue": 3000, "monthly_revenue": 300}},
    "shop4": {"revenue_data": {"total_revenue": 4000, "monthly_revenue": 400}},
    "shop5": {"revenue_data": {"total_revenue": 5000, "monthly_revenue": 500}},
    "shop6": {"revenue_data": {"total_revenue": 6000, "monthly_revenue": 600}},
    "shop7": {"revenue_data": {"total_revenue": 7000, "monthly_revenue": 700}},
    "shop8": {"revenue_data": {"total_revenue": 8000, "monthly_revenue": 800}},
    "shop9": {"revenue_data": {"total_revenue": 9000, "monthly_revenue": 900}},
    "shop10": {"revenue_data": {"total_revenue": 10000, "monthly_revenue": 1000}},
    # ... more shop data ...
}

users_data = {
    "token1": {"email": "user1@example.com"},
    "token2": {"email": "user2@example.com"},
    "token3": {"email": "user3@example.com"},
    # ... more user data ...
}


class VulnAPI:
    """VulnAPI API."""

    # This is the main function that starts the application
    def __init__(self):
        # The vuln_process variable is used to store the main API process
        self.vuln_process = None

        # The app variable is the main FastAPI instance
        self.app = FastAPI(
            title="VulnAPI",
            description="VulnAPI is a vulnerable API that demonstrates the top 10 OWASP API Vunerabilities.",
            version="v1.0.0",
            debug=True,
            # The RateLimitMiddleware is used to limit the number of requests to 20 per minute
            middleware=[
                Middleware(RateLimitMiddleware, limit=20, interval=60),
                # The CORSMiddleware is used to allow requests from the web interface
                Middleware(CORSMiddleware,
                           allow_origins=["*"],
                           allow_credentials=True,
                           allow_methods=["*"],
                           allow_headers=["*"])
            ]
        )

        # The index function is used to return the index page
        self.app.get(path="/",
                     tags=["index"],
                     name="VulnAPI Index",
                     summary="Here goes nothing",
                     description="Don't use this in production. Seriously.",
                     response_model=None)(self.index)

        # The get_shops function is used to return the list of shops
        self.app.get(path=f"{APIVersion.V1}/shops",
                     tags=["shops"],
                     name="BOLA",
                     summary="Broken Object Level Authorization",
                     description="The endpoints exposes a list of all the shops available in the ecommerce.",
                     response_model=None)(self.get_shops)

        # The get_shop_revenue_data function is used to return the revenue data for a shop
        self.app.get(path=f"{APIVersion.V1}/shops/{{shop_name}}/revenue_data.json",
                     tags=["shops"],
                     name="Broken Authentication",
                     summary="API2:2023 Broken Authentication",
                     description="Update the email address associated with a user's account",
                     response_model=None)(self.get_shop_revenue_data)

        # The update_email function is used to update the email address associated with a user's account
        self.app.put(path=f"{APIVersion.V1}/account",
                     tags=["account"],
                     name="Broken Authentication",
                     summary="API2:2023 Broken Authentication",
                     description="Update the email address associated with a user's account",
                     response_model=None)(self.update_email)

    def index(self):
        """index."""
        return {"/dev/null ": "before dishonor"}

    # BOLA: Broken Object Level Authorization
    # The get_shops function is used to return the list of shops
    async def get_shops(self):
        """Get all shops available in the ecommerce."""
        return {"shops": list(shops_data.keys())}

    # BOLA: Broken Object Level Authorization
    # The get_shop_revenue_data function is used to return the revenue data for a shop
    # The shop_name parameter is used to identify the shop for which the revenue data is to be returned
    async def get_shop_revenue_data(self, shop_name: str):
        """Get shop revenue data."""
        if shop_name in shops_data:
            return shops_data[shop_name]["revenue_data"]

        return {"error": "Shop not found"}

    # BA: Broken Authentication
    # Because the API does not require the user to confirm
    # their identity by providing their current password,
    # bad actors are able to put themselves in a position to steal the auth token.
    # They also might be able to take over the victim's account
    # by starting the reset password workflow after
    # updating the email address of the victim's account.
    # curl -X PUT "http://localhost:8000/api/v1/account" \
    #     -H "accept: application/json" \
    #     -H "Authorization: Bearer token1" \
    #     -d "{ \"email\": \"new_email@example.com\" }"
    async def update_email(self, authorization: Optional[str] = Header(), email: str = None):
        """Update the email address associated with a user's account."""
        auth_token = authorization.split(' ')[1] if authorization else None
        if auth_token in users_data:
            users_data[auth_token]["email"] = email
            return {"message": "Email updated successfully"}

        return {"error": "Invalid authorization token"}


app = VulnAPI().app
