from constants import GENERAL_GIT_CONFIG_PATH
from models.ssh_config import SshConfig
from models.git_config import GitConfig

class Profile:
    """
    This model represents all the information needed to create a complete profile.
    """
    def __init__(
            self,
            name: str,
            directory: str,
            ssh_config: SshConfig,
            git_config: GitConfig,
    ):
        self.name: str = name
        self.directory: str = directory
        self.ssh_config: SshConfig = ssh_config
        self.git_config: GitConfig = git_config
        self.git_config_profile_path: str = f'{GENERAL_GIT_CONFIG_PATH}-{self.name}'

    def to_git_config_content(self) -> str:
        """
        Method that returns the content to add to the git config file.
        """

        output = f'\n# {self.name}\n'
        output += f'[includeIf "gitdir:{self.directory}/"]\n'
        output += f'      path = {self.git_config_profile_path}\n'

        return output