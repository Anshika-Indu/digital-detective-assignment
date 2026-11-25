# Mission 7 — How Computers Communicate

## 1. Task / objective

Explain basic network concepts, observe connectivity and DNS lookup, and describe how a browser retrieves a website.

## 2. Work completed

### Task 7.1 — Network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | Connects devices in a small local area. | A home, classroom or office network. |
| MAN | Connects networks across a city or a large campus. | A city-wide network linking several campuses. |
| WAN | Connects networks over large distances. | The Internet connects networks across countries. |
| DNS | Finds the network address associated with a domain name. | Looking up `example.com` before connecting to it. |
| Router | Forwards data between networks. | A home router sends traffic between local devices and the Internet. |
| Protocol | A shared set of rules for communication. | HTTP/HTTPS describe how browsers and web servers exchange web requests. |
| Packet switching | Breaks data into packets that can travel across a network and be reassembled. | A webpage request and its response travel in packets. |
| Client-server | A client requests a service and a server responds. | A browser requests a webpage from a web server. |

### Task 7.2 — Network observations

- `ping -c 4 example.com` received four replies with no packet loss. A connectivity test checks whether a destination responds over the network. A missing reply does not always prove that a website is down, because some servers block ping.
- `nslookup example.com` returned DNS address records. A DNS lookup shows the network address associated with a domain name. The local resolver details and IP addresses were not copied into this README.
- When a person enters a domain name in a browser, DNS helps find the address the browser needs to contact.

### Task 7.3 — What happens when a website opens?

1. The browser reads the URL and identifies the domain and protocol.
2. DNS looks up the domain and returns an address the computer can use.
3. The browser, acting as a client, sends a request using a web protocol such as HTTPS.
4. The request travels through the local network and routers, which forward packets toward the server.
5. The server processes the request and sends back a response containing page resources.
6. The browser receives the response, assembles the page and displays it to the user.

## 3. Commands / tools used

- `ping -c 4 example.com` — checked whether the example destination responded to four network requests.
- `nslookup example.com` — looked up DNS records while omitting resolver and address details from the notes.

## 4. My understanding

A network lets devices exchange data. DNS helps people use readable domain names, while routers forward packets toward their destinations. In the web example, the browser is the client and the computer that provides the page is the server. Protocols provide the rules for exchanging the request and response.

## 5. Difficulties faced

No major difficulties; both the connectivity check and DNS lookup returned results.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-07-networking/README.md` — concept table, privacy-safe command observations and website request steps.

## 8. Commit details

Commit message: `Explain networking concepts and website communication`. The mission was pushed to the GitHub `main` branch.
