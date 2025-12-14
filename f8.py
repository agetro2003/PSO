from pso import PSO
import math
import time
def fitness(position):
    time.sleep(0.001)
    sum = 0
    for x_i in position:
        abs_x = abs(x_i)
            
        sqrt_x = math.sqrt(abs_x)

        sin_x = math.sin(sqrt_x)

        term = -x_i*sin_x

        sum += term
    return sum
if __name__ == '__main__':
    start_time = time.time()
    n = 30
    min_bound = -500
    max_bound = 500

    num_particles = 50
    iter = 1000
    # Peso de la inercia
    w = 0.7
    # Peso de la mejor solucion de la particula
    local_weight = 1.5
    # Peso de la mejor solucion global
    global_weight = 1.5

    
    
    pso = PSO(n, min_bound, max_bound, num_particles, iter, w, local_weight, global_weight, fitness)
    best_position, best_value = pso.run()
    end_time = time.time()
    result_time = end_time - start_time
    print(best_position)
    print(best_value)
    print("Tiempo de ejecución: " + f"{result_time:.3f}" + " segundos")            