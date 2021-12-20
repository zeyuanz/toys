import numpy as np
import time

#define global variables
state_size = 5 # 5 positions
action_size = 2 # forward and backward
eta = 0.1 # learning rate
discount = 0.95 # discount factor
q_table = np.zeros((state_size, action_size))  # q table.shape = (5,2)

def select_action(q_table: np.ndarray, curr_pos: int, randomness: float) -> int:
    ''' select proper action based on q_table and curr_pos
    args:
        q_table <np.ndarray>: the current values of q.
        curr_pos <int>: current position, should be [0, 4].
        randomness <float>: randomness of action choice.  
    returns:
        action <int>: 0 means forward, 1 means backward.
    '''
    q_forward = q_table[curr_pos, 0]
    q_backward = q_table[curr_pos, 1]
    prob_forward = 1.0
    if q_forward > q_backward:
        prob_forward = 1.0 - randomness / 2.0
    else:
        prob_forward = randomness / 2.0
    
    action = np.random.binomial(n=1, p=1-prob_forward)
    return action

def go_next_pos(curr_pos: int, action: int)->int:
    '''
    args:
        curr_pos <int>: current position
        action <int>: action, forward of backward
    return:
        next_pos <int>: next position
    '''
    next_pos = 0
    if action == 0:
        if curr_pos != 4:
            next_pos = curr_pos+1
        else:
            next_pos = curr_pos
    return next_pos

def update_qTable_pos(q_table: np.ndarray, curr_pos: int, action: int) -> int:
    ''' update q_table and position based on current q_table, position and action
        formula is the q-leanrning formula
    args:
        q_table <np.ndarray>: the current values of q.
        curr_pos <int>: current position, should be [0, 4].
        action <int>: action to take, 0 means forward, 1 means backward.
    returns:
        q_table <np.ndarray>: the updated values of q.
        curr_pos <int>: the updated position, should be [0, 4].
    '''
    curr_q = q_table[curr_pos, action]
    reward = 0
    next_forward_pos = curr_pos

    if action == 1:
        reward = 2
    elif action == 0 and (curr_pos == 3 or curr_pos == 4):
        reward = 10

    if curr_pos != 4:
        next_forward_pos += 1

    next_pos = go_next_pos(curr_pos, action) 
    next_q = max(q_table[next_forward_pos, 0], q_table[0, 1])
    curr_q = curr_q + eta * (reward + discount * next_q - curr_q)
    q_table[curr_pos, action] = curr_q
    return next_pos

def train(q_table: np.ndarray, n_iter: int)->None:
    ''' train with q-learning
    args:
        q_table <np.ndarray>: the current values of q.
        n_iter <int>: number of iterations
    return:
        q_table <np.ndarray>: final q table
    '''
    curr_pos = 0
    action  = 0
    beta = 0.9999
    for i in range(n_iter):
        randomness = beta ** float(i+1)
        action = select_action(q_table, curr_pos, randomness)
        curr_pos = update_qTable_pos(q_table, curr_pos, action)

def get_optimal_route(q_table: np.ndarray, n_step: int) -> list:
    ''' print the optimal route
    args:
        q_table <np.ndarray>: the current values of q.
        n_step <int>: number of steps in route
    return:
        route <list>: list of routes
    '''
    route = [None] * (n_step+1)
    curr_pos = 0
    route[curr_pos] = 0
    for i in range(n_step):
        next_foward = go_next_pos(curr_pos, 0)
        next_forward_q = q_table[next_foward, 0]
        next_backward_q = q_table[curr_pos, 1]
        if next_forward_q > next_backward_q:
            next_pos = next_foward
        else:
            next_pos = 0
        route[i+1] = next_pos
        curr_pos = next_pos
    return route

def main():
    start = time.time()
    train(q_table, 1000000)
    end = time.time()
    print(q_table.T)
    print("Time: %.4fs" %(end-start))
    print(get_optimal_route(q_table, 20))

if __name__ == '__main__':
    main()
