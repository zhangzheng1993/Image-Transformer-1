# Import
from imgTransformer import Transformer
import cv2

# Instantiation
data_transformer = Transformer(transform_boxes = True)
'''
parameter transform_boxes lets you specify if you want to suppy the corresponding bounding box annotations as well and get the transformed boxes too. Defaults to False
'''

# Affine transformation parameters
tx_range = (-20,20)	# Translate in x direction by n pixels where n is picked randomly from the range - (-20,20)
ty_range = (-20,20)	# Translate in y direction by n pixels where n is picked randomly from the range - (-20,20)
rot_range = (-30,30) # Rotate by an angle theta where theta is picked randomly from the range - (-30,30)
shear_range = 5 # Apply a shear transform with shear coefficient being 5

# Supply these parameters to the data_transformer object
data_transformer.set_params(tx_range,ty_range,rot_range,shear_range)

# Load an image
img = cv2.imread('0.JPEG') # numpy matrix with dimensions - (height,width,channels)

'''
Specify bounding boxes(dummy box taken here)
A list of list where each bounding boxes is a list of size 4 with elements(in order) - 

1. X coordinate of top left vertex
2. Y coordinate of top left vertex
3. X coordinate of bottom right vertex
4. Y coordinate of bottom right vertex

'''
boxes = [[132, 85, 251, 275]] # dummy box

# Apply the transform
img_trans, boxes_trans = data_transformer.applyTransforms(img,boxes,num_transforms = 2) # num_transforms specifies how many consecutive affine transformations should be applied.

# draw the bounding boxes for visualization
cv2.rectangle(img,(boxes[0][0],boxes[0][1]),(boxes[0][2],boxes[0][3]),color = (255,0,0))
cv2.rectangle(img_trans,(boxes_trans[0][0],boxes_trans[0][1]),(boxes_trans[0][2],boxes_trans[0][3]),color = (255,0,0))

# Store the files - 
cv2.imwrite('original.JPEG',img)
cv2.imwrite('transformed.JPEG',img_trans)
