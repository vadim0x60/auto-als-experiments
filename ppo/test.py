from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

import gym
import auto_als

model = PPO.load('model/rl_model_5000_steps.zip')
env = gym.make('Auto-ALS-v0', attach=False)

evaluate_policy(model, env)