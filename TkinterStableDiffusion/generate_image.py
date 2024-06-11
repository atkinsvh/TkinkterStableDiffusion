#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:49:09 2024

@author: neurolady
"""

def generate_image():
    import torch
    from torch import autocast
    from diffusers import StableDiffusionPipeline
    from tkinter.simpledialog import askstring

    # Path to the local model directory
    model_path = "/home/neurolady/Desktop/StableDiffusion/stable-diffusion/models/ldm/stable-diffusion-v1-4"

    # Load the model
    pipe = StableDiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        local_files_only=True
    ).to("cuda")

    # Define the prompt and filename
    prompt = askstring("Input", "Enter the prompt for the image:")
    filename = askstring("Input", "Enter the filename for the generated image (without extension): ") + ".png"

    # Generate the image
    with autocast("cuda"):
        image = pipe(prompt).images[0]

    # Save the generated image
    save_path = f"/home/neurolady/Desktop/StableDiffusion/{filename}"
    image.save(save_path)
    messagebox.showinfo("Generate Image", f"Image saved as {save_path}")
