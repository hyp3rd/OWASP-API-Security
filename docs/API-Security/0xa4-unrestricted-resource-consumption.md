# API4:2023 Unrestricted Resource Consumption

Unrestricted Resource Consumption occurs when an API is vulnerable to users consuming resources indefinitely, potentially leading to system instability and ultimately to a denial of service. This happens when the API does not adequately control the amount of resources that are allocated when processing a user's request, which can be exploited by an attacker by sending requests at a rate faster than it can handle.

## Impact

Any user or system sending requests to the API could exploit this weakness. This includes both authenticated and unauthenticated users. Exploiting this issue can lead to system instability and potentially a complete denial of service or a disastrous financial impact.

## Prevention

1. Ensure that your APIs limit the amount of system resources and bandwidth they can consume and use solutions that are easy to limit.
2. Define a limit for the data sent in a request to reduce the risk of abuse.
3. Implement rate limiting based on the user's IP, session, or more sophisticated identifier to prevent API abuse.
4. Secure the endpoints that can cause high resource consumption and ensure they only expose a limited data set.
5. Implement server-side validation and resource paging to limit the data returned by a single API request rather than attempting to return the entire dataset.
6. Use hypermedia/HATEOAS to prevent clients from being able to request large amounts of data to be returned.
7. Use a CDN to cache static content and reduce the load on your servers.
8. Prevent spikes in billing costs by using a billing cap or setting up alerts to notify you when your bill reaches a certain threshold.

## Exploitation

The primary method of exploiting this vulnerability is to send requests to the API at a rate faster than it can handle, ultimately causing the system to become unstable or fail. This can be done by any user or system that can send requests to the API.
