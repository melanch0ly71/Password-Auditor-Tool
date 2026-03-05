import time

print("Starting password breach check...\n")

with open("rockyou.txt", "r", errors="ignore") as f:
    rockyou = set(f.read().splitlines())

with open("sample_passwords.txt", "r") as f:
    samples = f.read().splitlines()
sample = len(samples)
safe_passwords = []

for i, password in enumerate(samples, 1):
    print(f"Checking password {i}/{len(samples)}: {password}", end='', flush=True)

    if password in rockyou:
        print(" -> BREACHED", flush=True)
    else:
        print(" -> Safe", flush=True)
        safe_passwords.append(password)
    
    time.sleep(0.0005)

with open("safe_passwords.txt", "w") as f:
    for p in safe_passwords:
        f.write(p + "\n")
safe = len(safe_passwords) 
print ("=" * 50)
print(f"{safe} safe passwords found from a total of {sample} ")
print ("=" * 50)
print("\nScan complete. Safe passwords saved in safe_passwords.txt")