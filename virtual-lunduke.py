"""Virtual Lunduke: Detects programs on your system that Lunduke wouldn't approve of."""

# This file is a part of Virtual Lunduke.
# Copyright (C) 2025 NexusSfan <nexussfan@duck.com>

# Virtual Lunduke is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Virtual Lunduke is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Virtual Lunduke. If not, see <https://www.gnu.org/licenses/>.

import sys
import json
import socket
import detection


def addition(lst: list, arg: str):
    if not lst:
        if not lst:
            lst.append(
                f"\t\tWoke applications installed on {socket.gethostname()}"
            )
        lst.append("")
    lst.append(arg)
    return lst

def check_all(data: list, detectsys):
    total_results = []
    for program in data:
        results = detectsys.check(program)
        if results:
            results_str = ", ".join(results)
            programlen = len(program)
            spaceslen = 20 - programlen
            spaces = " " * spaceslen
            total_results = addition(total_results, f"{program}{spaces}{results_str}")
    if sys.implementation.name == "cpython":
        total_results = addition(total_results, "CPython             python3")
    if not total_results:
        total_results.append(f"No woke applications installed on {socket.gethostname()}! I'm sure Lunduke would be happy.")
    return total_results


if __name__ == "__main__":
    with open("data/apps.json", encoding="ascii", errors="ignore") as filedata:
        appdata = json.loads(filedata.read())
    detection_systems = detection.get_detection_system()
    DETECT_DATA = f"data/{detection_systems[1]}.json"
    detection_system = detection_systems[0](DETECT_DATA)
    result = check_all(appdata, detection_system)
    print("\n".join(result))
