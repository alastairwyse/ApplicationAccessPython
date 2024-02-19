#
# Copyright 2021 Alastair Wyse (https://github.com/alastairwyse/ApplicationAccessPython/)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http:#www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest

from src.string_unique_stringifier import StringUniqueStringifier

class StringUniqueStringifierUnitTests(unittest.TestCase):
    """Unit tests for the StringUniqueStringifier class."""

    def setUp(self):
        self._test_string_unique_stringifier = StringUniqueStringifier()

    def test_to_string(self):
        result: str = self._test_string_unique_stringifier.to_string("ABC")

        self.assertEqual("ABC", result)

    def test_from_string(self):
        result: str = self._test_string_unique_stringifier.from_string("ABC")

        self.assertEqual("ABC", result)

if __name__ == "__main__":
    unittest.main()