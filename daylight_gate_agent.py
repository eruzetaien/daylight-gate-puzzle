import numpy as np

class DaylightGateAgent(): # Tabular Q-Learning
    def __init__(self, state_size, action_size, step_size=0.5, discount_factor=0.9, epsilon=0.1, seed=42):
        self.rand_generator = np.random.RandomState(seed)

        self.state_size = state_size
        self.action_size = action_size
        self.step_size = step_size  # Learning rate
        self.discount_factor = discount_factor  # Discount factor
        self.epsilon = epsilon  # Exploration rate

        # Initialize Q-table to zero
        self.q_table = np.zeros((state_size, action_size))

    def policy(self, state, is_deterministic = False):
        if not is_deterministic and self.rand_generator.random() < self.epsilon:
            return self.rand_generator.randint(0, self.action_size)

        state_idx = self.state_to_index(state)
        state_q_values = self.q_table[state_idx, :]
        best_action = np.argmax(state_q_values)
        return int(best_action)

    def update(self, state, action, reward, next_state): # Sutton Pg. 131
        state_idx = self.state_to_index(state)
        next_state_idx = self.state_to_index(next_state)
        
        max_next_state_q_value = np.max(self.q_table[next_state_idx, :])
        td_target = reward + self.discount_factor * max_next_state_q_value
        self.q_table[state_idx, action] += self.step_size * (td_target - self.q_table[state_idx, action])

    def state_to_index(self, state):
        """Convert [0/1, 0/1, ..., 0/1] into integer"""
        return int("".join(map(str, state)), 2)

    def index_to_state(self, idx):
        """Convert integer to [nS]-element binary list."""
        return [int(x) for x in f"{idx:0{self.state_size}b}"]