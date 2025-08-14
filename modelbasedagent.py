import random

class ModelBasedAgent:
    def __init__(self, states, actions):
        self.states = states
        self.actions = actions
        self.model = {}  # {(state, action): (next_state, reward)}
        self.value = {s: 0 for s in states}

    def update_model(self, state, action, next_state, reward):
        self.model[(state, action)] = (next_state, reward)

    def plan(self, iterations=10, gamma=0.9):
        for _ in range(iterations):
            for (state, action), (next_state, reward) in self.model.items():
                self.value[state] = max(
                    self.value[state],
                    reward + gamma * self.value.get(next_state, 0)
                )

    def select_action(self, state):
        best_action = None
        best_value = float('-inf')
        for action in self.actions:
            key = (state, action)
            if key in self.model:
                next_state, reward = self.model[key]
                value = reward + self.value.get(next_state, 0)
                if value > best_value:
                    best_value = value
                    best_action = action
        if best_action is None:
            return random.choice(self.actions)
        return best_action

# Example usage:
if __name__ == "__main__":
    states = ['A', 'B', 'C']
    actions = ['left', 'right']
    agent = ModelBasedAgent(states, actions)

    # Simulate experience
    agent.update_model('A', 'right', 'B', 1)
    agent.update_model('B', 'right', 'C', 2)
    agent.update_model('C', 'left', 'A', 0)

    agent.plan()
    print("Value function:", agent.value)
    print("Best action from A:", agent.select_action('A'))