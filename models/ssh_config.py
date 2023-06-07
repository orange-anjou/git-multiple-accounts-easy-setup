from typing import Union


class SshConfig:
    """
    This model stores the config that will be stored in the specific .ssh/config file.
    """
    def __init__(
        self,
        host: str,
        hostname: str,
        forward_agent: bool = False,
        port: Union[int, None] = None,
        preferred_authentication: Union[str, None] = None,
        identity_file: Union[str, None] = None,
        user: Union[str, None] = None,
    ):
        self.host: str = host
        self.hostname: str = hostname
        self.forward_agent: bool = forward_agent
        self.port: Union[int, None] = port
        self.preferred_authentication: Union[str, None] = preferred_authentication
        self.identity_file: Union[str, None] = identity_file
        self.user: Union[str, None] = user

    def to_file_content(self):
        """
        Method that returns the content of the custom ssh config file.
        """
        output: str = "\n"

        output += f'# === {self.host} ===\n'

        output += f'Host {self.host}\n'
        output += f'  HostName {self.hostname}\n'
        output += f'  ForwardAgent {self.forward_agent}\n'
        if self.port:
            output += f'  Port {self.port}\n'

        if self.preferred_authentication:
            output += f'  PreferredAuthentications {self.preferred_authentication}\n'

        if self.identity_file:
            output += f'  IdentityFile {self.identity_file}\n'

        if self.user:
            output += f'  User {self.user}\n'

        return output