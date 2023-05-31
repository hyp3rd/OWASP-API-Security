"""API module."""
import uuid
from enum import Enum
from typing import Dict, Optional

import requests
from api.models import Invite, Picture
from api.rate_limiter import RateLimitMiddleware
from fastapi import FastAPI, Header  # pylint: disable=import-error
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from pydantic import validators


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

videos_data = {
    "video1": {"description": "A nice video", "blocked": True},
    "video2": {"description": "Another nice video", "blocked": False},
    "video3": {"description": "Yet another nice video", "blocked": False},
    "video4": {"description": "A blocked video", "blocked": True},
    # ... more video data ...
}

# write 4 UUIDv4 here to follow


invites_data: Dict[str, Invite] = {
    "54f0c972-ff54-40cc-96f0-229134db8342": {"email": "user1@example.com", "role": "user"},
    "07b00d34-3e37-440a-8f62-2f787feec8c3": {"email": "user2@example.com", "role": "user"},
    "68d7d6d3-6a1c-4932-87a5-1c3e62f7e04a": {"email": "user3@example.com", "role": "user"},
    "19d7e418-5d5a-4a26-846e-eb2ac91740d0": {"email": "user4@example.com", "role": "user"},
    # ... more invite data ...
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
        self.app.get(path=f"{APIVersion.V1.value}/shops",
                     tags=["shops"],
                     name="BOLA",
                     summary="Broken Object Level Authorization",
                     description="The endpoints exposes a list of all the shops available in the ecommerce.",
                     response_model=None)(self.get_shops)

        # The get_shop_revenue_data function is used to return the revenue data for a shop
        self.app.get(path=f"{APIVersion.V1.value}/shops/{{shop_name}}/revenue_data.json",
                     tags=["shops"],
                     name="Broken Authentication",
                     summary="API2:2023 Broken Authentication",
                     description="Update the email address associated with a user's account",
                     response_model=None)(self.get_shop_revenue_data)

        # The update_email function is used to update the email address associated with a user's account
        self.app.put(path=f"{APIVersion.V1.value}/account",
                     tags=["account"],
                     name="Broken Authentication",
                     summary="API2:2023 Broken Authentication",
                     description="Update the email address associated with a user's account",
                     response_model=None)(self.update_email)

        # The update_video function the /api/v1/video/update_video endpoint accepts a PUT request
        # with a request body containing a description and optionally a blocked field.
        # If the video_id exists in our video data,
        # it updates the associated description and blocked status.
        # If the video_id doesn't exist, it returns an error message.
        self.app.put(path=f"{APIVersion.V1.value}/videos/{{video_id}}",
                     tags=["videos"],
                     name="Broken Object Property Level Authorization",
                     summary="API3:2023 Broken Object Property Level Authorization",
                     description="Update the video description and blocked status",
                     response_model=None)(self.update_video)

        # The get_invite function is used to return the invite data for a user

        self.app.get(path=f"{APIVersion.V1.value}/invites/{{invite_id}}",
                     tags=["invites"],
                     name="Broken Function Level Authorization",
                     summary="API5:2023 Broken Function Level Authorization",
                     description="Get the invite data for a user",
                     response_model=Invite)(self.get_invite)

        # The create_invite function is used to post an invite for a user
        self.app.post(path=f"{APIVersion.V1.value}/invites",
                      tags=["invites"],
                      name="Broken Function Level Authorization",
                      summary="API5:2023 Broken Function Level Authorization",
                      description="Post an invite for a user",
                      response_model=None)(self.create_invite)

        # The upload_picture function is used to upload a picture for a user profile
        self.app.post(path=f"{APIVersion.V1.value}/profile/picture",
                      tags=["profile"],
                      name="Server Side Request Forgery",
                      summary="API6:2023 Server Side Request Forgery",
                      description="Upload a picture for a user profile",
                      response_model=None)(self.upload_picture)

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

    # BOP: Broken Object Property Level Authorization
    # In this example, the vulnerability lies in the fact that the API allows a user
    # to change the blocked property of a video, even though
    # this should be an internal property that users do not have access to.
    # This means that a user could unblock their own blocked content by including a blocked field in the request body and setting it to false.
    # The endpoint /api/v1/video/update_video accepts a PUT request to update the description of a video.
    # For simplicity's sake, let's assume that there is no actual authentication logic in place
    #  and the blocked property of a video can be changed by any user.
    # This would highlight the vulnerability as there is no check in place
    # to confirm that the user making the request should have access to the blocked property.
    # curl -X 'PUT' \
    #   'http://127.0.0.1:8000/api/v1/videos/{video_id}' \
    #   -H 'accept: application/json' \
    #   -H 'Content-Type: application/json' \
    #   -d '{"description": "A nice video", "blocked": false}'
    async def update_video(self, video: Dict[str, str]):
        """Update the description or blocked status of a video."""
        video_id = "video1"  # For simplicity, we'll assume that we're always updating video1
        if video_id in videos_data:
            if "description" in video:
                videos_data[video_id]["description"] = video["description"]
            if "blocked" in video:
                videos_data[video_id]["blocked"] = video["blocked"]
            return {"message": "Video updated successfully"}

        return {"error": "Video not found"}

    # BFLA: API5:2023 Broken Function Level Authorization
    async def get_invite(self, invite_guid: str):
        """Get the invite data for a user."""
        if invite_guid in invites_data:
            return invites_data[invite_guid]

        return {"error": "Invite not found"}

    # BFLA: API5:2023 Broken Function Level Authorization
    # The critical issue here is that the API doesn't check the user's permissions
    # before allowing them to create a new invite with any role.
    # This means that an attacker could create a new invite with an admin role,
    # and then use this invite to create an admin account and gain full access to the system.
    # To fix this issue, we would typically add a function level authorization check
    # that verifies the user's role before allowing them to access certain endpoints.
    # This would help ensure that only users with the necessary permissions can create new invites.
    async def create_invite(self, invite: Invite):
        """Create an invite for a user."""
        invites_data[str(uuid.uuid4())] = {
            "email": invite.email, "role": invite.role}
        return {"message": "Invite created successfully"}

    # SSRF: API6:2023 Server Side Request Forgery
    async def upload_picture(self, picture: Picture):
        """Upload a picture for a user profile."""
        # For simplicity, we won't actually download the image from the URL. Instead,
        # we'll just return a message saying the image was downloaded successfully after executing a HEAD request to the URL.

        # Check if the url exists
        try:
            response = requests.head(picture.picture_url)
            if response.status_code != 200:
                return {"error": "URL does not exist"}
        except requests.exceptions.RequestException:
            return {"error": "URL does not exist"}

        return {"message": f"Image downloaded successfully from {picture.picture_url}"}


app = VulnAPI().app
