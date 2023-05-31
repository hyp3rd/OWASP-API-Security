# API7:2023 Security Misconfiguration

[Security Misconfiguration](https://github.com/OWASP/API-Security/blob/master/2023/en/src/0xa7-security-misconfiguration.md) refers to a security weakness where attackers often attempt to exploit unpatched flaws, unprotected files, directories, or standard endpoints to gain unauthorized access or knowledge of the system. This misconfiguration can occur at any level of the API stack, from the network to the application level. Automated tools can detect and exploit misconfigurations like unnecessary services or legacy options. If exploited, security misconfigurations can expose sensitive user data and system details, potentially leading to a full-service compromise.

## Impact

An API may be vulnerable to security misconfiguration if:

1. The appropriate security hardening must be present across any part of the API stack or if there are improperly configured permissions on cloud services.
2. The latest security patches are missing, or the systems are out of date.
3. Unnecessary features are enabled (e.g., HTTP verbs, logging features).
4. There are discrepancies in how incoming requests are processed by servers in the HTTP server chain.
5. Transport Layer Security (TLS) is missing.
6. Security or cache-control directives are not sent to clients.
7. A Cross-Origin Resource Sharing (CORS) policy needs to be included or adequately set.
8. Error messages include stack traces or expose other sensitive information​​.

## Prevention

To prevent security misconfigurations, consider the following measures:

1. Implement a repeatable hardening process leading to the fast and easy deployment of a properly locked-down environment.
2. Regularly review and update configurations across the entire API stack, including orchestration files, API components, and cloud services like S3 bucket permissions.
3. Establish an automated process to continuously assess the effectiveness of the configuration and settings in all environments.
4. Ensure that all API communications, whether internal or public-facing, occur over an encrypted communication channel (TLS).
5. Define which HTTP verbs each API can access and disable all others (e.g., HEAD).
6. Implement a proper Cross-Origin Resource Sharing (CORS) policy on APIs expected to be accessed from browser-based clients.
7. Ensure all servers in the HTTP server chain (e.g., load balancers, reverse and forward proxies, and back-end servers) process incoming requests uniformly to avoid desync issues.
8. Define and enforce all API response payload schemas, including error responses, to prevent exception traces and other valuable information from being returned to attackers.

## Exploitation

### Scenario #1

An API back-end server maintains an access log written by a popular third-party open-source logging utility with support for placeholder expansion and JNDI lookups, both enabled by default. A bad actor issues an API request, which gets written to the access log file with a malicious value in the X-Api-Version request header. Due to the insecure default configuration of the logging utility and a permissive network outbound policy, the logging utility will pull and execute the malicious object from the attacker's remote-controlled server when trying to write the corresponding entry to the access log​.

### Scenario #2

A social network website that offers a "Direct Message" feature issues an API request to retrieve new messages for a specific conversation. Because the API response does not include the Cache-Control HTTP response header, private conversations are cached by the web browser. This enables malicious actors to retrieve them from the browser cache files in the filesystem​1​.
