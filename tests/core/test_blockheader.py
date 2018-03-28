# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from unittest import TestCase

from mock import mock
from pyqrllib.pyqrllib import bin2hstr

from qrl.core import config
from qrl.core.misc import logger
from qrl.core.BlockHeader import BlockHeader
from qrl.crypto.misc import sha256

logger.initialize_default()


class TestBlockHeader(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBlockHeader, self).__init__(*args, **kwargs)

    def test_init(self):
        block_header = BlockHeader()
        self.assertIsNotNone(block_header)  # just to avoid warnings

    def test_init2(self):
        block_header = BlockHeader.create(1, sha256(b'prev'), sha256(b'txs'), 10)
        self.assertIsNotNone(block_header)  # just to avoid warnings

    def test_blob(self):
        with mock.patch('qrl.core.misc.ntp.getTime') as time_mock:
            time_mock.return_value = 1615270948

            block_header = BlockHeader.create(1, sha256(b'prev'), sha256(b'txs'), 10)
            self.assertEquals('74aa496ffe19107faaf418b720fb5b8446ba4b595c178fcf099c99b3dee99860d788c77910a9ed000000'
                              '0000000000e0d022b37421b81b7bbcf5b497fb89408c05c7d713c5e1e5187b02aa9344cf83bb20846e5d',
                              bin2hstr(block_header.mining_blob))
            self.assertEquals(config.dev.mining_blob_size, len(block_header.mining_blob))

    def test_hash(self):
        with mock.patch('qrl.core.misc.ntp.getTime') as time_mock:
            time_mock.return_value = 1615270948

            block_header = BlockHeader.create(1, sha256(b'prev'), sha256(b'txs'), 10)
            header_hash = block_header.generate_headerhash()

            self.assertEquals('c876626d034dbd1de177e39c2f81f4cb4cf54c4c975a72ff39d824074ce18d3d',
                              bin2hstr(header_hash))

            self.assertEquals(bin2hstr(header_hash),
                              bin2hstr(block_header.headerhash))

            self.assertEquals(32, len(block_header.headerhash))

    def test_hash_nonce(self):
        with mock.patch('qrl.core.misc.ntp.getTime') as time_mock:
            time_mock.return_value = 1615270948

            block_header = BlockHeader.create(1, sha256(b'prev'), sha256(b'txs'), 10)

            block_header.set_nonces(100, 0)

            header_hash = block_header.generate_headerhash()

            self.assertEquals('dd731f035b97315d2e527a44660135cb9d680e9f7d2bdec8f4f045a0e3c6010f',
                              bin2hstr(header_hash))

            self.assertEquals(bin2hstr(header_hash),
                              bin2hstr(block_header.headerhash))

            self.assertEquals(32, len(block_header.headerhash))
