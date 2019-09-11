import numpy as np 

def dice_score(GT, PR):
## the input of Grounf Truth and Prediciton are all PIL.Image datatype
	GT = np.array(GT.convert('L').astype(np.bool))

	PR = np.squeeze(np.array(PR.convert('L')))
	PR = (np.clip(PR, 0, 255)>5).astype(np.bool) ## remove background noise in predicitons

	im_sum = PR.sum() + GT.sum()
	intersection = np.logical_and(PR,GT)

	dice = 1.*intersection.sum()/(im_sum - intersection.sum())

	GTunique, GTcounts = np.unique(GT, return_counts = True)
	PRunique, PRcounts = np.unique(PR, return_counts = True)

	print("GT", GTunique, GTcounts)
	print("PR", PRunique, PRcounts)
	print("intersection", intersection.sum())
	print("sum", im_sum - intersection.sum())
	print("dice", dice)