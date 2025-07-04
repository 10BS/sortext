import os
import shutil
from pathlib import Path


class Operator:
    @staticmethod
    def make_move(
        source: str | Path,
        destination: str | Path
    ) -> None:
        """
        Moving entries from `source` to `destination`
        :param source: from where moving entries
        :param destination: to where moving entries
        :return: None
        """
        os.makedirs(destination, exist_ok=True)
        shutil.move(source, destination)
