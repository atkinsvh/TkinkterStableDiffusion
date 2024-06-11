#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:47:37 2024

@author: neurolady
"""

def verify_cuda():
    import torch
    print("CUDA available: ", torch.cuda.is_available())
    print("Current device: ", torch.cuda.current_device())
    print("Device name: ", torch.cuda.get_device_name(0))
    messagebox.showinfo("Verify CUDA", "Check the console for output")
