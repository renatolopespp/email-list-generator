# pentesting-tools
generate_email_addresses.py Documentation:

Description:
    This script generates email addresses by combining usernames from a file with a specified domain
    and saves the generated email addresses to an output file.

Usage:
    python generate_email_addresses.py username_file domain output_file

Arguments:
    - username_file: File containing a list of usernames, each on a new line.
    - domain: The domain to be appended to each username to form an email address.
    - output_file: The file where the generated email addresses will be saved.

Example:
    python generate_email_addresses.py usernames.txt example.com output_emails.txt

Script Flow:
    1. Read the list of usernames from the specified username_file.
    2. Combine each username with the provided domain to create an email address.
    3. Save the generated email addresses to the specified output_file.

Usage Note:
    Make sure to provide the correct number of command-line arguments:
    python generate_email_addresses.py username_file domain output_file

    If the correct number of arguments is not provided, the script will display a usage message.

Author:
    Renato Lopes

Version:
    1.0

Date:
    04/02/2024
