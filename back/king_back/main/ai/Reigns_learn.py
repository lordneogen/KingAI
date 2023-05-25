import math
import random
import tensorflow as tf
import numpy as np
import random
from gym import Env
from gym.spaces import Discrete, Box

from rl.agents.dqn import DQNAgent
from rl.core import Env
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Flatten
from situations_train import situations

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class StoryEnv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = Discrete(2)
        # Temperature array
        self.observation_space = Box(low=0, high=100, shape=(1,12))

        self.dif1=100000
        self.dif2 = 1000
        self.dif3 = 1000
        self.dif4 = 1000

        '''
        деньги|популярность|сила|земля
        '''
        self.state = np.array([0.5, 0.5, 0.5,0.5,0.5, 0.5, 0.5,0.5,0.5, 0.5, 0.5,0.5])
        # Set shower length
        self.age = 0

    def step(self, action):


        if action==0:
            self.state[0] = max(self.state[4], 0.0)
            self.state[1] = max(self.state[5], 0.0)
            self.state[2] = max(self.state[6], 0.0)
            self.state[3] = max(self.state[7], 0.0)
            self.state[0] = min(self.state[4], 1.0)
            self.state[1] = min(self.state[5] ,1.0)
            self.state[2] = min(self.state[6] , 1.0)
            self.state[3] = min(self.state[7] , 1.0)
        else:
            self.state[0] = max(self.state[8], 0.0)
            self.state[1] = max(self.state[9], 0.0)
            self.state[2] = max(self.state[10], 0.0)
            self.state[3] = max(self.state[11], 0.0)
            self.state[0] = min(self.state[8], 1.0)
            self.state[1] = min(self.state[9] ,1.0)
            self.state[2] = min(self.state[10] , 1.0)
            self.state[3] = min(self.state[11] , 1.0)
        x=random.choice(situations)
        x1=random.choice(situations)
        while x!=x1:
            x1 = random.choice(situations)
        self.state[4] = min(self.state[0] + x['option_effect']['money'] / self.dif1, 1.0)
        self.state[5] = min(self.state[1] + x['option_effect']['popularity'] / self.dif2, 1.0)
        self.state[6] = min(self.state[2] + x['option_effect']['army'] / self.dif3, 1.0)
        self.state[7] = min(self.state[3] + x['option_effect']['land'] / self.dif4, 1.0)
        self.state[8] = min(self.state[0] + x1['option_effect']['money'] / self.dif1, 1.0)
        self.state[9] = min(self.state[1] + x1['option_effect']['popularity'] / self.dif2, 1.0)
        self.state[10] = min(self.state[2] + x1['option_effect']['army'] / self.dif3, 1.0)
        self.state[11] = min(self.state[3] + x1['option_effect']['land'] / self.dif4, 1.0)
        self.state[4] = max(self.state[4], 0.0)
        self.state[5] = max(self.state[5], 0.0)
        self.state[6] = max(self.state[6], 0.0)
        self.state[7] = max(self.state[7], 0.0)
        self.state[8] = max(self.state[8], 0.0)
        self.state[9] = max(self.state[9], 0.0)
        self.state[10] = max(self.state[10], 0.0)
        self.state[11] = max(self.state[11], 0.0)
        # for x in situations:
        #     if action==x['id']:
        #         self.state[0]=max(self.state[0],0.0)
        #         self.state[1] = max(self.state[1], 0.0)
        #         self.state[2] = max(self.state[2], 0.0)
        #         self.state[3] = max(self.state[3], 0.0)
        #         self.state[0]=min(self.state[0]+x['option_effect']['money']/10000,1.0)
        #         self.state[1] = min(self.state[1] + x['option_effect']['popularity'] / 100,1.0)
        #         self.state[2] = min(self.state[2] + x['option_effect']['army'] / 100,1.0)
        #         self.state[3] = min(self.state[3] + x['option_effect']['land'] / 100,1.0)


        observation_space_array = self.observation_space.sample()
        self.age += 1
        reward=0

        # print(self.state)
        if self.state[0]>=0.5 and  self.state[1]>=0.5 and self.state[2]>=0.5 and self.state[2]>=0.5:
            reward=1
            if self.age >= 90:
                reward = 10
            # print(action, self.state[0])
        else:
            reward=-1

        reward = reward + self.age ** 2


        if self.age >= 100 or( self.state[0]<=0 or self.state[1]<=0 or self.state[2]<=0 or self.state[3]<=0 ):
            print("\nstate:",self.state,"final-obs:",self.observation_space.sample()[-1],"age:",self.age)
            done = True
        else:
            done = False

        info = {}

        return self.state, reward, done, info

    def render(self):
        pass

    def reset(self):
        self.state = np.array([0.5, 0.5, 0.5,0.5,0.5, 0.5, 0.5,0.5,0.5, 0.5, 0.5,0.5])
        self.age = 0
        return self.state

env = StoryEnv()

episodes = 10
for episode in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        action = env.action_space.sample()
        print(env.action_space)
        n_state, reward, done, info = env.step(action)
        score += reward
    print('Episode:{} Score:{}'.format(episode, score))
del env


env = StoryEnv()

states = env.observation_space.shape
actions = env.action_space.n
from tensorflow import keras
def build_model(states, actions):
    model = keras.Sequential([
    keras.layers.Dense(24, activation='relu', input_shape=states),
    keras.layers.Dense(24, activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(actions, activation='linear')
    ])
    return model

model = build_model(states, actions)

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=10000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                  nb_actions=actions, nb_steps_warmup=5, target_model_update=1e-2)
    return dqn

dqn = build_agent(model, actions)


from keras.optimizers import Adam

dqn.compile(optimizer=Adam(lr=1e-3), metrics=['mae'])
dqn.fit(env, nb_steps=10000, visualize=False, verbose=1)

dqn.model.save('model.h5')

scores = dqn.test(env, nb_episodes=10, visualize=False)
print(np.mean(scores.history['episode_reward']))
