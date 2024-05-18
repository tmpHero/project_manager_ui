import gradio as gr
from gradio_tools import *
from settings import *
from project_settings import *


def btn_add_func(project_index):
    project_index = int(project_index)
    project_name = PROCESS_LIST_NAME[project_index]
    queue_list[project_index].put(CommandRunnerSimple(PROCESS_LIST[project_index]))
    return f"add {project_name}"

def btn_show_func(project_index):
    project_index = int(project_index)
    project_name = PROCESS_LIST_NAME[project_index]
    return f"len: {queue_list[project_index].qsize()}\n{[project_name for _ in range(queue_list[project_index].qsize())]}"

def btn_clear_func(project_index):
    project_index = int(project_index)
    # project_name = PROCESS_LIST_NAME[project_index]
    queue_list[project_index].queue.clear()
    return f"all clear"

def btn_del_func(project_index):
    project_index = int(project_index)
    project_name = PROCESS_LIST_NAME[project_index]
    if queue_list[project_index].empty():
        return f"{project_name} is empty"
    else:
        queue_list[project_index].get()
        return f"{project_name} is del"



def webui(share=False) -> None:
    # 创建一个 Gradio 界面
    with gr.Blocks() as app:
        # 添加 Gradio 组件
        gr.Markdown(
            """
            # 说明: 
            ###    settings.py 配置文件
            ###    单次:
            ###       点击运行按钮，即可运行命令
            ###    多次：
            ###       add: 添加任务，del: 删除最开始任务，clear: 清空所有任务，show: 显示当前所有任务
            #### 版本：1.0.0
            """
        )

        if len(btn_run_func_lst) == 0:
            gr.Markdown(
                """
                # 什么都没有, 打开 project 添加项目，并且配置settings.py
                """
            )
        for cnt in range(len(btn_run_func_lst)):
            with gr.Accordion(PROCESS_LIST_NAME[cnt], open=cnt==0):
                with gr.Group():
                    project_name = gr.Markdown("# ",PROCESS_LIST_NAME[cnt])
                    project_index = gr.Markdown(f"{cnt}", visible=False)
                    with gr.Row():
                        btn_running = btn_run_func_lst[cnt](False)[0]
                        text_running = gr.Textbox(label="Running", scale=9)
                    
                    with gr.Row():
                        btn_add = gr.Button(value="add")
                        btn_del = gr.Button(value="del")
                        btn_clear = gr.Button(value="clear")
                        btn_show = gr.Button(value="show")
                    text_info = gr.Textbox(label="Info", scale=9)
                    btn_running.click(fn=btn_run_func_lst[cnt], inputs=[btn_running], outputs=[btn_running, text_running])
                    
                    btn_add.click(fn=btn_add_func, inputs=[project_index], outputs=[text_info])
                    btn_del.click(fn=btn_del_func, inputs=[project_index], outputs=[text_info])
                    btn_clear.click(fn=btn_clear_func, inputs=[project_index], outputs=[text_info])
                    btn_show.click(fn=btn_show_func, inputs=[project_index], outputs=[text_info])
        

        app.launch(
            server_name='0.0.0.0',
            share=share,          
            inbrowser=True
        )

if __name__ == '__main__':

    webui()
