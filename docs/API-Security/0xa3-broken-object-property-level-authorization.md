# API3:2023 Broken Object Property Level Authorization

In Broken Object Property Level Authorization vulnerabilities, an API endpoint is susceptible when it:

1. Accepts a JSON object from a client application and merges it into a server-side object without adequately verifying the client's permissions.
2. Exposes sensitive properties to the client application that should not be returned in the server response.

This vulnerability is particularly dangerous when the object properties include sensitive data or controls that can impact the application's behaviour. It can lead to unauthorized data access, modification, or execution of unintended application functionalities.

## Exploitation

Exploiting BOP LA involves the following steps:

1. **Identify Vulnerable API Endpoints**: The attacker needs to identify which API endpoints are vulnerable to BOP LA. This can be achieved by observing the API's responses and noting any sensitive data or controls returned in these responses.

2. **Craft Malicious Requests**: After identifying a vulnerable endpoint, the attacker crafts a request that includes a JSON object with the properties they wish to access or modify. The attacker will generally need to guess or infer the names of these properties.

3. **Send the Request**: The attacker sends the crafted request to the vulnerable endpoint. Suppose the endpoint does not verify the user's permissions correctly before merging the client-supplied JSON object into the server-side object. In that case, the attacker can modify or access the targeted properties.

## Mitigation

Preventing BOP LA vulnerabilities involves the implementation of strict access controls that verify a user's permissions before allowing them to access or modify an object's properties. This can be achieved by:

1. Implementing Property Level Permissions: Ensure that each property of an object has associated permissions that are checked before the property is accessed or modified.

2. Removing Sensitive Properties from Server Responses: Do not include sensitive properties in the server's response to a client request.

3. Enforce Input Validation: Implement strict input validation to prevent attackers from supplying malicious JSON objects in their requests.

4. Use of Allow Lists: Implement allow lists that specify which properties a user can access or modify.

The steps for preventing and managing security risks are described in general terms and are consistent with the guidelines outlined in the OWASP API Security document.
