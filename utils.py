import matplotlib.pyplot as plt
import os

def plot_q_learning_reward_training(mean_profits,output_dir="plots"):
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(mean_profits, label="Reward per Episode", color='blue', linewidth=1)
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.title(f"Q-Learning Reward Trend")
    plt.grid(True)
    plt.legend()

    plt.savefig(os.path.join(output_dir, "train.png"), bbox_inches="tight")
    plt.close()
