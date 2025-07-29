log_file_path = "log.txt"

total_requests = 0
unauthorized_requests = 0

with open(log_file_path, "r") as file:
    for line in file:
        if "HTTP/1.1" in line:
            total_requests += 1
            spilt_line = line.split()
            if spilt_line[-1] == "401":
                unauthorized_requests += 1

percentage = (unauthorized_requests / total_requests) * 100
print(f"percentage of unauthorized requests: {percentage:.2f}%")
