from redis import Redis
from .connection_options import connection_option

class RedisConnectionHandler:
    def __init__(self) -> None:
        self.__host = connection_option["HOST"]
        self.__port = connection_option["PORT"]
        self.__db = connection_option["DB"]
        self.__connection = None

    def connect(self) -> Redis:
        self.__connection = Redis(
            host=self.__host,
            port=self.__port,
            db=self.__db,
        )
        return self.__connection
    
    def get_conn(self) -> Redis:
        return self.__connection