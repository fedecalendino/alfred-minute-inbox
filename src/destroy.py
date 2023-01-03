import sys

from pyflow import Workflow

import utils


def main(workflow):
    inbox = utils.restore_cached_inbox(workflow)

    if not inbox:
        return

    inbox.delete()

    utils.delete_cached_inbox(workflow)

    workflow.new_item(
        title=f"{inbox.address} has been destroyed",
        valid=True,
    ).set_icon_file(
        path="./img/icons/destroy.png",
    )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
