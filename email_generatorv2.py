import sys

def generate_email_addresses(username_file, domain, output_file):
    email_addresses = []
    with open(username_file, 'r') as file:
        usernames = file.readlines()
    for username in usernames:
        username = username.strip()
        email = f"{username}@{domain}"
        email_addresses.append(email)
    with open(output_file, 'w') as file:
        file.write('\n'.join(email_addresses))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py username_file domain output_file")
    else:
        username_file = sys.argv[1]
        domain = sys.argv[2]
        output_file = sys.argv[3]
        generate_email_addresses(username_file, domain, output_file)
        print("Email addresses generated and saved in the output file.")
