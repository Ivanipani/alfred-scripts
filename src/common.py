import json
import subprocess
from typing import List, Union
from dataclasses import dataclass


@dataclass
class AlfredJsonFormatItem:
    title: str
    subtitle: str = ""

    def to_dict(self):
        return {"title": self.title, "subtitle": self.subtitle}


class AlfredJsonFormatList:
    def __init__(self, items: List[AlfredJsonFormatItem]):
        self.items = items

    def to_json_str(self):
        return json.dumps({"items": [i.to_dict() for i in self.items]})

    @classmethod
    def from_list(cls, l: List[str]):
        return cls([AlfredJsonFormatItem(title=i) for i in l])


def run_command(cmd: Union[str, List[str]], shell: bool = False):
    """Run a shell command and return the output as a utf-8 encoded string.

    If shell is False, cmd should be a list of strings. Otherwise, cmd should be a string.

    Raises CalledProcessError if the command returns a non-zero exit status.
    """

    result = subprocess.run(cmd, shell=shell, check=True, stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8").strip()
