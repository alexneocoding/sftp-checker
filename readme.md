# SFTP Connection Tester Utility

This utility allows users to test and validate SFTP server connections. It connects to specified SFTP servers, lists the contents of a target directory, and provides useful feedback for debugging and monitoring SFTP setups.

## Features

- Supports multiple SFTP configurations via a JSON file.
- Securely handles private key passphrases using environment variables.
- Lists remote directory contents to verify connectivity.
- Logs meaningful output for troubleshooting.
- Easy to configure and use via command-line arguments.

## Requirements

- Python 3.7+
- `paramiko` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/alexneocoding/sftp-checker.git
   cd sftp-checker

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Set up environment variables for private key passphrases:
    ```bash
    export SFTP_DEV_PASSPHRASE="your_dev_passphrase"
    export SFTP_PROD_PASSPHRASE="your_prod_passphrase"

4. Configure the config.json file
   - alias: Friendly name for the connection.
   - host: SFTP server hostname.
   - port: SFTP server port.
   - username: Username for authentication.
   - private_key_path: Path to the private key file.
   - passphrase_env: Name of the environment variable containing the passphrase.
   - list_dir: Directory to list files from (default is .).


## Usage
   ```bash
    python sftp_checker.py --config config.json
   ```
    
### Example output

   ```bash
   Connecting to Fintech DEV GCP (dev.sftp.com:2022) as user-fintech-apps-dev...
   Files in '/dev/directory': ['file1.txt', 'file2.txt', 'subfolder']
   Connection to DEV GCP successful!
   
   Connecting to Fintech PROD GCP (prod.sftp.com:2022) as user-fintech-apps...
   Files in '/prod/directory': ['file3.txt', 'file4.txt', 'archive']
   Connection to PROD GCP successful!
  ```

### Error Handling
   ```bash
    An error occurred while connecting to Fintech DEV GCP: [Errno 111] Connection refused
   ```

### License
This project is licensed under the MIT License. See the LICENSE file for details.