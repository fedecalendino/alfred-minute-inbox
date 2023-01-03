import sys
from datetime import timedelta

from bs4 import BeautifulSoup
from pyflow import Workflow

import utils


def main(workflow):
    inbox = utils.restore_cached_inbox(workflow)
    new = False

    if not inbox:
        inbox = utils.new_inbox(workflow)
        new = True

    subtitle = f"expires in {timedelta(seconds=inbox.expires_in)}"

    if new:
        subtitle += " (your old inbox expired)."

    item = workflow.new_item(
        title=f"Your address in {inbox.address}",
        subtitle=subtitle,
        arg=inbox.address,
        valid=True,
    ).set_icon_file(
        path="./img/icons/inbox.png",
    )

    item.set_cmd_mod(
        arg="extend",
        subtitle="🔄 extend expiration for 10 minutes",
    )

    item.set_alt_mod(
        arg="destroy",
        subtitle="🔥 destroy this inbox",
    )

    for mail in inbox.mails:
        path = f"{workflow.cache.cachedir}/{inbox.address}.{mail.id}.html"

        with open(path, "w+") as file:
            soup = BeautifulSoup(mail.content, features="html.parser")
            [x.extract() for x in soup.findAll(["script", "style"])]

            file.write(str(soup))

        workflow.new_item(
            title=mail.subject,
            subtitle=f"{mail.sender.name} <{mail.sender.address}> · {mail.sent_at}",
            arg=path,
            valid=True,
        ).set_icon_file(
            path="./img/icons/new.png" if mail.is_new else "./img/icons/envelope.png",
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
