# Outline Bridge Server

This repository contains V2Ray Docker Compose files to run a bridge server for the Outline proxy.
It helps Outline proxy to work in highly restricted networks.

## Documentation

### Outline

[Outline](https://getoutline.org) is a Shadowsocks-based proxy created by Google.
It lets you create and manage Shadowsocks servers easily.
Outline clients are well-designed applications available for all platforms.

It usually works as below.

```
[Outline client] <-> [Outline server] <-> (Internet)
```

Read the [Outline official documentation](https://getoutline.org/get-started) to set up an Outline server using the Outline Manager application.

### The Bridge Server

The bridge server will be inserted between clients and a server to connect the clients to the server
in networks where this connection is not possible directly.
It runs a V2Ray proxy to pass the incoming Shadowsocks traffic from clients to the Outline server.

The bridge server changes the flow as below.

```
[Outline client] <-> [V2Ray server] <-> [Outline server] <-> (Internet)
```

#### Setup the bridge server

Follow these steps to run the V2Ray proxy on the bridge server.

1. Install Docker and Docker-compose.
1. Clone this repository into the bridge server.
1. Run `./setup.py` script. It gets the following inputs:
    1. `Outline Server Hostname`: Find it in Outline Manager > {Server} > Settings > Hostname
    1. `Outline Server Port`: Find it in Outline Manager > {Server} > Settings > Port
    1. Allow the port for incoming/outcoming traffic if you have a firewall.
1. Run `docker-compose up -d`.
1. Open Outline Manager and change the server hostname to the bridge server IP address.

Important: After updating the hostname in the Outline Manager application, remove old keys and generate them again.

### Docker images

* GitHub:
    * Image: ```ghcr.io/getimages/v2fly-core:v4.45.2```
    * URL: https://github.com/orgs/getimages/packages/container/package/v2fly-core
    * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`
* Docker Hub:
    * Image: ```v2fly/v2fly-core:v4.45.2```
    * URL: https://hub.docker.com/r/v2fly/v2fly-core/tags
    * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`

## More

* [V2Ray Docker Compose (Bridge and Upstream Servers)](https://github.com/miladrahimi/v2ray-docker-compose)
