"""
Merkle Tree Cryptographic Ledger Verifier for Batch Escrow Settlements
"""

import hashlib
from typing import List

class MerkleTreeLedger:
    def __init__(self, transaction_hashes: List[str]):
        self.leaves = [hashlib.sha256(h.encode("utf-8")).hexdigest() for h in transaction_hashes]
        self.root = self._build_tree(self.leaves)

    def _build_tree(self, nodes: List[str]) -> str:
        if not nodes:
            return "0" * 64
        if len(nodes) == 1:
            return nodes[0]

        next_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left
            combined = hashlib.sha256((left + right).encode("utf-8")).hexdigest()
            next_level.append(combined)

        return self._build_tree(next_level)

    def get_merkle_root(self) -> str:
        return self.root

    def verify_inclusion(self, transaction_hash: str, proof: List[str]) -> bool:
        current = hashlib.sha256(transaction_hash.encode("utf-8")).hexdigest()
        for sibling in proof:
            current = hashlib.sha256((current + sibling).encode("utf-8")).hexdigest()
        return current == self.root
