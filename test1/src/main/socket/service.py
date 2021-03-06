import socket

# 创建 socket 对象
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 获取本地主机名
host=socket.gethostname()

port=9999
# 绑定端口
serverSocket.bind((host, port))
# 设置最大连接数，超过后排队
serverSocket.listen(5)

while True:
    # 建立客户端连接
    clientSocket,addr=serverSocket.accept()
    print('连接地址 %s'.format(str(addr)))
    msg='欢迎访问'
    clientSocket.send(msg.encode('utf-8'))
    clientSocket.close()
