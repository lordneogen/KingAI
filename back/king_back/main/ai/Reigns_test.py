import torch
import gym
from gym import spaces
import numpy as np
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import BoltzmannQPolicy
from keras.optimizers import Adam
import template
from situations_test import situations


def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=1000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                  nb_actions=actions, nb_steps_warmup=5, target_model_update=1e-2)
    return dqn


env=template.StoryEnv_learn()

dqn=build_agent(template.model,template.actions)
dqn.compile(optimizer=Adam(lr=1e-3), metrics=['mae'])

scores = dqn.test(env, nb_episodes=10, visualize=False)
print(np.mean(scores.history['episode_reward']))