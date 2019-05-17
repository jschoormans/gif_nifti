"""Example usage of gif_your_nifti."""

import gif_your_nifti.core as gif2nif

filename = r'/home/jschoormans/lood_storage/divi/Ima/parrec/jschoormans/carotid_DCE/2019_05_15/Results/ca_15052019_1535002_6_2_cdce-transvV4R_19_05_16_13_38CS.nii'



# Create a temporal grayscale gif.

gif2nif.write_gif_temporal(filename)


#%%

# Create a normal grayscale gif.
gif2nif.write_gif_normal(filename)

#%%
# Create a pseudocolored gif.
gif2nif.write_gif_pseudocolor(filename, colormap='plasma')

# Create a depth gif.
gif2nif.write_gif_depth(filename)

# Change the size of gifs.
gif2nif.write_gif_pseudocolor(filename, size=0.5, colormap='cubehelix')
gif2nif.write_gif_pseudocolor(filename, size=0.5, colormap='inferno')
gif2nif.write_gif_pseudocolor(filename, size=0.5, colormap='viridis')

# Create an RGB gif, based on gray matter, white matter and cerebrospinal fluid
# images from MNI template.
filename1 = 'mni_icbm152_gm_tal_nlin_asym_09c.nii'
filename2 = 'mni_icbm152_wm_tal_nlin_asym_09c.nii'
filename3 = 'mni_icbm152_csf_tal_nlin_asym_09c.nii'
gif2nif.write_gif_rgb(filename1, filename2, filename3)
