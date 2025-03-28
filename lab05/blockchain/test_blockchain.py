from blockchain import Blockchain

my_blockchain = Blockchain()
# Thêm các giao dịch vào blockchain
my_blockchain.add_transaction('Alice', 'Bob', 10)
my_blockchain.add_transaction('Bob', 'Charlie', 5)
my_blockchain.add_transaction('Charlie', 'Alice', 3)

# Lấy block trước đó để tính toán proof cho block mới
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof

# Tính toán proof mới bằng cách sử dụng phương thức proof_of_work
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash

# Thêm giao dịch của miner và tạo block mới
my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# In thông tin tất cả các block trong blockchain
for block in my_blockchain.chain:
    print(f"Block#{block.index}")
    print("Timestamp: ", block.timestamp)
    print("Transactions: ", block.transactions)
    print("Proof:", block.proof)
    print("Previous hash: ", block.previous_hash)
    print("Hash: ", block.hash)
    print("-----------------------------------------")

# Kiểm tra tính hợp lệ của blockchain
print("Is Blockchain Valid: ", my_blockchain.is_chain_valid(my_blockchain.chain))
