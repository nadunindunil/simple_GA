import random, string , time, operator

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

name = "nadunindunil"


population = []
popSize = 10000

# introducing the population
for i in range(0,popSize):
    population.append(randomword(len(name)))

def selection(population):
    selected = []
    d = {}
    fit = 0
    for i in range(len(population)):
        d[population[i]] = calcFitness(name,population[i])
        fit += calcFitness(name,population[i])

    # print d
    print max(d.iteritems(), key=operator.itemgetter(1))[0]
    time.sleep(0.1)
    # print fit/len(population)
    newPop = []
    # unique = set(val for dic in lis for val in dic.key())
    # for i in range(len(unique)):
    #     for j in range(int(((d.get(unique[i])/len(name))*popSize))):
    #         newPop.append(key)
    print "old len : " ,len(population)

    travelled = []
    # sortedDic = sorted(d.items(), key=operator.itemgetter(1))
    # for w in sorted(d, key=d.get, reverse=True):
    #     print w, d[w]
    # time.sleep(0.9)
    # for key, value in sorted(d.iteritems(), reverse=True):
    #     if key not in travelled:
    #         for j in range(int(((float(value)/len(name))*popSize))):
    #             newPop.append(key)
    #         travelled.append(key)

    #         if len(newPop) > popSize:
    #             break
    loc_count = 0
    for w in sorted(d, key=d.get, reverse=True):
        if w not in travelled:
            travelled.append(w)
            for j in range(int(((float(d[w])/len(name))*popSize))):
                newPop.append(w)
                loc_count += 1 # take count
                if len(newPop) >= popSize:
                    break
            else:
                continue
            break
            
    print "travelled : " , travelled
    # print "new:" ,newPop
    print "new len : " ,len(newPop)
    return newPop, fit
# calculating fitness
def calcFitness(word1, word2):
    fitness = 0
    for j in range(len(word1)):
        if word1[j] == word2[j]:
            fitness += 1
    if (fitness == len(word1)):
        print "################################### done #################################"
        print word2
        quit()
    return fitness

# generating offsprings
def mating(word1, word2):
    rndNum = random.randint(0,len(name))

    newWord2 = word1[:rndNum] + word2[rndNum:]
    newWord1 = word2[:rndNum] + word1[rndNum:]
    # print word1,word2, newWord1,newWord2
    return newWord1,newWord2

def pickRandom(population):
    rndNum = random.randint(0,len(population) -1)
    return population[rndNum]

def crossOver(population):
    newGeneration = []
    for i in range(0,len(population)/2):

        child1,child2 = mating(pickRandom(population),pickRandom(population))
        newGeneration.extend([child1,child2])
    return newGeneration

# mutation
def mutation(offspring):
    # mutation 1
    rndNum = random.randint(0,len(offspring)-1)
    offspring = offspring.replace(offspring[rndNum],random.choice(string.ascii_lowercase))

    # mutation 2
    # for i in range(len(offspring)):
    #     # print "in :" , offspring
    #     rndNum = random.randint(0,1)
    #     if (rndNum == 1):
    #         offspring = offspring.replace(offspring[i],random.choice(string.ascii_lowercase))
        # print "out :", offspring
    return offspring

def mutationRound(population):
    # print "in :" , population
    for i in range(0,len(population)):
        population[i] = mutation(population[i])
    # print "out :" , population
    return population
print population

score = 0
gen = 0
while (score <  5):
    gen += 1
    # print "len : " ,len(population)

    population , fit= selection(population)
    # print population
    population = crossOver(population)
    # print population

    population = mutationRound(population)

    print "gen : ", gen
    print "fit :" , fit
    # print population

    # print population

