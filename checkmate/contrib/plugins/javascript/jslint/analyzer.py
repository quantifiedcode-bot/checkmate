# -*- coding: utf-8 -*-
"""
This file is part of checkmate, a meta code checker written in Python.

Copyright (C) 2015 Andreas Dewes, QuantifiedCode UG

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import unicode_literals
from __future__ import absolute_import

import os
import tempfile
import json
import subprocess

import checkmate.settings as settings
from checkmate.lib.analysis.base import BaseAnalyzer

class JSLintAnalyzer(BaseAnalyzer):

    def summarize(self,items):
        pass

    def analyze(self,file_revision):
        issues = []
        f = tempfile.NamedTemporaryFile(delete = False)
        try:
            with f:
                f.write(file_revision.get_file_content())
            try:
                result = subprocess.check_output(["jslint",
                                                  "--json",
                                                  f.name])
            except subprocess.CalledProcessError as e:
                if e.returncode == 1:
                    result = e.output
                else:
                    raise
            json_result = json.loads(e.output)

            for issue in json_result[1]:
                issues.append({
                    "code": issue["code"],
                    "location": ((issue["line"], issue["character"]),
                                 (issue["line"], None)),
                    "data": issue})

        finally:
            os.unlink(f.name)
        return {'issues' : issues}
