class SimpleReflexAgent:
    def __init__(self, rules):
        self.rules = rules  # rules: dict mapping percepts to actions

    def perceive(self, percept):
        return self.rules.get(percept, "No action")

# Example usage:
if __name__ == "__main__":
    # Define rules: if 'dirty', clean; if 'clean', do nothing
    rules = {
        "dirty": "clean",
        "clean": "do nothing"
    }
    agent = SimpleReflexAgent(rules)
    percepts = ["dirty", "clean", "unknown"]
    for p in percepts:
        action = agent.perceive(p)
        print(f"Percept: {p} -> Action: {action}")