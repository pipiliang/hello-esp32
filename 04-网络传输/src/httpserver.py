import socket
import _thread


class SimpleHttpServer:

    def __init__(self, ip, port, num):
        self.ip = ip
        self.port = port
        self.num = num
        self.server = None

    def start(self, listen):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(self.num)
        print('waiting for connection...')
        while True:
            # 接受新连接
            sock, address = self.server.accept()
            _thread.start_new_thread(self._handle, (sock, address, listen))

    def stop(self):
        if self.server:
            self.server.close()

    def _handle(self, sock, address, listen):
        print('new connection from %s:%s...' % address)
        method, headers, body = self._parse_request(sock)
        response_body = listen(method, headers, body)
        sock.send(self._to_response(response_body))
        sock.close()
        print('Connection from %s:%s closed.' % address)

    def _to_response(self, body):
        response = 'HTTP/1.1  200  OK\r\n'
        response += 'Access-Control-Allow-Origin: *\r\n'
        response += '\r\n'
        response += body
        print('----------response----------')
        print(response)
        return response.encode('utf-8')

    def _decode(self, data):
        try:
            return data.decode()
        except Exception as e:
            return data.decode('gbk')

    def _parse_request(self, client_socket):
        # 判断并解析请求数据
        recv_data = ''
        request_header = ''  # 请求头字符串
        request_headers = {}  # 请求头解析后的字典
        body = ''  # 实体
        content_length = 0  # 实体长度
        request_line = ''  # 请求行

        while True:
            # 完整读取请求数据
            recv_data_s = client_socket.recv(256)
            print('receive data length: ', len(recv_data_s))
            # 接收的数据为空，则返回空
            if recv_data_s == b'':
                request_line = '0'
                return request_line, request_headers, body

            recv_data_s = self._decode(recv_data_s)
            # try:
            #     recv_data_s = recv_data_s.decode()
            # except Exception as e:
            #     recv_data_s = recv_data_s.decode('gbk')

            if "\r\n\r\n" not in recv_data:
                recv_data += recv_data_s
            if "\r\n\r\n" not in recv_data:
                pass
            else:
                if request_header == '':
                    # 第一次接收到， 空行 说明请求头结束
                    space_line_index = recv_data.index("\r\n\r\n")
                    request_header = recv_data[0: space_line_index]
                    body = recv_data[space_line_index + 4:]
                    for index, request in enumerate(request_header.split('\r\n')):
                        if index == 0:
                            request_line = request
                        else:
                            key = request.split(':')[0]
                            value = request.lstrip(key).lstrip(':')
                            key = key.strip(' ').lower()
                            value = value.strip(' ')
                            request_headers[key] = value

                    if "content-length" in request_headers.keys():
                        # 查看content_length是否在请求头,若在，需要获取其值
                        content_length = int(request_headers['content-length'])
                        if content_length == len(body.encode()):
                            print("receive end")
                            return request_line, request_headers, body
                    else:
                        # 不存在则说明只有请求头,没有实体
                        return request_line, request_headers, body
                else:
                    # 实体数据
                    body += recv_data_s
                    if content_length == len(body.encode()):
                        print("receive end")
                        return request_line, request_headers, body


def listen(method, headers, body):
    print('--------method------------')
    print(method)
    print('----------headers----------')
    print(headers)
    print('----------body----------')
    print(body)
    return body


if __name__ == "__main__":
    SimpleHttpServer('0.0.0.0', 9999, 1).start(listen)
