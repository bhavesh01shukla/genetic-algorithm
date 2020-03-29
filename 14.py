import numpy 
import random
from client_moodle import get_errors , submit

def crossover(arr1,arr2):
    #### one-point cross-over
    shape=(2,11)
    new=numpy.zeros(shape)
    for i in range(0,11):
        prob1=random.random()
        prob2=random.random()
        if prob1<0.5:
            new[0][i]=arr2[i]
        else:
            new[0][i]=arr1[i]
        ### made 2 off-springs
        if prob2<0.5:
            new[1][i]=arr1[i]
        else:
            new[1][i]=arr2[i]
    return new

def mutate(arr):
    ### if prob < 0.25 , then mutation occurs
        ### then swap arr[i] with a random position in 2nd half of array
    for i in range(0,11):
        p = random.randrange (0,100,1)
        p = p/100
        if p < 0.3:
            #idx = random.randrange(5,11,1)
            arr[i]=random.uniform(-10,10)
                        #arr[i]=arr[idx]
                        #arr[idx]=temp

    return arr

def create_error_for_manual_testing():
    x=random.randrange(0.999999999999999e+32,9.999999999999999e+34)
    y=random.randrange(0.999999999999999e+32,9.999999999999999e+34)
    return [x,y]

def create_new_pop(error_list,population,prob):
    #### sort the current pop according to their fitness value
    new_pop=numpy.zeros(pop_size)
    error_list=sorted(error_list,key = lambda x: x[1])
    #print(numpy.size(error_list))
        ### now select top 6 from error_list[2]i.e. chromosome into new_pop numpy array	
    for i in range(0,5):
        idx = error_list[i][0]
        new_pop[i]=numpy.copy(population[idx])

        ### use these 5 to create 20 chromosomes using  cross over and mutation 
    for i in range (0,7): ## one iteration creates 2 offspring
        ind1 = random.randrange(0,5,1)
        ind2 = random.randrange(0,5,1)
        while ind1==ind2:
            ind2 = random.randrange(0,5,1)

        temp=crossover(population[ind1],population[ind2])
        new_pop[5+ i*2] = numpy.copy(temp[0])
        x=mutate(temp[0])
        new_pop[5+ i*2]=numpy.copy(x)

        new_pop[5+ i*2 +1] = numpy.copy(temp[1])
        x=mutate(temp[1])
        new_pop[5+ i*2 +1] = numpy.copy(x)

    return new_pop


team_id='St0WqOenu3543rZHrK2slWsnWWaRxtPXMeXynMX7GJQK2ERUva'

num_weights = 11
num_solution = 19 #Defining the no of chromosomes.

pop_size = (num_solution,num_weights) #shape of population list

### Step 0 :: Create the initial population.
#population = numpy.random.uniform(low=-10.0, high=10.0, size=pop_size)
# print("pop_size:",pop_size)
# print(population)


#### check if server works for giver overfit list given in overfit.txt
overfit=numpy.array([0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12])

#### create the population
population=numpy.zeros(pop_size)
for i in range(pop_size[0]):
    population[i]=numpy.copy(overfit)


# inp=numpy.copy(overfit)
# inp=numpy.array(inp).tolist()
# print("overfit",type(inp))
# error_val=get_errors(team_id,inp)
# error_val=create_error_for_manual_testing()
# print("error_val for overfit.txt:",error_val)
min_error=float('inf')
min_weights=[]
iteration=0
while(iteration < 70):
    print(iteration,'////////////////////////////////////////////////////////////////////////')
    error_list=[]
    prob=numpy.zeros(num_solution)
        ### step1:: find the error for each chromosome
    for i in range(0,num_solution):
            #### change population[i] to a list of length 11 
        temp=numpy.copy(population[i])
        new_list=numpy.array(temp).tolist()

        error_val=get_errors(team_id,new_list) ### error val is a python array of 2 values(error)
        # error_val=create_error_for_manual_testing()
        print("idx:",i,"\t","error_val:",error_val)

        ### now call fitness function and assgn fitness values according to their error values	
        total_error=error_val[0] + 4*error_val[1]
        if total_error < min_error:
            min_error=total_error
            min_weights=numpy.copy(new_list)
        error_list.append([i,total_error])
        prob[i]=total_error

    ### step2 :: select parent for cross-over and mutation 			
    ### select best 20-25% and use them to generate new pop
    new_pop=create_new_pop(error_list,population,prob)  ## sort chromosomes according to their fitness value

    print('population',population)
    print('----------------------------------------------')
    print('new population',new_pop)

    iteration+=1
    population=numpy.copy(new_pop)

print('min_error:',min_error)
print('min_weights:',min_weights)
### step3 :: cross-over
### step4 :: one-point crossover 
### step5 :: mutation
