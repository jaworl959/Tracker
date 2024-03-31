import numpy as np 
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt
import random 
from PIL import Image

destinations = []
enyerence = []
#tozi normal    
def normalDisteribution(x,mean,sd) :

    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2) 
    return prob_density 

#az bein 0 ta 101 adad random migire y ra nemodar dar tozi normal mohasebe mikone va ehtemal hesab mikone
def getRandomByNormalDist(mean,sd) :
    while (True) :
        random_x = np.random.choice(0,101)
        probability_density = normalDisteribution(random_x, mean, sd)
        normalized_probability = (probability_density / normalDisteribution(mean,mean,sd)) * 100
        # Validation
        random_y = random.randint(0, 100)
        if random_y <= normalized_probability :
            return random_x

        

#mean & sd
# path_rgb = [239, 237, 237]
# num = random.randint(4,7)
# def getRandomCoordinants (points,startPoints,num):
#     # mean = 5
#     # sd = 5
#     #image_path = "your_image_path.jpg" 
#     #image = Image.open(image_path)
#     #random_pixels = []
# # Select random pixels and mark them in red
#     selsctedPixelsCoordinants = []
#     # for _ in range(num):
#         # selected_cordinants = random.randint(points)
    
#         # pixel_rgb = image.getpixel(selected_cordinants)
#         # if pixel_rgb == tuple(path_rgb):
#         #     selsctedPixelsCoordinants.append("(",x,",",y,")")
#         # if pixel_rgb != tuple(path_rgb):
#         #     num += 1