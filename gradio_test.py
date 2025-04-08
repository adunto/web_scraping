import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown('## Gradio Test')
    gr.Markdown('This is a test of the Gradio library.')
    gr.Markdown('### Test 1')
    gr.Markdown('This is a test of the Gradio library.')

demo.launch(share=True)
# Create a public link to the demo
# demo.launch(share=True)
