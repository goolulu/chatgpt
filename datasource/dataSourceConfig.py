from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# MySQL 数据库连接配置
db_config = {
    'host': '47.106.98.73',
    'user': 'root',
    'password': 'lifeng888jhWfhpo~*#',
    'database': 'chatgpt',
    'port': '3306'
}

# db_config = {
#     'host': '47.106.98.73',
#     'user': 'root',
#     'password': 'lifeng888jhWfhpo~*#',
#     'database': 'chatgpt',
#     'port': '3306'  # 通常 MySQL 默认端口是 3306
# }

# 创建 MySQL 连接引擎
engine = create_engine(
    f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

Session = sessionmaker(bind=engine)
session = Session()
