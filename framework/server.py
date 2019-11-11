import socket

def log(*param, **args):
    print(*param, **args)

#method path head(dict) body
def parsed_request(r):
    col_head, body = r.split("\r\n\r\n", 1)
    col, head = col_head.split("\r\n", 1)
    method = col.split()[0]
    path = col.split()[1]
    headDict = dict()
    hs = head.split("\r\n")
    for item in hs:
        key, value = item.split(":", 1)
        headDict[key] = value
    return method, path, headDict, body


def response_from_path(path):
    routers = {
        "/": index,
        "/img": img,

    }
    response = routers.get(path, error)
    return response()


def index():
    pass


def img():
    with open("static/doge.gif", "rb") as f:
        head = b"http/1.1 200 ok\r\n"
        head += b"Content-Type:image/gif\r\n"
        image = head + b'\r\n' + f.read()
        log('img ', image)
        return image


def error():
    pass


def run(host='', port=3000):
    with socket.socket() as s:
        s.bind((host, port))
        log('start at', '{}:{}'.format(host, port))
        while True:
            s.listen(5)
            connection, address = s.accept()
            r = connection.recv(1000)
            r = r.decode('utf-8')
            if len(r.split()) < 2:
                continue
            method, path, head, body = parsed_request(r)
            log(method, path, head, body)
            response = response_from_path(path)
            # 把响应发送给客户端
            connection.sendall(response)
            # 处理完请求, 关闭连接
            connection.close()


if __name__ == '__main__':
    # 生成配置并且运行程序
    config = dict(
        host='',
        port=3000,
    )
    run(**config)

