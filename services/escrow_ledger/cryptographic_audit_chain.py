"""
Cryptographic Tamper-Evident Ledger Audit Chain for Escrow Security Deposits
"""

import hashlib
import json
from datetime import datetime, timezone
from typing import List, Dict

class AuditBlock:
    def __init__(self, index: int, data: Dict, previous_hash: str):
        self.index = index
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_content = f"{self.index}|{self.timestamp}|{json.dumps(self.data, sort_keys=True)}|{self.previous_hash}"
        return hashlib.sha256(block_content.encode("utf-8")).hexdigest()

class CryptographicAuditChain:
    def __init__(self):
        self.chain: List[AuditBlock] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = AuditBlock(0, {"event": "GENESIS_ESCROW_LEDGER"}, "0" * 64)
        self.chain.append(genesis)

    def append_event(self, event_data: Dict) -> AuditBlock:
        prev_hash = self.chain[-1].hash
        new_block = AuditBlock(len(self.chain), event_data, prev_hash)
        self.chain.append(new_block)
        return new_block

    def verify_chain_validity(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]
            if current.previous_hash != prev.hash:
                return False
            if current.hash != current.compute_hash():
                return False
        return True
