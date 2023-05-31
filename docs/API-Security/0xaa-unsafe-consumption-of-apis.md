# API10:2023 Unsafe Consumption of APIs

## Summary

[Unsafe Consumption of APIs](https://github.com/OWASP/API-Security/blob/master/2023/en/src/0xaa-unsafe-consumption-of-apis.md) refers to the security risk associated with integrating external or third-party APIs into your own applications. This risk emerges from developers often trusting but not verifying the endpoints of these external APIs. This can lead to exploiting security flaws in these APIs, impacting the applications that rely on them. Common issues include the exposure of sensitive information to unauthorized actors and various kinds of injections​​.

## Impact

The impact of this vulnerability is significant. If an API is compromised, it can lead to serious security breaches. These breaches can include interactions with other APIs over an unencrypted channel, improper validation and sanitization of data gathered from other APIs, blind following of redirections, unlimited resources available to process third-party services responses, and lack of implemented timeouts for interactions with third-party services​​.

## Exploitation

Exploitation scenarios can vary greatly, but a few examples are:

    1. An API relies on a third-party service to enrich user-provided business addresses. Attackers can use this third-party service to store an SQL injection (SQLi) payload associated with a business they created. It could then exfiltrate data to an attacker's controlled server.

    2. An API integrates with a third-party service provider to store sensitive user medical information. If the third-party API is compromised and starts responding with a redirect to an attacker's server, the API would unknowingly send the user's sensitive data to the attacker's server due to its blind following of redirects.

    3. An attacker can prepare a git repository with a malicious name, which, when integrated with an application, could be used as an injection payload, causing the application to execute harmful SQL queries​1​.

## Prevention

Prevention of unsafe consumption of APIs involves several strategies:

1. When evaluating service providers, assess their API security posture.
2. Ensure all API interactions happen over a secure communication channel (e.g., TLS).
3. Always validate and properly sanitize data received from integrated APIs before using it.
4. Maintain an allowlist of well-known locations integrated APIs may redirect your API too, and do not blindly follow redirects​​.
5. Implement timeouts for interactions with third-party services.
6. Implement rate-limiting for interactions with third-party services.
7. Implement a mechanism to monitor the health of integrated APIs.
8. Implement a mechanism to monitor the security posture of integrated APIs.
9. Implement a mechanism to monitor the availability of integrated APIs.
10. Implement a mechanism to monitor the performance of integrated APIs.
11. Implement a mechanism to monitor the compliance of integrated APIs with your organization's security policies.
