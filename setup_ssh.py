from typing import List
import os
from models.profile import Profile
from models.ssh_config import SshConfig

from constants import GENERAL_GIT_CONFIG_PATH, SSH_DIRECTORY_PATH


def create_ssh_keys(key_names: List[str]) -> None:
    """
    This function creates the different ssh keys and prints the public keys.

    :param key_names: List of the names of the keys to create.
    :return: None
    """
    print("=== Creating the ssh keys ===")
    ssh_path = f'{SSH_DIRECTORY_PATH}'
    for key_name in key_names:
        key_path = f'{ssh_path}/{key_name}'
        os.system(f'ssh-keygen -o -a 256 -t ed25519 -C "{key_name}" -f {key_path} -q -N ""')
        # TODO: Add a check to know if the key already exists and the user as overwritten it or not. If not, do not print the public key.

        path_to_public_key = f'{key_path}.pub'

        print(f"Created private key file ==> {key_path}")
        print(f"Created public key file ==> {path_to_public_key}")

        # Print the public key
        with open(path_to_public_key, 'r') as f:
            print(f"Public key for {key_name} :\n{f.read()}")



def create_ssh_configs(ssh_configs: List[SshConfig]) -> None:
    """
    This function creates the different ssh config files.

    :param ssh_configs: List of the ssh configs to create.
    :return: None
    """
    print("=== Creating the ssh config ===")
    with open(f'{SSH_DIRECTORY_PATH}/config', 'a') as f:
        f.write("# SSH config for GitLab and GitHub\n")
        for ssh_config in ssh_configs:
            print(f'Setting up ssh config for {ssh_config.host}')
            f.write(ssh_config.to_file_content())
        print(f"Modified file ==> {SSH_DIRECTORY_PATH}/config")


def create_directories(directories: List[str]):
    """
    This function creates the different directories listed in input.

    :param directories: List of the directories to create.
    :return: None
    """
    print("=== Creating the directories ===")
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory ==> {directory}")


def setup_git_config(profiles: List[Profile]):
    """
    This function creates the different git config files from the specified profiles.

    :param profiles: List of the profiles to create.
    :return: None
    """
    print(f'=== Setting up git config ===')

    for profile in profiles:
        with open(GENERAL_GIT_CONFIG_PATH, 'a') as f:
            print(f"Modified file ==> {GENERAL_GIT_CONFIG_PATH}")
            f.write(profile.to_git_config_content())

        with open(profile.git_config_profile_path, 'w') as f:
            if os.path.exists(profile.git_config_profile_path):
                print(f"Overwritting file ==> {profile.git_config_profile_path}")
            else:
                print(f"Created file ==> {profile.git_config_profile_path}")
            f.write(profile.git_config.to_file_content())
