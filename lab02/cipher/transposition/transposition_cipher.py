class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encrypt_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypt_text += text[pointer]
                pointer += key
        return encrypt_text
    
    def decrypt(self, text, key):
        # Calculate the number of rows for the matrix
        num_rows = (len(text) + key - 1) // key
        num_cols = key

        # Calculate the number of characters in the last column (it might not be full)
        num_chars_last_col = len(text) % key if len(text) % key != 0 else key

        # Create an empty matrix (list of lists)
        matrix = [[''] * num_cols for _ in range(num_rows)]
        
        # Fill the matrix with characters from the cipher text
        idx = 0
        for col in range(num_cols):
            # Determine how many rows to fill for the current column
            rows_to_fill = num_rows if col < num_chars_last_col else num_rows - 1
            for row in range(rows_to_fill):
                if idx < len(text):
                    matrix[row][col] = text[idx]
                    idx += 1

        # Read the matrix row by row to reconstruct the decrypted text
        decrypted_text = ''
        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] != '':
                    decrypted_text += matrix[row][col]
        
        return decrypted_text
