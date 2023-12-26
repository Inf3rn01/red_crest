from src.client.api import resolvers


class Session:
    user_id: int
    FIO: str
    id_role: str
    error: str
    server_available: bool = False

    def __init__(self):
        self.server_available = type(resolvers.check_connection()) is bool

    def login(self, login_str: str, password: str):
        user_id = resolvers.login(login_str, password)

        if type(user_id) is dict:
            self.error = user_id['error']
            return

        self.error = ''

        user_data: dict = resolvers.get_user_by_id(user_id)
        self.user_id = user_data['id']
        self.FIO = user_data['FIO']
        self.id_role = user_data['id_role']
