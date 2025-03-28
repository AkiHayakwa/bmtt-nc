from block import Block
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transaction = []
        # Tạo block Genesis (block đầu tiên) với proof = 1 và previous_hash = '0'
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transaction, proof)
        self.current_transaction = []  # Reset danh sách giao dịch cho block tiếp theo
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            # Tính toán hash theo công thức: hash = sha256(new_proof^2 - previous_proof^2)
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # Kiểm tra 4 chữ số '0' đầu tiên trong hash
                check_proof = True
            else:
                new_proof += 1
        return new_proof  # Trả về proof hợp lệ

    def add_transaction(self, sender, receiver, amount):
        self.current_transaction.append({'sender': sender, 'receiver': receiver, 'amount': amount})
        # Trả về index của block tiếp theo
        return self.get_previous_block().index + 1

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            
            # Kiểm tra previous_hash của block có trùng với hash của block trước đó không
            if block.previous_hash != previous_block.hash:
                return False

            # Kiểm tra tính hợp lệ của proof_of_work
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':  # Kiểm tra xem hash có chứa 4 chữ số '0' ở đầu hay không
                return False

            previous_block = block
            block_index += 1
        return True
