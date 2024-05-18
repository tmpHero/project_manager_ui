from subprocess import Popen, PIPE
from .kill_process import *
import os

class CommandRunner:
    def __init__(self, command):
        self.command = command
        self.pid = None
        self.output = None
        self.error = None

        self._run()

    def _run(self):
        process = Popen(self.command, stdout=PIPE, shell=True)
        self.output, self.error = process.communicate()
        self.pid = process.pid
        self.output = self.output.decode('utf-8')
    

    def get_info(self):
        return f"Command: {self.command}\nPID: {self.pid}\nOutput: {self.output}"
    
    def kill(self):
        kill_process(self.pid)
        print(f"Killed process with command: {self.command}")


    def __del__(self):
        if self.pid:
            self.kill()
    


"""
    使用示例：
    run_time.py:
        import time
        def time_test():
            s = 0
            while True:
                print(f"{s}s")
                time.sleep(1)
                s+=1
        if __name__ == '__main__':
            time_test()


    command = 'python run_time.py'
    c = CommandRunnerSimple(command=command)
    time.sleep(5)
    print(c.get_info())
    del c
    
    
    

    arguments:
        command: 要执行的命令

"""

class CommandRunnerSimple:
    def __init__(self, command):
        self.command = command
        self.pid = None

        self._run()

    def _run(self):
        if type(self.command) == str:
            run_py_file = [_ for _ in self.command.split(" ") if _.endswith(".py")][0]
        elif type(self.command) == list:
            if len(self.command) != 1:
                run_py_file = [_ for _ in self.command if _.endswith(".py")][0]
            else:
                run_py_file = self.command[0]
        
        cwd: str = os.path.dirname(run_py_file)
        process = Popen(self.command, shell=True, cwd=cwd)
        # self.output, self.error = process.communicate()  # 等待进程结束
        self.pid = process.pid
        print(f"loaded process with pid: {self.pid}")
    


    def get_info(self):
        return f"Command: {self.command}\nPID: {self.pid}\n"
    
    def kill(self):
        kill_process(self.pid)
        print(f"Killed process with command: {self.command}\n")

    def __del__(self):
        if self.pid:
            self.kill()
        del self  # 删除对象







if __name__ == '__main__':
    import time
    from queue import Queue

    # q = Queue()

    # command = r'python run_time.py'
    # q.put(CommandRunnerSimple(command=command))
    # # q.put(CommandRunnerSimple("ls -l"))
    
    # while not q.empty():
    #     c = q.get()
    #     print(c.get_info())
    #     time.sleep(1)
    #     q.task_done()


    command = r'project\test_project_2\emo_cluster.exe'
    c = CommandRunnerSimple(command=command)
    time.sleep(5)
    print(c.get_info())
    del c
