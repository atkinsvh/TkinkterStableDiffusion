#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:49:37 2024

@author: neurolady
"""

def generate_gif():
    import torch
    from torch import autocast
    from diffusers import StableDiffusionPipeline
    from PIL import Image
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
    prompt = askstring("Input", "Enter the prompt for the GIF:")
    filename = askstring("Input", "Enter the filename for the generated GIF (without extension): ")

    # Number of frames to generate
    num_frames = 5

    # Generate the frames
    frames = []
    for i in range(num_frames):
        with autocast("cuda"):
            image = pipe(prompt).images[0]
        frames.append(image)

    # Save the generated frames as a GIF
    save_path = f"/home/neurolady/Desktop/StableDiffusion/{filename}.gif"
    frames[0].save(save_path, save_all=True, append_images=frames[1:], duration=200, loop=0)
    messagebox.showinfo("Generate GIF", f"GIF saved as {save_path}")
