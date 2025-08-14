class UtilityBasedAgent:
    def __init__(self, actions, utility_function):
        self.actions = actions
        self.utility_function = utility_function

    def perceive(self, environment_state):
        self.environment_state = environment_state

    def choose_action(self):
        best_action = None
        max_utility = float('-inf')
        for action in self.actions:
            utility = self.utility_function(self.environment_state, action)
            if utility > max_utility:
                max_utility = utility
                best_action = action
        return best_action

# Example usage:
def sample_utility_function(state, action):
    # Example: maximize value in state dict for the action key
    return state.get(action, 0)

actions = ['eat', 'sleep', 'work']
agent = UtilityBasedAgent(actions, sample_utility_function)

state = {'eat': 2, 'sleep': 5, 'work': 3}
agent.perceive(state)
chosen_action = agent.choose_action()
print(f"Chosen action: {chosen_action}")