from typing import List
from constants import HOME_DIRECTORY_PATH, SSH_DIRECTORY_PATH
from models.git_config import GitConfig
from models.profile import Profile
from models.ssh_config import SshConfig


profiles: List[Profile] = [
    Profile(
        name='orange-github',
        directory=f'{HOME_DIRECTORY_PATH}/Documents/OrangeGitHub',
        ssh_config=SshConfig(
            host='orange-github',
            hostname='github.com',
            forward_agent=True,
            preferred_authentication='publickey',
            identity_file=f'{SSH_DIRECTORY_PATH}/orange-github',
            user='git',
        ),
        git_config=GitConfig(
            user_name='orange-anjou',
            user_email='raphael.anjou@orange.com'
        )
    )
]