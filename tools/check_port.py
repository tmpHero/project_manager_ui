from subprocess import Popen, PIPE


"""
    检查Windows主机端口是否被占用
    @param port 端口号
    @return True or False
"""
def check_win_host_port(port) -> bool:
    out, _ = Popen('netstat -ano | findstr ' + str(port), stdout=PIPE, stderr=PIPE, shell=True).communicate()
    return out.decode('gbk').strip() != ''


"""
    选择一个未被占用的端口号
    @param port 端口号起始值
    @return 未被占用的端口号
"""
def select_win_host_port(port: int=7861) -> int:
    max_port = 65535
    while port != max_port:
        if check_win_host_port(port):
            port += 1
        else:
            return port
    return port





res = select_win_host_port()
print(res)

