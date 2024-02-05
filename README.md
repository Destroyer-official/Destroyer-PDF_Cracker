<div align="center">

# 🌐 Parallel PDF Password Cracker 🌐

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

</div>

⚠️ **Disclaimer:**

**IMPORTANT:** Password cracking, even for educational purposes, can be risky and may violate ethical or legal standards. Always respect copyright and digital rights. Exercise caution and ensure you have the necessary permissions before attempting to crack any PDF passwords. This script is intended for educational use only to demonstrate parallel processing and password cracking techniques. It is not intended for malicious or unauthorized use.

## 🌟 **Overview**

Harness the power of parallel processing to explore password cracking techniques in a controlled educational setting. This Python script maximizes CPU utilization to accelerate password cracking attempts on encrypted PDF files.

## 📂 **Project Structure**

```
.
├── pdf_cracker.py
├── README.md
├── requirements.txt
└── ...
```

##  🛠️ **Features**

- 🚀**Parallel Processing:** ⚡ Leverages multiprocessing and multithreading for faster password cracking.
- **Customizable Options:** ⚙️ Fine-tune chunk size, process count, and thread count for optimal performance.
- **User-friendly Interface:** 🎯 Interact with the script seamlessly through a clear command-line interface.
- **Error Handling:** ⚠️ Handles common file-related errors gracefully.
- **Logging:** 📝 Provides detailed records for debugging and analysis.

## **Usage**

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/parallel-pdf-cracker.git
    ```

2. **Navigate to the directory:**
    ```bash
    cd parallel-pdf-cracker
    ```

3. **📦 Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **✨ Execute the script:**
    ```bash
    python parallel-pdf-cracker.py -pdf <path_to_pdf_file> -password <path_to_password_list>
    ```

## **Optional Arguments**

- `-ch`: Size of password chunks for parallel processing (default: 10000).
- `-pr`: Number of parallel processes (default: 50).
- `-thr`: Number of threads per process (default: 20).

**Example Usage:**

```bash
python parallel-pdf-cracker.py -pdf "encrypted_file.pdf" -password "passwords.txt" -ch 5000 -pr 30 -thr 10
```

## 📚 How It Works

The `parallel-pdf-cracker.py` script is designed to efficiently crack the password of encrypted PDF files by leveraging parallel processing. Here's a breakdown of its key components and functionality:

1. **🔐 Password Decryption Attempt:**
    - The script attempts to decrypt the PDF file using a list of passwords provided in the specified password list file.

2. **⚡ Parallel Processing:**
    - To expedite the cracking process, the script utilizes multiprocessing to parallelize password attempts. Each chunk of passwords is processed concurrently, making the most out of the available CPU cores.

3. **🔄 Multithreading:**
    - Within each process, multithreading is employed to further optimize performance. This allows multiple password attempts to be made simultaneously within a process.

4. **🍱 Chunked Passwords:**
    - Passwords are divided into chunks based on the specified chunk size. This allows for efficient distribution of password attempts across multiple processes.

5. **⚠️ Error Handling:**
    - The script incorporates robust error handling to gracefully manage common file-related errors. Any exceptions encountered during the decryption attempts are logged for further analysis.

6. **📝 Logging:**
    - Detailed logs are generated to record important events during the password cracking process. This includes information about successful password attempts or encountered errors.

7. **⚙️ Customizable Options:**
    - Users have the flexibility to customize the chunk size, number of parallel processes, and number of threads per process through command-line arguments. This ensures adaptability to different hardware configurations.

8. **🚪 Exit Upon Success:**
    - As soon as the correct password is found, the script exits, and the correct password is displayed. This minimizes unnecessary processing once the goal is achieved.

9. **🎓 Educational Purpose Emphasis:**
    - The script is developed strictly for educational purposes and is intended to showcase the principles of parallel processing in the context of password cracking. Users are reminded to use the script responsibly and adhere to ethical and legal standards.

By understanding these key components, users can gain insights into the inner workings of the script and appreciate the efficiency achieved through parallel processing for password cracking.


## 🤝 **Contributing**

Contributions are welcome! Fork the repository, make your enhancements, and create a pull request.

### 📜 License

⚖️This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<div align="center">
</div>
```
