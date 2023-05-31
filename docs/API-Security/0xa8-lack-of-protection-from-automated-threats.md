# API8:2023 Lack of Protection from Automated Threats

## Summary

Automated threats have become more profitable, smarter, and harder to protect from, and APIs are often used as an easy target for them. [Lack of Protection from Automated Threats](https://github.com/OWASP/API-Security/blob/master/2023/en/src/0xa8-lack-of-protection-from-automated-threats.md) is an API security issue where APIs expose business-sensitive functionality without considering how the functionality could harm the business if used excessively in an automated manner. Traditional protections, such as rate limiting and captchas, have become less effective. For example, an attacker who operates botnets (for scalping) gets around rate limiting because they can easily access the API from thousands of location/IP addresses worldwide in seconds. Vulnerable APIs don't necessarily have implementation bugs. They expose a business flow - such as buying a ticket or posting a comment - without considering how the functionality could harm the business if used excessively in an automated manner.

## Impact

Exploiting this security issue involves understanding the business model of the API, finding sensitive business flows, and automating access to these flows, causing harm to the business. When broken down, each attack's request represents an entirely legitimate request and cannot be identified as an attack. An attack can be identified only when looking at the sum of the requests regarding the service/application business logic. In general technical impact is not expected. However, exploitation might hurt the business in different ways, for example:

1. Prevent legitimate users from purchasing a product.
2. Lead to inflation in the internal economy of a game.
3. Allow the attacker to send excessive messages/comments and quickly spread fake news.

## Prevention

Mitigation planning should be done in two layers:

**Business** - identify the business flows that might harm the business if used excessively.
**Engineering** - choose the proper protection mechanisms to mitigate the business risk.

Some of the protection mechanisms that can be used to slow down automated threats are:

1. Device fingerprinting: Denying service to unexpected client devices (e.g., headless browsers) tends to make threat actors use more sophisticated solutions, thus more costly for them.
2. Human detection: Using a captcha or more advanced biometric solutions (e.g., typing patterns).
3. Non-human patterns: Analyze the user flow to detect non-human patterns (e.g., the user accessed the "add to cart" and "complete purchase" functions in less than one second).
4. Consider blocking IP addresses of Tor exit nodes and well-known proxies.
5. Secure and limit access to APIs consumed directly by machines (such as developer and B2B APIs). They tend to be an easy target for attackers because they often don't implement all the required protection mechanisms.

## Exploitation

There are various scenarios through which this vulnerability can be exploited. Here are a couple of examples:

**Scenario #1:** A technology company announces they will release a new gaming console on Thanksgiving. The product has very high demand, and the stock is limited. An attacker, an operator of a network of automated threats, writes code to automatically buy the new product and complete the transaction. On the release day, the attacker runs the code distributed across different IP addresses and locations. The API doesn't implement the appropriate protection and allows the attacker to buy most of the stock before other legitimate users. Later, the attacker sells the product on another platform for a much higher price.

**Scenario #2:** A ride-sharing app provides a referral program - users can invite their friends and gain credit for each friend who has joined the app. This credit can be later used as cash to book rides. An attacker exploits this flow by writing a script to automate the registration process, with each new user adding credit to the attacker's wallet. The attacker can later enjoy free rides or sell the accounts with excessive credits for cash.
