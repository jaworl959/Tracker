import numpy as np
import matplotlib.pyplot as plt
import random 

## roye nemodar tozi normal x random entekhab mikone y ro brmigardone va ehtemal vogho x ro hessab mikone
def randomNumNormalDist ():
    # Creating a series of data of in range of 1-50.
    x = np.linspace(1,100,200)

    #Creating a Function.
    def normal_dist(x , mean , sd):
        prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
        return prob_density
    
    #Calculate mean and Standard deviation.
    mean = 5
    sd = 5
    
    #Apply function to the data.
    pdf = normal_dist(x,mean,sd)

    #Plotting the Results
    plt.plot(x,pdf , color = 'red')
    plt.xlabel('Data points')
    plt.ylabel('Probability Density')
    plt.show()

    # Set mean and standard deviation
    mean = 50
    std_dev = 20

    # # Generate random numbers from a normal distribution
    # num_samples = 50  # Number of random samples
    # random_numbers = np.random.normal(mean, std_dev, num_samples)

    # # Print the generated random numbers
    # print(random_numbers)
    # print(normal_dist(50,50,20))

    # #all = 62.83185307179586

    # Generate random x from the x's in the graph.
    random_x = np.random.choice(x)

    # Calculate the probability density at the randomly selected x.
    probability_density = normal_dist(random_x, mean, std_dev)

    # Calculate the normalized probability.
    normalized_probability = (probability_density / 62.83185307179586) * 100
    #ehtemal vogho adad random x

    #print("Randomly selected x:", random_x)
    #print("Probability density at the selected x:", probability_density)
    print("Normalized probability:", normalized_probability)

    random_y = random.randint(0, 100)
    print(random_y)
    if random_y > normalized_probability :
        print ("probability",normalized_probability,"accepted")
    if random_y == normalized_probability :
        print ("probability",normalized_probability,"accepted")
    if random_y < normalized_probability :
        print ("probability not accepted")

randomNumNormalDist ()