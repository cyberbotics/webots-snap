#!/usr/bin/env python

# Copyright 1996-2019 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test build dependencies."""

import os
import unittest
import yaml


class TestBuildDependencies(unittest.TestCase):
    """
    Unit test of the project structure.

    Currenlty on the worlds are test.
    """

    def setUp(self):
        """Get dependencies from snapcraft and travis file."""
        filePAth = os.path.dirname(os.path.realpath(__file__))

        self.snapcraftDependencies = []
        with open(os.path.join(filePAth, '..', 'snapcraft.yaml')) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.snapcraftDependencies = set(data['parts']['webots']['build-packages'])

        self.travisDependencies = ['python3.5-dev']
        with open(os.path.join(filePAth, '..', '.travis.yml')) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.travisDependencies = set(data['jobs']['include'][1]['addons']['apt']['packages'] + self.travisDependencies)

    def test_build_dependencies(self):
        """Test that the 'worlds' directory is correct."""
        self.assertTrue(
            self.snapcraftDependencies == self.travisDependencies,
            msg='Snapcraft "build-packages" and Travis "apt-packages" not equal'
        )


if __name__ == '__main__':
    unittest.main()
