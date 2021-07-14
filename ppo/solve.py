from subprocess import call
import click

from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import CheckpointCallback

import gym
from auto_als import UnityException, UnityGymException

def solve():
    try:
        env = gym.make('Auto-ALS-v0', attach=False)
        
        try:
            model = PPO.load('model')
        except IOError:
            model = PPO('MlpPolicy', env, verbose=True)
            
        model.learn(10000, callback=CheckpointCallback(1000, 'model'))
        evaluate_policy(model, env)
    except (UnityException, UnityGymException):
        solve()

if __name__ == '__main__':
    solve()