# ==================================================================================================
# Copyright 2015 Twitter, Inc.
# --------------------------------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==================================================================================================

import unittest

from zktraffic.base.network import BadPacket
from zktraffic.zab.quorum_packet import (
  PacketType,
  QuorumPacket
)


class ZabTestCase(unittest.TestCase):
  def test_basic(self):
    payload = '%s%s%s' % (
      '\x00\x00\x00\x02',                  # type
      '\x00\x00\x00\x00\x00\x00\x07\xd0',  # zxid
      'cchenwashere',                      # data
    )
    packet = QuorumPacket.from_payload(payload, '127.0.0.1:2889', '127.0.0.1:10000', 0)
    self.assertEqual(PacketType.PROPOSAL, packet.type)
    self.assertEqual(packet.zxid, 2000)
