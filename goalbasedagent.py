class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def perceive(self, environment):
        # Perceive the current state from the environment
        return environment.get_state()

    def is_goal_state(self, state):
        # Check if the current state matches the goal
        return state == self.goal

    def get_possible_actions(self, state):
        # Return a list of possible actions from the current state
        return ['action1', 'action2', 'action3']

    def choose_action(self, state):
        # Choose an action that brings the agent closer to the goal
        actions = self.get_possible_actions(state)
        # Dummy logic: just pick the first action
        return actions[0]

    def act(self, environment):
        state = self.perceive(environment)
        if self.is_goal_state(state):
            print("Goal achieved!")
            return
        action = self.choose_action(state)
        environment.apply_action(action)
        print(f"Performed action: {action}")

# Example usage with a dummy environment
class DummyEnvironment:
    def __init__(self):
        self.state = 0

    def get_state(self):
        return self.state

    def apply_action(self, action):
        self.state += 1

if __name__ == "__main__":
    goal = 3
    agent = GoalBasedAgent(goal)
    env = DummyEnvironment()
    while not agent.is_goal_state(env.get_state()):
        agent.act(env)
    print("goal achieved")