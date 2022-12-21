import sys
from datetime import timedelta

from pyflow import Workflow

import utils


def main(workflow):
    inbox = utils.restore_inbox(workflow)
    inbox.extend_10m()

    workflow.new_item(
        title=f"{inbox.address} expires in {timedelta(seconds=inbox.expires_in)}",
        subtitle="Added 10 minutes to expiration",
        arg=inbox.address,
        valid=True,
    ).set_icon_file(
        path="./img/icons/extend.png",
    )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
