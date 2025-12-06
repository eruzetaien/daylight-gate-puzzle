import numpy as np
from daylight_gate_agent import DaylightGateAgent
from daylight_gate_env import DaylightGateEnv
from utils import plot_q_learning_reward_training
from tqdm import tqdm

def run_q_learning_experiment(
    episodes=500, episode_length=1000, seed=42
):
    env = DaylightGateEnv()
    agent = DaylightGateAgent(
        state_size=env.get_state_size(),
        action_size=env.get_action_size(),
        step_size=0.05,
        discount_factor=1,
        epsilon=0.1,
        seed=seed
    )

    all_episode_reward = []

    for _ in tqdm(range(episodes), desc="Episodes"):
        state = [
            1,1,
            1,1,
            1,1
        ] 
        total_reward = 0

        step = 0
        terminated = False
        while (step < episode_length and not terminated):
            action = agent.policy(state)
            next_state, reward, terminated = env.step(state,action)
            agent.update(state, action, reward, next_state)
            
            state = next_state
            total_reward += reward
            step += 1

        all_episode_reward.append(total_reward)

    return agent, all_episode_reward

def simulate_next_move(current_state, agent):
    env = DaylightGateEnv()
    state=current_state
    terminated = False
    actions = []
    while (not terminated):
        action = agent.policy(state, is_deterministic = True)
        actions.append(action)
        next_state, _, terminated = env.step(state,action)
        state = next_state
    print()
    print(" -> ".join(str(a) for a in actions))

def main():    
    agent, all_rewards = run_q_learning_experiment()
    plot_q_learning_reward_training(all_rewards)
    simulate_next_move([1,1,1,1,1,1],agent)
    

if __name__ == "__main__":
    main()

