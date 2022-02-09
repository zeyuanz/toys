from tensorforce.environments import Environment
from tensorforce.agents import Agent
from tensorforce.execution import Runner

class CustomEnvironment(Environment):
    def __init__(self):
        self.state = self.reset()
        super().__init__()

    def states(self):
        return dict(type='float', shape=(5,))

    def actions(self):
        return dict(type='int', num_values=2)

    def max_episode_timesteps(self):
        return super().max_episode_timesteps()

    def close(self):
        super().close()

    def reset(self):
        state = [1,0,0,0,0]
        self.state = state
        return state

    def execute(self, actions):
        def move_forward(states):
            pos = 0
            for i, s in enumerate(states):
                if s == 1:
                    pos = i
                    break
            if pos != 4:
                states[pos] = 0
                states[pos+1] = 1
            return states, pos

        def move_backward():
            return [1,0,0,0,0]

        reward = 0
        if actions == 0:
            next_state, pos = move_forward(self.state)
            self.state = next_state
            if pos == 4:
                reward = 10
            else:
                reward = 0
        elif actions == 1:
            reward = 2
            next_state = move_backward() 
            self.state = next_state
        terminal = False  # Always False if no "natural" terminal state
        return next_state, terminal, reward

environment = Environment.create(
    environment=CustomEnvironment, max_episode_timesteps=500
)

agent = Agent.create(
    agent='tensorforce', environment=environment, update=64,
    optimizer=dict(optimizer='adam', learning_rate=1e-3),
    objective='policy_gradient', reward_estimation=dict(horizon=20)
)

runner=Runner(agent=agent, environment=environment)
runner.run(num_episodes=100)
runner.run(num_episodes=10, evaluation=True)

'''
sum_rewards = 0.0
states = environment.reset()
internals = agent.initial_internals()
for i in range(100):
    actions, internals = agent.act(
        states=states, internals=internals,
        independent=True, deterministic=True
    )
    states, terminal, reward = environment.execute(actions=actions)
    sum_rewards += reward
    print("Iter: %d\tactions: %d\treward: %2.f" %(i+1, actions, sum_rewards), "states: ", states)
'''