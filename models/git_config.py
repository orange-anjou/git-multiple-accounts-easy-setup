class GitConfig:
    """
    This model stores the config that will be stored in the specific .gitconfig file.
    """
    def __init__(
        self,
        user_name: str,
        user_email: str,
    ):
        self.user_name: str = user_name
        self.user_email: str = user_email


    def to_file_content(self) -> str:
        """
        Method that returns the content of the custom git config file.
        """
        output: str = ""

        output += f'[user]\n'
        output += f'      name = {self.user_name}\n'
        output += f'      email = {self.user_email}\n'

        return output