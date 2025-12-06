class DaylightGateEnv():
    LAMP_SWITCH_RULE = {
        0: [0, 2, 4],
        1: [0, 1, 4, 5],
        2: [1, 2, 4, 5],
        3: [1, 2, 3, 5],
        4: [3, 4, 5],
        5: [0, 1, 2, 4],
    }

    def __init__(self):
        self.goal_state = [
            0,0,
            0,0,
            0,0
        ]
        self.action_size = len(self.LAMP_SWITCH_RULE)
        self.state_size = 2 ** self.action_size
    
    def toggle(self, state, action):
        for lamp in self.LAMP_SWITCH_RULE[action]:
            state[lamp] ^= 1     # XOR flip
        return state

    def step(self, state, action):
        next_state = self.toggle(state, action) 
        
        if (next_state) == self.goal_state:
            reward = 20
            terminated = True
        else :
            reward = -1
            terminated = False
        
        return state, reward, terminated

    def reset(self):
        return 

    def get_action_size(self):
        return self.action_size
    
    def get_state_size(self):
        return self.state_size