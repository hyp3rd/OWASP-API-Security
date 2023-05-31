# API6:2023 Server-Side Request Forgery

## Summary

[Server Side Request Forgery (SSRF)](https://github.com/OWASP/API-Security/blob/master/2023/en/src/0xa6-server-side-request-forgery.md) is a security vulnerability that occurs when an API can request arbitrary URLs the user provides without sufficient validation or restrictions. This can happen when an API endpoint receives a URI as a parameter and then accesses the provided URI. This vulnerability is often seen in modern application development due to the widespread use of functionalities like Webhooks, file fetching from URLs, custom Single Sign-On (SSO), and URL previews.
It can lead to performing port scanning of internal networks, accessing internal services such as HTTP, FTP, SMTP, etc. and in some cases, accessing the server's local file system.

## Impact

Successful exploitation of an SSRF vulnerability can lead to severe consequences. It allows an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall or a VPN. This may lead to internal services enumeration (e.g. port scanning) or information disclosure, bypassing firewalls or other security mechanisms. Sometimes, it can lead to Denial of Service (DoS) or the server being used as a proxy to hide malicious activities. SSRF attacks can be especially dangerous when modern technologies like cloud providers, Kubernetes, and Docker are used, as they expose management and control channels over HTTP on predictable, well-known paths. Such channels are an easy target for an SSRF attack.

## Prevention

Preventing SSRF vulnerabilities requires careful design and implementation of URL handling and resource fetching. Some strategies include:

1. Isolating the resource fetching mechanism in your network, as these features are typically aimed at retrieving remote resources and not internal ones.
2. Using allow lists of remote origins, users are expected to download resources from (e.g. Google Drive, Gravatar, etc.), URL schemes and ports, and accepted media types for a given functionality.
3. Disabling HTTP redirections.
4. Using a well-tested and maintained URL parser to avoid issues caused by URL parsing inconsistencies​.

## Exploitation

To exploit an SSRF vulnerability, an attacker typically needs to find a vulnerable web application that allows them to specify a URL parameter. The attacker can then manipulate the URL parameter to send a request to an internal or external system. Techniques that can be used include IP address manipulation, protocol injection, and URL redirection to bypass security controls and access sensitive data or execute arbitrary code.

For example, in a social network application that allows users to upload profile pictures by providing a URL, an attacker can send a malicious URL that initiates port scanning within the internal network using the API Endpoint. This can be used to determine which ports are open and which are closed, and then use this information to launch further attacks. Based on the response time, the attacker can determine whether the port is open.
