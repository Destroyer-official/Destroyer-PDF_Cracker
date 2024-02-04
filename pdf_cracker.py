import argparse
import concurrent.futures
import logging
import PyPDF2

def attempt_decryption(passwords, pdf_file_path):
    """
    Attempt to decrypt the PDF file using a list of passwords.

    Args:
        passwords (list): List of passwords to attempt.
        pdf_file_path (str): Path to the PDF file.

    Returns:
        str or None: Correct password if found, otherwise None.
    """
    try:
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for password in passwords:
                if pdf_reader.decrypt(password):
                    return password  # Password is correct

    except Exception as e:
        logging.error(f"Error while attempting decryption: {e}")

    return None  # Incorrect password or an error occurred

def parallel_password_crack(pdf_file_path, password_list_path, chunk_size=10000, num_processes=50, num_threads_per_process=20):
    """
    Crack the password of a PDF file using a parallelized approach.

    Args:
        pdf_file_path (str): Path to the PDF file.
        password_list_path (str): Path to the file containing passwords.
        chunk_size (int, optional): Size of password chunks for parallel processing.
        num_processes (int, optional): Number of parallel processes.
        num_threads_per_process (int, optional): Number of threads per process.

    Returns:
        str or None: Correct password if found, otherwise None.
    """
    try:
        # Read passwords from the file
        with open(password_list_path, 'r', encoding='utf-8') as password_file:
            passwords = password_file.read().splitlines()

        # Divide passwords into chunks
        password_chunks = [passwords[i:i + chunk_size] for i in range(0, len(passwords), chunk_size)]

        # Open the PDF file for reading in binary mode
        with open(pdf_file_path, 'rb') as pdf_file:
            # Use ProcessPoolExecutor for parallel processing of chunks
            with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as process_executor:
                futures = []

                # Submit each password chunk for processing in parallel
                for chunk in password_chunks:
                    future = process_executor.submit(attempt_decryption, chunk, pdf_file_path)
                    futures.append(future)

                # Use ThreadPoolExecutor for parallel processing of results
                with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads_per_process) as thread_executor:
                    # Iterate over completed futures
                    for future in concurrent.futures.as_completed(futures):
                        result = future.result()
                        if result:
                            return result  # Exit as soon as a correct password is found

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except PermissionError as e:
        logging.error(f"Permission error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return None

def get_user_input(prompt, default_value=None):
    """
    Prompt the user for input and return the entered value.

    Args:
        prompt (str): The prompt message.
        default_value (str, optional): Default value if the user just presses Enter.

    Returns:
        str: User-entered value or default value if provided.
    """
    user_input = input(f"{prompt} [{default_value}]: ")
    return user_input if user_input else default_value


def get_command_line_arguments():
    """
    Parse command-line arguments and return the parsed arguments.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description='Parallel PDF Password Cracker')
    parser.add_argument('-pdf', help='Path to the PDF file', default=None)
    parser.add_argument('-password', help='Path to the file containing passwords', default=None)
    parser.add_argument('-ch', type=int, default=10000, help='Size of password chunks for parallel processing')
    parser.add_argument('-pr', type=int, default=50, help='Number of parallel processes')
    parser.add_argument('-thr', type=int, default=20, help='Number of threads per process')

    return parser.parse_args()

def print_command_line_instructions():
    """
    Print instructions on how to use the script and explain each command-line argument.
    """
    print("To use this script, provide the following command-line arguments:")
    print("-pdf: Path to the PDF file")
    print("-password: Path to the file containing passwords")
    print("-ch: Size of password chunks for parallel processing (default: 10000)")
    print("-pr: Number of parallel processes (default: 50)")
    print("-thr: Number of threads per process (default: 20) \n\n")

def main():
    args = get_command_line_arguments()

    # Check if no command-line arguments are provided
    if args.pdf is None and args.password is None:
        print_command_line_instructions()
        args = get_command_line_arguments()

    # Prompt user for PDF file path if not provided
    pdf_file_path = args.pdf if args.pdf else get_user_input("Enter the path to the PDF file ")

    # Prompt user for password list path if not provided
    password_list_path = args.password if args.password else get_user_input("Enter the path to the password list", "dictionary.txt")

    # Attempt to find the correct password
    correct_password = parallel_password_crack(
        pdf_file_path, password_list_path,
        chunk_size=args.ch,
        num_processes=args.pr,
        num_threads_per_process=args.thr
    )

    if correct_password:
        print(f"The correct password is: {correct_password}")
    else:
        print("Password not found in the list.")

if __name__ == "__main__":
    main()
