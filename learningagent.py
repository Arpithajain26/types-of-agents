import random

class LearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.2):
        self.q_table = {}  # state -> action values
        self.actions = actions
        self.lr = learning_rate
        self.df = discount_factor
        self.er = exploration_rate

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        if random.random() < self.er:  # Explore
            return random.choice(self.actions)
        # Exploit (choose best)
        q_values = [self.get_q(state, a) for a in self.actions]
        max_q = max(q_values)
        best_actions = [a for a, q in zip(self.actions, q_values) if q == max_q]
        return random.choice(best_actions)

    def learn(self, state, action, reward, next_state):
        old_q = self.get_q(state, action)
        next_qs = [self.get_q(next_state, a) for a in self.actions]
        max_next_q = max(next_qs) if next_qs else 0.0
        new_q = old_q + self.lr * (reward + self.df * max_next_q - old_q)
        self.q_table[(state, action)] = new_q

if __name__ == "__main__":
    actions = ['left', 'right']
    agent = LearningAgent(actions)

    state = 0
    for episode in range(1, 21):  # Run 20 episodes
        action = agent.choose_action(state)
        reward = 1 if action == 'right' else 0
        next_state = state + 1 if action == 'right' else state - 1
        agent.learn(state, action, reward, next_state)
        state = next_state

        print(f"Episode {episode}: State={state}, Action={action}, Reward={reward}")
        print("Q-table:", agent.q_table)
        print("-" * 40)
