"""Example usage of gif_your_nifti."""

import gif_your_nifti.core as gif2nif

filename = r'/home/jschoormans/lood_storage/divi/Ima/parrec/jschoormans/carotid_DCE/2019_05_15/Results/ca_15052019_1535002_6_2_cdce-transvV4R_19_05_16_13_38CS.nii'
filename = r'/home/jschoormans/lood_storage/divi/Projects/cosart/scans/FEM/20160803_CarotisDCE_FlipAngle15/Results/20_03082016_1524321_5_2_wip3dradialdcesenseV4R_19_05_15_14_09interp.nii'



# Create a temporal grayscale gif.

gif2nif.write_gif_temporal(filename,dims=[1,1,1], fps=6)


#%%

# Create a normal grayscale gif.
#gif2nif.write_gif_normal(filename)

