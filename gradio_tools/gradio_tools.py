# coding = utf-8
import gradio as gr 


"""
    MyButton 按钮工具
    
    args:
        - start: 开始按钮文字
        - end: 结束按钮文字
        - state: 按钮状态
    functions:
        - __call__(is_running: bool, *args, **kwargs) -> gr.Button
            - is_running: 按钮状态
            value 和 variant 自动根据状态变化
        - update(start: str) -> gr.Button
        - get_button_start() -> bool
        
    example:
        @mybutton_wrapper
        def btn_run_func(btn_obj: MyButton, btn_start: str) -> tuple[gr.Button, ...]:

            returnResult: tuple[gr.Button, ...] = (
                btn_obj.update(btn_start), f"{btn_obj.get_button_start()}"
            )
            return returnResult
    


        with gr.Blocks() as demo:
            gr.Markdown("# 按钮示例")
            test_btn: gr.Button = btn_run_func(False)[0]
            text = gr.Textbox(label="test")


            test_btn.click(
                fn=btn_run_func, 
                inputs=[test_btn], 
                outputs=[test_btn, text],
            )

            demo.launch()
"""

class MyButton:
    def __init__(self, start ="点击运行", end = "运行中..."):
        self.state: bool = False
        self.start: str = start
        self.end: str = end
        
    def __call__(self, is_running: bool, *args, **kwargs) -> gr.Button:
        self.state = is_running
        return gr.Button(
            value=self.start if not is_running else self.end,
            variant="primary" if not is_running else "secondary",
            scale=1,
            *args, **kwargs
        )
    
    def update(self, btn_start: str) -> gr.Button:
        # print(f"btn_start: {btn_start}, self.start: {self.start}")
        # gr.Button.click -> value
        self.state = btn_start == self.start
        return self(self.state)

    def get_button_state(self) -> bool:
        return self.state
    
    def get_button_state_info(self) -> str:
        return self.start if not self.state else self.end
    
    def get_button_start_custom(self, btn_start: str, btn_end: str) -> str:
        return btn_start if not self.state else btn_end
    



def mybutton_wrapper(func):
    def wrapper(*args, **kwargs) -> tuple[gr.Button, str]:
        btn = MyButton()
        
        result = func(btn, *args, **kwargs)
        return result
    return wrapper



if __name__ == "__main__":
    
    @mybutton_wrapper
    def btn_run_func(btn_obj: MyButton, btn_start: str) -> tuple[gr.Button, ...]:
        """
            按钮运行函数
        """

        returnResult: tuple[gr.Button, ...] = (
            btn_obj.update(btn_start), f"{btn_obj.get_button_start()}"
        )
        return returnResult
    


    with gr.Blocks() as demo:
        gr.Markdown("# 按钮示例")
        test_btn: gr.Button = btn_run_func(False)[0]
        text = gr.Textbox(label="test")


        test_btn.click(
            fn=btn_run_func, 
            inputs=[test_btn], 
            outputs=[test_btn, text],
        )

        demo.launch()