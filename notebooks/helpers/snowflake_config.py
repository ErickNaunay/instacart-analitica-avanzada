from dotenv import load_dotenv
import os

def credenciales():
    
    load_dotenv()

    config = {
        'user': os.getenv('USERNAME'),
        'password': os.getenv('PASSWORD'),
        'account': os.getenv('ACCOUNT'),
        'database': os.getenv('DATABASE'),
        'schema': os.getenv('SCHEMA'),
        'warehouse': os.getenv('WAREHOUSE'),
        'role': os.getenv('ROLE')
    }

    return config