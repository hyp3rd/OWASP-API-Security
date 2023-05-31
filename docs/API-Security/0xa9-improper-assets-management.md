# API9:2023 Improper Inventory Management

[Improper Inventory Management](https://github.com/OWASP/API-Security/blob/master/2023/en/src/0xa9-improper-assets-management.md) is a security weakness where threat agents gain unauthorized access through old API versions, or endpoints left running unpatched and using weaker security requirements. This vulnerability may also be exploited by gaining access to sensitive data through a third party that should not have the data. Lack of updated documentation and absence of assets inventory and retirement strategies result in running unpatched systems, leading to sensitive data leakage. This issue is common in modern concepts like microservices which make applications easy to deploy and independent, leading to the exposure of API hosts unnecessarily. Attackers can gain access to sensitive data or even take over the server through old, unpatched API versions connected to the same database​.

## Impact

Improper Inventory Management expands the attack surface of your APIs. Attackers can exploit old, unpatched API versions, often connected to the same database as the current version. This allows them to access sensitive data or even take over the server. The lack of visibility and inventory of sensitive data flows also creates risks, especially in the event of a breach on the third-party side. For instance, a "sensitive data flow", where the API shares sensitive data with a third party without a business justification or approval or without inventory or visibility of the flow can be exploited by malicious actors.

## Prevention

To prevent improper inventory management, follow these steps:

1. **Inventory all API hosts**: Document essential aspects of each one of them, focusing on the API environment (e.g., production, staging, test, development), who should have network access to the host (e.g., public, internal, partners), and the API version.
2. **Inventory integrated services**: Document their role in the system, what data is exchanged (data flow), and their sensitivity.
3. **Document all aspects of your API**: This includes authentication, errors, redirects, rate-limiting, cross-origin resource sharing (CORS) policy, and endpoints, including their parameters, requests, and responses.
4. **Automate documentation generation**: Adopt open standards and include the documentation build in your CI/CD pipeline.
5. **Restrict API documentation access**: Make API documentation available only to those authorized to use the API.
6. **Use external protection measures**: Implement API security-specific solutions for all exposed versions of your APIs, not just for the current production version.

## Exploitation

The following scenario demonstrates how Improper Inventory Management can be exploited:

### Scenario #1

A company has an API that allows users to retrieve their account information. The API is protected by a Web Application Firewall (WAF) that blocks requests with a missing or invalid API key. The company decided to release a new version of the API, which is protected by a new WAF. The old version of the API is still running, but it is not covered by a WAF. The company forgets to remove the old version of the API, which is now vulnerable to attacks.

An attacker can exploit this vulnerability by sending requests to the old API version. The attacker can then use the information obtained from the old version of the API to attack the new version of the API.
