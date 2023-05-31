# API2_2019_Broken_User_Authentication

The application needs to prove the identity of the user sufficiently. It allows an attacker to impersonate a user and gain access to the application.

## Challenge 3 - Reset the password of a different user

Find the email address of another user on crAPI.
To solve the challenge, you must reset the password of another user.

1. Navigate the the **Community** clicking on the *Community* option in the navbar;
2. Observe the request sent after clicking on a random user's post. It can be seen that the endpoint is in the format `/community/api/v2/community/posts/<post_id>`;
3. Capture the response and find the email of the user who created the post;
4. Logout from the application and use the **Forgot Password** link;
5. Use the email of the user found in the previous step to reset the password;
6. The application will reply with a request for an OTP to proceed and reset the credentials. Observe the API request that occurs submitting random data. The endpoint is `/identity/api/auth/v3/check-otp`; The payload looks like the following: `{"email":"email@example.com","otp":"OTP","password":"some password"}`. What makes the most sense is to brute force it with a list of common OTPs;
7. Attempt the same payload repeatedly before trying any brute force attack. If there is rate-limiting, it is better avoiding to waste time.
8. The endpoint implements rate limiting, but it is worth noticing that it is a `v3` endpoint. It means there might be a `v2` endpoint that is not rate-limited. Find it by changing the URLs `v3` to `v2`. The payload is the same, but the response is different. Here is the brute force target.
9. Attempt an attack with `ffuf`, leveraging the `4-digits-0000-9999.txt` from `seclists`. The command is:

    ```bash
    ffuf -w ./4-digits-0000-9999.txt -u http://172.20.10.2:8888/identity/api/auth/v2/check-otp -X POST -H "Content-Type: application/json" -d '{"email":"<target_email>","otp":"FUZZ","password":"<some_password>"}' > out
    ```

10. If the attack is successful, try the login endpoint to test the credentials.

Check out the video for a demonstration.
