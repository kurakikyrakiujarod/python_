import socket
import hmac

secret_key = '菜菜菜子'.encode('utf-8')
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

urandom = sk.recv(32)
hmac_obj = hmac.new(key=secret_key, msg=urandom)
sk.send(hmac_obj.hexdigest().encode('utf-8'))
print('-----')
sk.close()
