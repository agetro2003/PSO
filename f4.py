from parallel_pso import PSO
import time
def fitness(position): 
    absolute_values = [abs(x_i) for x_i in position]
    return max(absolute_values)
    
if __name__ == '__main__':
    start_time = time.time()
    n = 30
    min_bound = -100
    max_bound = 100

    num_particles = 50

    iter = 1000

    w = 0.7

    local_weight = 1.5

    global_weight = 1.5



    pso = PSO(n, min_bound, max_bound, num_particles, iter, w, local_weight, global_weight, fitness)
    best_position, best_value = pso.run()
    end_time = time.time()
    result_time = end_time - start_time
    print(best_position)
    print(best_value)
    print("Tiempo de ejecución: " + f"{result_time:.3f}" + " segundos")