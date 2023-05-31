# API8_2019_Injection

The application does not sanitize user input. It allows an attacker to inject malicious code into the application and abuse it.

## Challenge 12 - Find a way to get free coupons without knowing the coupon code

1. Login into your account;
2. Navigate to the `Shop` page and click on the `Add Coupon` button;
3. Add some random gibberish and intercept the response. The endpoint hit with a `POST` is `http://localhost:8888/community/api/v2/coupon/validate-coupon`;

    The payload sent is:

    ```json
    {
        "coupon_code": "<whatever you entered>"
    }
    ```

What makes sense is trying to trick the DB and spit out the coupons. The following payload is a good start:

```json
{
    "coupon_code": "1' OR 1=1; --"
}
```

The response is a `500` with an empty payload.

```json
{}
```

The application is vulnerable to SQL injection. The request does not get filtered, but the response is empty. It is a good sign. Let's set a proper attack and include NoSQL injection since the SQL injection does not return anything.

Open **Burp** and create a new project.

1. Choose a temporary project;
2. We want to intercept the request and modify the payload, navigate to the `Proxy` tab;
3. Ensure that the port is set to a value available on your machine under `Proxy Settings` > Proxy Listeners > `Add`. For example, `11260`, and bind it to your IP address, avoiding localhost;
4. Open **Firefox** and navigate to `http://<your_IP>:8888/shop`, and click on the `Add Coupons` button;
5. Move back to **Burp** and under the `Proxy` tab, click on the `Intercept is on` button to start intercepting the requests;
6. Back to the browser, add some gibberish in the text field, and click on the `Add Coupon` **Validate**;
7. Back to **Burp**, the request should be intercepted. Select it all, right-click, and hit `Send to intruder`. Click on the `Intercept is off` button to stop intercepting the requests;
8. Under the `Intruder` tab, ensure that the placeholders in the request's payload are external to the quotes of the `coupon_code` value: `{"coupon_code":§"ad"§}` click on the `Payloads` tab and select `Sniper`;
9. Click on the `Payloads` tab and select `Add` > `Payload type` > `Simple list`;
10. Uneder `Payloads Settings`, click on `Load`, and select the `Generic-NoSQLi.txt` file from the `assets/seclists/fuzzing/SQLi` folder of the repository;
11. Deselect the `Payload Encoding` > `URL-Encode` option;
12. Click on the `Start attack` button and wait for the attack to finish;
13. If there is a hit, the response will be a `200`, and the payload will be displayed in the `Response` tab, returning the coupon's code:

    ```json
    {
        "coupon_code":"<the_code>",
        "amount":"75",
        "CreatedAt":"2023-04-12T12:24:26.403Z"
    }
    ```

Free money.
