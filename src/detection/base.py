"""Base detection system"""

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

import json


class DetectionSystem:
    def __init__(self, data: str):
        with open(data, encoding="ascii", errors="ignore") as file:
            self.jsondata = json.loads(file.read())

    def exists_or_exception(self, name: str):
        if not self.exists(name):
            raise IndexError("Not found in the data")

    def exists(self, name: str):
        if name in self.jsondata:
            return True
        return False
