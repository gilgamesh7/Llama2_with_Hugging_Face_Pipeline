# Llama2_with_Hugging_Face_Pipeline
In this Hugging Face pipeline tutorial for beginners we'll use Llama 2 by Meta. We will load Llama 2 and run the code in the free Colab Notebook. You'll learn how to chat with Llama 2 (the most hyped open source llm) easily thanks to the Hugging Face library. 

# Links
- [Youtube video](https://youtu.be/Z6sCl6abJj4?si=vpzAZ9_6RAep25GY)
- [Llama-2 7B Model on Hugging face](https://huggingface.co/meta-llama/Llama-2-7b)
- [Llama-2 7b chat](https://huggingface.co/spaces/huggingface-projects/llama-2-7b-chat)
- [Huggingface login / logout](https://huggingface.co/docs/huggingface_hub/en/package_reference/login)
- [Enabling GPU for Pytorch on M1](https://stackoverflow.com/questions/68820453/how-to-run-pytorch-on-macbook-pro-m1-gpu)
- [Accelerated PyTorch training on Mac](https://developer.apple.com/metal/pytorch/)

- # Fails on M1 Mac
- Issue : NotImplementedError: The operator 'aten::isin.Tensor_Tensor_out' is not currently implemented for the MPS device. 
- Try on Windows and wait for a fix