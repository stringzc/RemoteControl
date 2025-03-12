from cryptography.fernet import Fernet
from django.conf import settings
import secrets
import string

# 加密函数
def encrypt_data(data):
    cipher_suite = Fernet(settings.FERNET_KEY.encode())
    return cipher_suite.encrypt(data.encode()).decode()

# 解密函数
def decrypt_data(encrypted_data):
    cipher_suite = Fernet(settings.FERNET_KEY.encode())
    return cipher_suite.decrypt(encrypted_data.encode()).decode()

# 生成45位随机ID
def generate_planid():
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(45))