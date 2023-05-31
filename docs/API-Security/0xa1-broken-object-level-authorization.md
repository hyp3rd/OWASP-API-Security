# API1:2023 Broken Object Level Authorization

The [**Broken Object Level Authorization**](https://github.com/OWASP/API-Security/blob/master/2023/en/src/0xa1-broken-object-level-authorization.md) is an API vulnerability where an attacker can manipulate object references to access unauthorized data.

This is often due to the API server needing to correctly verify whether the requesting user can access the requested data. This can result in unauthorized data exposure, modification, and sometimes, a complete system takeover.

## Impact

The severity of BOLA vulnerabilities is often high as it can allow attackers to access sensitive data or perform unauthorized actions. For example, an attacker might change the value of an ID parameter in a URL or POST data to access other users' data or perform actions on their behalf.

## Prevention

1. Avoid exposing direct object references: Avoid using direct references to internal implementation objects (like database keys) in your API. Instead, use other data to look up the object, like data tied to the authenticated user's session.

2. Implement Access Controls: Implement strict access control checks for every request. This includes verifying that the authenticated user has the necessary permissions to perform the requested action on the object.

3. Use Random and Unpredictable values: Use UUIDs or other random and hard-to-guess identifiers for your objects. This will make it harder for an attacker to guess valid IDs and exploit BOLA vulnerabilities.

4. Write tests: Write tests to ensure that your access controls are working as expected. This includes testing that users can only access their own data and can't access other users' data.

## Exploitation

Exploiting BOLA vulnerabilities is usually straightforward. An attacker can modify the ID parameter in a URL or POST data to gain access to other users' information, perform actions on their behalf, or move across resources beyond their authorized level.
