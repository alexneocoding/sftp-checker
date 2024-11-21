import paramiko
from paramiko import SSHClient, RSAKey
import json
import argparse
import os
from rich import print


class SFTPUtility:
    def __init__(self):
        self.ssh_client = SSHClient()

    def sftp_connect(self, alias, host, port, username, private_key_path, passphrase, list_dir='.'):
        """
        Connects to an SFTP server and lists files in the specified directory.

        :param alias: Connection alias for identification
        :param host: SFTP server hostname
        :param port: SFTP server port
        :param username: Username for authentication
        :param private_key_path: Path to the private key file
        :param passphrase: Passphrase for the private key
        :param list_dir: Directory to list files from
        """
        try:
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            private_key = RSAKey.from_private_key_file(private_key_path, password=passphrase)

            print(f"Connecting to {alias} ({host}:{port}) as {username}...")
            self.ssh_client.connect(hostname=host, port=port, username=username, pkey=private_key)

            sftp = self.ssh_client.open_sftp()
            remote_files = sftp.listdir(list_dir)
            print(f"Files in '{list_dir}': {remote_files}")

            sftp.close()
            self.ssh_client.close()

        except Exception as e:
            print(f"[red]An error occurred while connecting to {alias}: {e}[/red]")


def parse_config(config_path):
    """
    Parses a JSON configuration file.

    :param config_path: Path to the JSON configuration file
    :return: List of SFTP connection configurations
    """
    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description="SFTP Connection Tester")
    parser.add_argument(
        "--config",
        required=True,
        help="Path to the JSON configuration file containing connection details"
    )
    args = parser.parse_args()

    config_path = args.config
    sftp_configs = parse_config(config_path)

    if not sftp_configs:
        print("No valid configurations found. Exiting.")
        return

    utility = SFTPUtility()
    for config in sftp_configs:
        utility.sftp_connect(
            alias=config.get("alias", "Unnamed Connection"),
            host=config["host"],
            port=config["port"],
            username=config["username"],
            private_key_path=config["private_key_path"],
            passphrase=os.getenv(config.get("passphrase_env", "SFTP_PASSPHRASE"), ""),
            list_dir=config.get("list_dir", ".")
        )


if __name__ == "__main__":
    main()
