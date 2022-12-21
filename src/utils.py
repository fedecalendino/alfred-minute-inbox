import json

from minuteinbox import Inbox


def restore_inbox(workflow):
    path = f"{workflow.cache.cachedir}/cache.json"

    with open(path) as file:
        cache = json.loads(file.read())

    address = cache["address"]
    token = cache["token"]

    inbox = Inbox(
        address=address,
        token=token,
    )

    _ = inbox.expires_in

    return inbox


def new_inbox(workflow):
    path = f"{workflow.cache.cachedir}/cache.json"

    inbox = Inbox()

    with open(path, "w+") as file:
        cache = {
            "address": inbox.address,
            "token": inbox.token,
        }

        file.write(json.dumps(cache))

    return inbox
