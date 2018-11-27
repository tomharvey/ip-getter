"""Get my IP."""


def ip_getter(event, context):
    """Get the IP of the requester."""
    source_ip = event['requestContext']['identity']['sourceIp']

    headers = {
        "Content-Type": "text/html",
    }

    response = {
        "statusCode": 200,
        "body": source_ip,
        "headers": headers
    }

    return response
