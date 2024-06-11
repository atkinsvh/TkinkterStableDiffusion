#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:51:18 2024

@author: neurolady
"""

#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import subprocess

# Import functions from other scripts
from verify_cuda import verify_cuda
from generate_image import generate_image
from generate_gif import generate_gif
from img2img import img2img
from convert_ckpt_to_diffusers import convert_ckpt_to_diffusers

root = Tk()
root.title("Stable Diffusion Toolkit")

mainframe = Frame(root, height=200, width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5, pady=5)

intro = Label(mainframe, text="Welcome to the Stable Diffusion Toolkit. Please select one of the following options:")
intro.pack(side=TOP)

verify_button = Button(mainframe, text="Verify CUDA", command=verify_cuda)
verify_button.pack()

generate_image_button = Button(mainframe, text="Generate Image", command=generate_image)
generate_image_button.pack()

generate_gif_button = Button(mainframe, text="Generate GIF", command=generate_gif)
generate_gif_button.pack()

img2img_button = Button(mainframe, text="Image-to-Image", command=img2img)
img2img_button.pack()

convert_ckpt_button = Button(mainframe, text="Convert CKPT to Diffusers", command=convert_ckpt_to_diffusers)
convert_ckpt_button.pack()

exit_button = Button(mainframe, text="Quit", command=root.destroy)
exit_button.pack(side=BOTTOM)

root.mainloop()
