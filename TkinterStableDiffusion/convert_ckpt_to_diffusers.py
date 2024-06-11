#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:50:50 2024

@author: neurolady
"""

def convert_ckpt_to_diffusers():
    import os
    from tkinter.simpledialog import askstring

    # Get the paths
    ckpt_path = askstring("Input", "Enter the path to the checkpoint file:")
    output_path = askstring("Input", "Enter the output directory for the Diffusers model:")

    # Run the conversion script
    os.system(f"python /home/neurolady/Desktop/StableDiffusion/convert_ckpt_to_diffusers.py --checkpoint_path {ckpt_path} --dump_path {output_path}")
    messagebox.showinfo("Convert CKPT to Diffusers", f"Model converted and saved to {output_path}")
