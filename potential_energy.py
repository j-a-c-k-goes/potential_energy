import math

'''
PE = m * g * h

    PE   potential energy, J
    m    mass, kg
    g    gravity, 9.8 m/s2
    h    height, m

'''
''' times '''
time = (1800,3600,7680,21600,28800,43200) # seconds

''' heights '''
height_max = 1.828 # in metersb ut this is six feet
height_min = height_max / 2 # half the max height
heights = (height_min, height_max)

''' masses '''
max_mass = 9800 / 2.2 # 4500 kg or 9800 pounds
min_mass = max_mass / 2 # 4500 / 2 or 
mass = (max_mass, min_mass)

''' conversion factors '''
p = 2.20462 # pound
f = 3.28084 # feet
i = 39.37 #inch

''' potential energy formula '''
def potential_energy(m, h):
	g = 9.8 # meters per second squared, gravity constant
	potential_energy = (m)*(g)*(h)
	return potential_energy

''' setup sim '''
def run_sim(time,mass):
	for t in time:
		for m in mass:
			for h in heights:
				print()
				''' print time in minutes '''
				print(f'time\t{round(t / 60,2)} minutes')
				''' print mass in pounds '''
				print(f'mass\t{m} kg\t{round((m * p),2)} pounds')
				''' print height in inches '''
				print(f'height\t{round(h,4)} m\t{round((h * i),2)} inches')
				''' print potential energy in J '''
				print(f'PE\t{potential_energy(m,h)} J')
				print()

if __name__ == "__main__":
	run_sim(time,mass)