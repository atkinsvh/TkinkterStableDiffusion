#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:50:00 2024

@author: neurolady
"""

def img2img():
    import torch
    from torch import autocast
    from diffusers import StableDiffusionImg2ImgPipeline
    from PIL import Image
    from tkinter.simpledialog import askstring, askfloat

    # Path to the local model directory
    model_path = "/home/neurolady/Desktop/StableDiffusion/stable-diffusion/models/ldm/stable-diffusion-v1-4"

    # Load the model
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        local_files_only=True
    ).to("cuda")

    # Define the prompt, initial image, and strength
    prompt = askstring("Input", "Enter the prompt for the image:")
    init_img_path = askstring("Input", "Enter the path to the initial image:")
    strength = askfloat("Input", "Enter the strength of the transformation:")

    # Load the initial image
    init_image = Image.open(init_img_path).convert("RGB")
    init_image = init_image.resize((512, 512))

    # Generate the image
    with autocast("cuda"):
        images = pipe(prompt=prompt, image=init_image, strength=strength).images

    # Save the generated image
    output_path = init_img_path.replace(".jpg", "_output.jpg").replace(".png", "_output.png")
    images[0].save(output_path)
    messagebox.showinfo("Image-to-Image", f"Image saved as {output_path}")
