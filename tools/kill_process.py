import psutil
import os


"""
    Kill process on Windows
    
    @param process_pid: process id
    @return: None
    @raise: None
    @version: 1.0.0
    @since: 1.0.0
"""
def kill_process_windows(process_pid: int):
    os.system(f"taskkill /t /f /pid {process_pid}")
    print(f"kill process: {process_pid}")


"""
    Kill process on Linux and windows
    
    @param process_pid: process id
    @return: None
    @raise: None
    @version: 1.0.0
    @since: 1.0.0
"""
def kill_process(process_pid: int):
    try:
        process = psutil.Process(process_pid)
        # kill all children processes
        for child in process.children(recursive=True):
            child.terminate()
        process.terminate()
        print(f"Killed process with PID: {process_pid}")
    except psutil.NoSuchProcess:
        print(f"No such process with PID: {process_pid}")




