import json
import os

from minuteinbox import Inbox


def restore_cached_inbox(workflow):
    try:
        path = f"{workflow.cache.cachedir}/cache.json"

        with open(path) as file:
            cache = json.loads(file.read())
    except FileNotFoundError:
        return None

    address = cache["address"]
    token = cache["token"]

    inbox = Inbox(
        address=address,
        token=token,
    )

    _ = inbox.expires_in

    return inbox


def delete_cached_inbox(workflow):
    path = f"{workflow.cache.cachedir}/cache.json"
    os.remove(path)


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
