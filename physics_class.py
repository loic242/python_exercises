# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
# train_distance = 100
bomb_mass = 1


# Write your code below: 

#This function convert a temperature in Fahrenheit to temperature in Celsius
def f_to_c (f_temp):
     c_temp =((f_temp - 32) * 5/9)
     return c_temp

f100_in_celsius = f_to_c(100)

print(f100_in_celsius)

#
#Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.
#It should then return f_temp.
#The equation you should use is:

def c_to_f (c_temp):
    f_tepm = ((c_temp*(9/5)) + 32)
    return f_tepm

c0_in_fahrenheit = c_to_f (0)

print("Our temp is: "  + str(c0_in_fahrenheit))

#Define a function called get_force that takes in mass and acceleration. It should return mass multiplied by acceleration.

def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(train_mass, train_acceleration )

print("The train force is: " + str(train_force))


#Define a function called get_energy that takes in mass and c.
#c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.
#get_energy should return mass multiplied by c squared.

def get_energy (mass, c = 3*10**8):
    return mass*c


bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " +str(bomb_energy) +" Joules")

