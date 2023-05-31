# API1_2019_Broken_Object_Level_Authorization

The application needs to verify the identity of the user adequately. It lets an attacker access information that should be tight to an authorization model.

## Challenge 1 - Access details of another user's vehicle

To solve the challenge, you must leak sensitive information about another user's vehicle.

1. Since vehicle IDs are not sequential numbers but GUIDs, you need to find a way to expose the vehicle ID of another user.
2. Find an API endpoint that receives a vehicle ID and returns information about it.

### Detailed solution 1

1. [Login](http://localhost:8888/login) to the application;
2. Navigate to the community page by clicking on the *Community* option in the navbar;
3. Observe the request sent after clicking on a random user's post. It can be seen that the endpoint is in the format `/community/api/v2/community/posts/<post_id>`.

The payload that the server sends back contains the vehicle ID of the user who created the post, amongst the others:

```json
{
    "id": "BgKUbgWE5UcG9BD4t5QAuH",
    "title": "Title 3",
    "content": "Hello world 3",
    "author": {
        "nickname": "Robot",
        "email": "robot001@example.com",
        "vehicleid": "be7b64cb-5239-4969-a363-7bc37dea620c",
        "profile_pic_url":"  ",
        "created_at": "2023-04-12T12:24:26.519Z"
    },
    "comments": [],
    "authorid": 3,
    "CreatedAt": "2023-04-12T12:24:26.519Z"
}
```

Here to follow the demo:

[demo](https://user-images.githubusercontent.com/62474964/232136102-438692d2-7e55-485b-ae27-fe7f82be18d9.mp4)

### Detailed solution 2

After adding your vehicle to the application, you can access and refresh the car's location.
Observe the request sent after clicking on the *Refresh* button. It can be seen that the endpoint is in the format `/api/v1/vehicles/<vehicle_id>/location`.

Use the vehicle ID of another user, collected in part 1 of this challenge to access their location.

`POST /api/v1/vehicles/<vehicle_id>/location`

```json
{
    "carId": "2eebf0d8-d950-42cb-804e-10b84e78652d",
    "vehicleLocation": {
        "id": 3,
        "latitude": "37.7775112",
        "longitude": "-122.3970889"
    },
    "fullName": "Hank"
}
```

The application does not implement a security model and the resources are acwardly unprotected allowing an attacker to access information of any users.

## Challenge 2 - Access mechanic reports of other users

crAPI allows vehicle owners to contact their mechanics by submitting a "contact mechanic" form. This challenge is about accessing mechanic reports that were submitted by other users.

1. [Login](http://localhost:8888/login) to the application;
2. After adding a vehicle, we will have the option to send a service request to the mechanic by using the *Contact Mechanic* option;
3. Observe the request sent after the *Send Service Request*. In the `/workshop/api/merchant/contact_mechanic` response, we can find the hidden API endpoint in `report_link`.
4. Go to the link present as a value in `report_link`.
5. Change the value of `report_id` in the request and send it to access details of another user's vehicle.

Watch it in the video:

[demo](https://user-images.githubusercontent.com/62474964/232136333-0cefc2a2-3222-481f-b6e7-42045b380c5e.mp4)
