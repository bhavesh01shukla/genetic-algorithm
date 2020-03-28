import numpy 
import random
from client_moodle import get_errors , submit 	

team_id='St0WqOenu3543rZHrK2slWsnWWaRxtPXMeXynMX7GJQK2ERUva'

population=[]
num_weights = 11
num_solution = 10 #Defining the no of chromosomes.

pop_size = (num_solution,num_weights) # The population will have solution chromosomes where each chromosome has num_weights genes.

### Step 0 :: Create the initial population.
new_population = numpy.random.uniform(low=-10.0, high=10.0, size=pop_size)
print("pop_size:",pop_size)
print(new_population)


#### check if server works for giver overfit list
overfit=[0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
print("overfit",type(overfit))
error_val=get_errors(team_id,overfit)
print("error_val:",error_val)

fitness_list=[]
error_list=[]
### step1:: find the error for each chromosome
for i in range(0,num_solution):
	print(i)

	#### change new_population[i] to a list of length 11 
	temp=numpy.copy(new_population[i])
	new_list=numpy.array(temp).tolist()

	error_val=get_errors(team_id,new_list) ### error val is a python array of 2 values(error)
	print("idx:",i,"\t","error_val:",error_val)

### now call fitness function and assgn fitness values according to their error values	
	fitness_list.append(error_val[0]+error_val[1])
	error_list.append([error_val[0],error_val[1]])

# ### step2 :: select parent for cross-over 			

# ### step3 :: cross-over
# ### step4 :: mutation
# ### step4 :: create new_population