#Elias Matos e Morgana Weber

def random_generator(x0, a, c, M, size):
    values = [0] * size
    values[0] = x0
    i = 1
    while i < size:
        values[i] = (a * values[i - 1] + c) % M
        i += 1
    values.pop(0)
    return values

RANDOM_NUMBERS_AMOUNT = 1000
QUEUE = [] 
SCHEDULER = []
TIME = 1
RANDOM_NUMBERS = random_generator(1, 1.3, 0.2, 1, RANDOM_NUMBERS_AMOUNT)
#RANDOM_NUMBERS = [0.2,0.7,0.1,0.9,0.3,0.4,0.6,0.5]
START_ARRIVE = 1
END_ARRIVE = 2
START_EXIT = 3
END_EXIT = 4

def single_queue_simulator(c, k):
    global SCHEDULER
    global TIME
    QUEUE.append([TIME,0])
    individual_time = (END_EXIT-START_EXIT) * RANDOM_NUMBERS.pop(0) +  START_EXIT
    SCHEDULER.append([TIME+individual_time, individual_time, 1]) 
    #print("tabela 1: ", QUEUE)
    #print("tabela 2: ", SCHEDULER)

    arrival(k,c)

def arrival(k,c):
    global RANDOM_NUMBERS_AMOUNT
    global TIME 
    global SCHEDULER 
    global RANDOM_NUMBERS
    global QUEUE
    global START_ARRIVE
    global END_ARRIVE
    
    if len(RANDOM_NUMBERS) == 0: exit()

    individual_time = (END_ARRIVE-START_ARRIVE) * RANDOM_NUMBERS.pop(0) +  START_ARRIVE
    TIME += individual_time
    SCHEDULER.append([TIME, individual_time, 0])

    SCHEDULER.sort(key = lambda x: x[0])

    #print("tabela 1: ", QUEUE)
    #print("tabela 2: ", SCHEDULER)
    
    if len(QUEUE) < k:
        QUEUE.append(SCHEDULER.pop(0))
        if len(QUEUE) <= c:
            exit_queue(c)
        
        if len(SCHEDULER) > c:
            if SCHEDULER[0][2] == 1:
                TIME = SCHEDULER[0][0]
                QUEUE.pop(0)
                SCHEDULER.pop(0)
                
    arrival(k,c)

def exit_queue(c):
    global RANDOM_NUMBERS_AMOUNT
    global TIME
    global RANDOM_NUMBERS
    global QUEUE
    global START_EXIT
    global END_EXIT

    if len(RANDOM_NUMBERS) == 0: exit()
    individual_time = (END_EXIT-START_EXIT) * RANDOM_NUMBERS.pop(0) +  START_EXIT
    SCHEDULER.append([TIME, individual_time, 1])

single_queue_simulator(2, 4)
