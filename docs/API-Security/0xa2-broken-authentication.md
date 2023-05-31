# API2:2023 Broken Authentication

## Summary

[Broken Authentication](https://github.com/OWASP/API-Security/blob/master/2023/en/src/0xa2-broken-authentication.md) is a type of vulnerability that allows an attacker to bypass the authentication methods that are used by a web application or API.

This could be due to flaws in the authentication scheme, implementation, or design. An attacker exploiting this vulnerability could assume the identity of other users or gain unauthorized access to sensitive data.

## Impact

The impact of Broken Authentication is significant. If successfully exploited, an attacker can impersonate legitimate users, gain unauthorized access to sensitive data, or perform unauthorized actions. In the worst-case scenario, the attacker could take over an administrative account, leading to a complete compromise of the system. The potential damage includes data breaches, financial loss, and damage to the organization's reputation.

## Prevention

Preventing Broken Authentication involves implementing a robust and secure authentication mechanism. Here are some best practices:

1. Authorization and Authorization Mechanism: Ensure you understand what and how they are used. OAuth is not authentication, and neither are API keys.

2. Multi-factor Authentication: Implement multi-factor authentication, which provides an additional layer of security.

3. Protect the resources sensitive to credentials exposure or manipulation: Endpoints that allow password resets, re-auth, and MFA are as sensitive as secrets, and misconfigurations can lead to complete takeovers.

4. Limit Login Attempts: Implement account lockout or delay mechanisms after a certain number of failed login attempts to prevent brute force attacks.

5. Implement anti-brute force mechanisms to mitigate credential stuffing, dictionary attacks, and brute force attacks on your authentication endpoints. This mechanism should be stricter than the common rate-limiting mechanisms on your APIs.

## Exploitation

Exploiting Broken Authentication vulnerabilities is usually straightforward. An attacker can use a variety of techniques to bypass authentication. Here are some examples:

1. Brute Force Attacks: An attacker may try to guess the credentials of an account by trying different combinations.

2. Intercept sensitive authentication details in the URL, such as auth tokens and passwords.

3. Credential Stuffing: In this type of attack, an attacker uses known username/password combinations, often obtained from data breaches, to gain unauthorized access.

4. Insecure Direct Object References (IDOR). This vulnerability allows an attacker to manipulate a parameter value and gain unauthorized access to a system object if the API endpoint lacks proper permission checks.
