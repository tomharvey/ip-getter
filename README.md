# IP-Getter

The minimum amount of python to get a service which will tell me my IP.

## Why?

When behind a NAT and I need to know my WAN IP address I've used a
[variety](http://ifconfig.me) of [services](http://checkmyip.net) to find out,
both directly and through the [ipgetter](https://github.com/phoemur/ipgetter)
package from [@phoemur](https://github.com/phoemur).

But, that ipgetter package from phoemur is dead, as is the link above, and it's
not on [pypi](https://pypi.org) anymore.

Besides, the 45 servers which ipgetter v0.6.0 made random use of were never
particularly fast and they were all HTTP (no SSL!).

So, this is a simple, easy to deploy IP reporting service - giving you your own
data management, using SSL, with API key authentication, and ever within a VPC
if you like.

I'm using it to tell my [pyftpdlib](https://github.com/giampaolo/pyftpdlib)
based FTP server what it's external IP is when it's behind NAT. But, you can
just use your own deployment of it to check your WAN IP anywhere.

It's pretty straightforward, but hopefully saves someone from having to trawl
through the lack of documentation about what's available in the `event` and the
`context` objects in a lambda api gateway request.

## Usage
### Dependancies

Requires [serverless framework](http://serverless.com) so go install that with
`npm install serverless -g`.

### Deployment
Serverless is basically some opinions about how to structure a lambda function
and a deployment framework for multi-cloud operators. This function deploys to
AWS with `sis deploy --stage production --region eu-west-1`

### Getting your IP
After deployment, `sis` will report back with an API_KEY and an
HTTPS API_ENDPOINT.

``` bash

curl -X GET \
  https://$API_ENDPOINT/production/ip-getter \
  -H 'x-api-key: $API_KEY'
```

Or you can use your favourite library to make that call from within your code.