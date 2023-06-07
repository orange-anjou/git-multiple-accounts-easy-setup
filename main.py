from setup_ssh import create_directories, create_ssh_configs, create_ssh_keys, setup_git_config
from profiles_config import profiles


if __name__ == '__main__':
    key_names = [profile.name for profile in profiles]
    create_ssh_keys(key_names)

    ssh_configs = [profile.ssh_config for profile in profiles]
    create_ssh_configs(ssh_configs)

    directories = [profile.directory for profile in profiles]
    create_directories(directories)

    setup_git_config(profiles)
