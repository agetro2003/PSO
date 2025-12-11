from pso import PSO
import time

if __name__ == '__main__':
    start_time = time.time()
    n = 30
    min_bound = -100
    max_bound = 100

    num_particles = 30

    iter = 50000

    w = 0.5

    local_weight = 1

    global_weight = 1.5

    def fitnees(position):
        sum = 0
        for x_i in position:
            sum += x_i**2
        return sum
    
    pso = PSO(n, min_bound, max_bound, num_particles, iter, w, local_weight, global_weight, fitnees)
    best_position, best_value = pso.run()
    end_time = time.time()
    result_time = end_time - start_time
    print(best_position)
    print(best_value)
    print("Tiempo de ejecución: " + f"{result_time:.3f}" + " segundos")       