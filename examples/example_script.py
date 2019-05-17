"""Example usage of gif_your_nifti."""

import gif_your_nifti.core as gif2nif

filename = r'/home/jschoormans/lood_storage/divi/Ima/parrec/jschoormans/carotid_DCE/2019_05_15/Results/ca_15052019_1535002_6_2_cdce-transvV4R_19_05_16_13_38CS.nii'
filename = r'/home/jschoormans/lood_storage/divi/Projects/cosart/scans/FEM/20160803_CarotisDCE_FlipAngle15/Results/20_03082016_1524321_5_2_wip3dradialdcesenseV4R_19_05_15_14_09interp.nii'
filename = r'/home/jschoormans/lood_storage/divi/Projects/cosart/scans/FEM/20160803_CarotisDCE_FlipAngle15/Results/20_03082016_1524321_5_2_wip3dradialdcesenseV4R_19_05_15_14_09CS.nii'



# Create a temporal grayscale gif.

gif2nif.write_gif_temporal(filename,dims=[1,0,0], fps=2,size=1,coords=[70,0,0])
gif2nif.write_gif_temporal(filename,dims=[0,1,0], fps=2,size=1)
gif2nif.write_gif_temporal(filename,dims=[0,0,1], fps=2,size=1)


#%%

# Create a normal grayscale gif.
#gif2nif.write_gif_normal(filename)

