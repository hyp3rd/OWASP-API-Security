# Exploiting crAPI

This section aims to exploit the vulnerabilities in **crAPI** and learn how to prevent them.
Learning how to gather information about the API and exploit it without the aid of a tool like Burp Suite is essential.

It is possible to execute most exploits against **crAPI** leveraging the [list of endpoints](./endpoints.md) and Postman to organize your requests.
Of course, the exploits can get sophisticated and require more than a simple request to the API. Still identifying and avoiding flaws in our code that would trigger digital havoc is the primal matter here.

```{note}
::: the exploits in this section are not meant to be used against production systems :::

/dev/null before dishonor
```

## Preparing the environment

The first step is to prepare the environment to execute the exploits. Refer to the [setup](./setup.md) section to get your system ready.

## Exploiting the API

The exploits are categorized, each aiming to showcase a different [**OWASP API Security Top 10 vulnerability**](https://owasp.org/www-project-api-security/).
At the end of the section, you should be able to identify and exploit the vulnerabilities in **crAPI** and, most importantly, how to chain a vulnerability to another and move laterally to other parts of the app.

### Import the Postman collection

The Postman collection contains most API requests and the necessary information to execute the exploits.
Import the [collection](./postman-collection.json) as shown in the video below (the keyboard shortcut for macOS: `cmd+o`).

[import the collection](https://user-images.githubusercontent.com/62474964/232120896-cda7ce5e-69af-42a1-9147-9d67aa50985c.mp4)

### Index of exploits

1. [Broken Object Level Authorization](./solutions/broken-object-level-authorization.md)
2. [Broken User Authentication](./solutions/broken-user-authentication.md)
3. [Excessive Data Exposure](./solutions/excessive-data-exposure.md)
4. [Lack of Resources and Rate Limiting](./solutions/lack-of-resources-rate-limiting.md)
5. [Injections](./solutions/injections.md)
