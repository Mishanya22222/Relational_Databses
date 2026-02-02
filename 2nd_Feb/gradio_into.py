import gradio as gr

def f(x,y):
    return x + y

with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            x = gr.Number(label="Input X")
            y = gr.Number(label="Input Y")
        with gr.Column():
            sum = gr.Number(label="Sum")

    x.change(fn = f, inputs = [x,y], outputs = [sum])
    y.change(fn = f, inputs = [x, y], outputs = [sum])

iface.launch()