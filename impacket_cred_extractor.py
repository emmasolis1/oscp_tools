import re
import sys

def extract_credentials(filename):
    credentials = set()
    usernames = set()
    password_hashes = set()

    # Patterns for NTLM hashes and Kerberos keys
    ntlm_pattern = re.compile(r'^([^:]+):(\d+):([a-f0-9]{32}):([a-f0-9]{32}):')
    kerberos_pattern = re.compile(r'^([^:]+):([a-z0-9-]+):([a-f0-9]{32,})')

    with open(filename, 'r') as file:
        for line in file:
            ntlm_match = ntlm_pattern.match(line)
            kerberos_match = kerberos_pattern.match(line)

            if ntlm_match:
                username = ntlm_match.group(1)
                lm_hash = ntlm_match.group(3)
                nt_hash = ntlm_match.group(4)
                credentials.add((username, f'{lm_hash}:{nt_hash}'))
                usernames.add(username)
                password_hashes.add(f'{lm_hash}:{nt_hash}')
            elif kerberos_match:
                username = kerberos_match.group(1)
                kerberos_key_type = kerberos_match.group(2)
                kerberos_key = kerberos_match.group(3)
                credentials.add((username, f'{kerberos_key_type}:{kerberos_key}'))
                usernames.add(username)
                password_hashes.add(f'{kerberos_key_type}:{kerberos_key}')

    return credentials, usernames, password_hashes

def save_credentials(credentials, usernames, password_hashes, output_file, username_file, password_file):
    with open(output_file, 'w') as full_file, \
         open(username_file, 'w') as user_file, \
         open(password_file, 'w') as pass_file:
        
        for username, password_or_hash in sorted(credentials):
            full_file.write(f'{username}: {password_or_hash}\n')
        
        for username in sorted(usernames):
            user_file.write(f'{username}\n')
        
        for password_or_hash in sorted(password_hashes):
            pass_file.write(f'{password_or_hash}\n')

    print(f"Credentials extracted and saved to {output_file}")
    print(f"Usernames saved to {username_file}")
    print(f"Passwords/Hashes saved to {password_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract_secrets.py <secretsdump_output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "extracted_credentials.txt"
    username_file = "usernames.txt"
    password_file = "passwords_hashes.txt"
    
    credentials, usernames, password_hashes = extract_credentials(input_file)
    save_credentials(credentials, usernames, password_hashes, output_file, username_file, password_file)
