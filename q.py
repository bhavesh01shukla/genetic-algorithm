import numpy 
import random
from client_moodle import get_errors , submit

def create_new_pop(fitness_list):
	#### sort the current pop according to their fitness value
	fitness_list=sorted(fitness_list,key = lambda x: x[1])
	new_pop=numpy.zeros(pop_size)
	
	### now select 5 from fitness_list[2] using probability i.e. chromosome into new_pop numpy array
	### use these 5 to create 20 chromosomes using  cross over and mutation 
	return new_pop


team_id='St0WqOenu3543rZHrK2slWsnWWaRxtPXMeXynMX7GJQK2ERUva'

population=[]
num_weights = 11
num_solution = 20 #Defining the no of chromosomes.

pop_size = (num_solution,num_weights) #shape of population list

### Step 0 :: Create the initial population.
population = numpy.random.uniform(low=-10.0, high=10.0, size=pop_size)
print("pop_size:",pop_size)
print(population)


#### check if server works for giver overfit list given in overfit.txt
overfit=[0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
print("overfit",type(overfit))
error_val=get_errors(team_id,overfit)
print("error_val:",error_val)

fitness_list=[]
# error_list=[]
### step1:: find the error for each chromosome
for i in range(0,num_solution):
	print(i)

	#### change population[i] to a list of length 11 
	temp=numpy.copy(population[i])
	new_list=numpy.array(temp).tolist()

	error_val=get_errors(team_id,new_list) ### error val is a python array of 2 values(error)
	print("idx:",i,"\t","error_val:",error_val)

### now call fitness function and assgn fitness values according to their error values	
	fitness_list.append([i, error_val[0] + 5*error_val[1], new_list])
	# error_list.append([i,error_val[0],error_val[1]])

### step2 :: select parent for cross-over and mutation 			
### select best 20-25% and use them to generate new pop
new_pop=create_new_pop(fitness_list)  ## sort chromosomes according to their fitness value



# ### step3 :: cross-over
### one-point crossover 


# ### step4 :: mutation
# ### step4 :: create new_population
