# API5:2023 Broken Function Level Authorization

The [Broken Function Level Authorization](https://github.com/OWASP/API-Security/blob/master/2023/en/src/0xa5-broken-function-level-authorization.md) vulnerability occurs when an attacker sends legitimate API calls to an endpoint that they should not have access to. These endpoints might be exposed to anonymous users or regular, non-privileged users. APIs are structured to make it easier to discover these flaws, such as by changing the HTTP method from GET to PUT or changing the "users" string in the URL to "admins". Authorization checks for a function or resource are usually managed via configuration and sometimes at the code level. Modern applications can contain many types of roles or groups and complex user hierarchies (e.g., sub-users or users with more than one role), which can make implementing proper checks confusing. Detection of such flaws relies on appropriate logging and monitoring. Attackers can exploit these flaws to access unauthorized functionality, with administrative functions being key targets​.

## Impact

This type of vulnerability allows attackers to access unauthorized functionality. Attackers mainly target administrative functions as they often lead to gaining unauthorized control or access to sensitive data​.

## Prevention

Each application should have a consistent and easy-to-analyze authorization model invoked or injected from all your business functions. This model should be based on the user's group/role and the application's business logic. The following are some guidelines to help you implement a proper authorization model:

1. The enforcement mechanism(s) should deny all access by default, requiring explicit grants to specific roles for access to every function.
2. Review your API endpoints against function-level authorization flaws while keeping in mind the application's business logic and group hierarchy.
3. Ensure all administrative controllers inherit from an abstract administrative controller that implements authorization checks based on the user's group/role.
4. Make sure that administrative functions inside a regular controller implement authorization checks based on the user's group and role.

## Exploitation

To exploit a system, an attacker must send legitimate API calls to an API endpoint they cannot access. This can be achieved by altering the HTTP method or changing URL components to gain access to different resources. For example, an attacker may change "users" to "admins" in the URL to try and access administrative functions.
