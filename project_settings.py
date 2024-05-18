import os
from tools.kill_process import *
from tools.process_tools import *
from gradio_tools.gradio_tools import *
from queue import Queue
from settings import *

start_process_click = lambda queue, process: queue.put(CommandRunnerSimple(process)) 
kill_process_click = lambda queue: None if queue.empty() else queue.get()

def btn_run_func_wrapper(*args):

    queue, command = args[0], args[1]
    @mybutton_wrapper
    def btn_run_func(btn_obj: MyButton, *args, **kwargs) -> tuple[gr.Button, ...]:
        btn_start = args[0]
        returnResult: list = [
            btn_obj.update(btn_start), f"{btn_obj.get_button_start_custom('None', 'running')}",
        ]
        """
            按钮运行函数
        """
        start_process_click(queue, command) \
        if btn_obj.get_button_state() else kill_process_click(queue=queue)
        
        return returnResult
    
    return btn_run_func


os.makedirs("project", exist_ok=True)


# queue_project_time = Queue()
# btn_run_func = btn_run_func_wrapper(queue_project_time, PROCESS_LIST[0])

btn_run_func_lst: list = []
queue_list: list = []
for cnt in range(len(PROCESS_LIST)):
    queue_list.append(Queue())
    btn_run_func_lst.append(
        btn_run_func_wrapper(queue_list[cnt], PROCESS_LIST[cnt])
    )

# print(btn_run_func_lst)