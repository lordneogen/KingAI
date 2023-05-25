import math
import random
import tensorflow as tf
import numpy as np
import random
import statistics
from gym import Env
from gym.spaces import Discrete, Box
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from rl.agents.dqn import DQNAgent
from rl.core import Env
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Flatten
from ..view_card import LIST_Cards,CARDS_LEARN,CARDS_TEST
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
kings=[]
choices=[]
data=[]
no=[]
class StoryEnv_learn(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = Discrete(2)
        # Temperature array
        self.observation_space = Box(low=0, high=100, shape=(1,12))
        self.cor1={}
        self.cor2={}
        self.cor2["name"]="Начало"
        self.cor2["title"]=""
        self.cor1["name"]="Начало"
        self.cor1["title"]=""
        self.dif1=100000
        self.dif2 = 1000
        self.dif3 = 1000
        self.dif4 = 1000
        self.ages=[]
        self.res=[]
        self.id=0
        '''
        деньги|популярность|сила|земля
        '''
        self.state = np.array([0.5, 0.5, 0.5,0.5,0.5, 0.5, 0.5,0.5,0.5, 0.5, 0.5,0.5])
        # Set shower length
        self.age = 0

    def step(self, action):

        situations=return_all_card()
        if action==0:
            self.state[0] = max(self.state[4], 0.0)
            self.state[1] = max(self.state[5], 0.0)
            self.state[2] = max(self.state[6], 0.0)
            self.state[3] = max(self.state[7], 0.0)
            self.state[0] = min(self.state[4], 1.0)
            self.state[1] = min(self.state[5] ,1.0)
            self.state[2] = min(self.state[6] , 1.0)
            self.state[3] = min(self.state[7] , 1.0)

            self.res.append(
                "id:{},Выбор пал на {} а не на {},  Деньги: {} ,Популярность: {},Армия: {},Земля: {},Возраст:{}\n".format(self.id,self.cor1["name"]+" "+self.cor1["title"],self.cor2["name"]+" "+self.cor2["title"],int(self.state[0] * 100),int(self.state[1] * 100),int(self.state[2] * 100),int(self.state[3] * 100),self.age))

            if self.age>0:
                choices.append(self.cor1)
                no.append(self.cor2)
        else:
            self.state[0] = max(self.state[8], 0.0)
            self.state[1] = max(self.state[9], 0.0)
            self.state[2] = max(self.state[10], 0.0)
            self.state[3] = max(self.state[11], 0.0)
            self.state[0] = min(self.state[8], 1.0)
            self.state[1] = min(self.state[9] ,1.0)
            self.state[2] = min(self.state[10] , 1.0)
            self.state[3] = min(self.state[11] , 1.0)
            if self.age > 0:
                choices.append(self.cor2)
                no.append(self.cor1)
            self.res.append(
                "id:{},Выбор пал на {} а не на {},  Деньги: {} ,Популярность: {},Армия: {},Земля: {},Возраст:{}\n".format(self.id,
                                                                                                                          self.cor2["name"]+" "+self.cor2["title"],self.cor1["name"]+" "+self.cor1["title"],int(self.state[0] * 100),int(self.state[1] * 100),int(self.state[2] * 100),int(self.state[3] * 100),self.age))


        data.append([self.state[0],self.state[1],self.state[2],self.state[3]])
        x=random.choice(situations)
        self.cor1=x
        x1=random.choice(situations)
        while x==x1:
            x1 = random.choice(situations)
        self.cor2=x1
        self.state[4] = min(self.state[0] + x['money'] / self.dif1, 1.0)
        self.state[5] = min(self.state[1] + x['popularity'] / self.dif2, 1.0)
        self.state[6] = min(self.state[2] + x['army'] / self.dif3, 1.0)
        self.state[7] = min(self.state[3] + x['land'] / self.dif4, 1.0)
        self.state[8] = min(self.state[0] + x1['money'] / self.dif1, 1.0)
        self.state[9] = min(self.state[1] + x1['popularity'] / self.dif2, 1.0)
        self.state[10] = min(self.state[2] + x1['army'] / self.dif3, 1.0)
        self.state[11] = min(self.state[3] + x1['land'] / self.dif4, 1.0)
        self.state[4] = max(self.state[4], 0.0)
        self.state[5] = max(self.state[5], 0.0)
        self.state[6] = max(self.state[6], 0.0)
        self.state[7] = max(self.state[7], 0.0)
        self.state[8] = max(self.state[8], 0.0)
        self.state[9] = max(self.state[9], 0.0)
        self.state[10] = max(self.state[10], 0.0)
        self.state[11] = max(self.state[11], 0.0)


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

            # print("\nstate:",self.state,"final-obs:",self.observation_space.sample()[-1],"age:",self.age)
            done = True
            kings.append([choices,data,no])
            self.ages.append(self.age)
            self.id+=1
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

class StoryEnv_test(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = Discrete(2)
        # Temperature array
        self.observation_space = Box(low=0, high=100, shape=(1,12))
        self.cor1={}
        self.cor2={}
        self.cor2["name"]="Начало"
        self.cor2["title"]=""
        self.cor1["name"]="Начало"
        self.cor1["title"]=""
        self.dif1=100000
        self.dif2 = 1000
        self.dif3 = 1000
        self.dif4 = 1000
        self.ages=[]
        self.res=[]
        self.id=0
        '''
        деньги|популярность|сила|земля
        '''
        self.state = np.array([0.5, 0.5, 0.5,0.5,0.5, 0.5, 0.5,0.5,0.5, 0.5, 0.5,0.5])
        # Set shower length
        self.age = 0

    def step(self, action):

        situations=return_all_card()
        if action==0:
            self.state[0] = max(self.state[4], 0.0)
            self.state[1] = max(self.state[5], 0.0)
            self.state[2] = max(self.state[6], 0.0)
            self.state[3] = max(self.state[7], 0.0)
            self.state[0] = min(self.state[4], 1.0)
            self.state[1] = min(self.state[5] ,1.0)
            self.state[2] = min(self.state[6] , 1.0)
            self.state[3] = min(self.state[7] , 1.0)

            self.res.append([self.id,self.cor1["name"]+"-"+self.cor1["title"],self.cor2["name"]+"-"+self.cor2["title"],int(self.state[0] * 100),int(self.state[1] * 100),int(self.state[2] * 100),int(self.state[3] * 100),self.age])

            if self.age>0:
                choices.append(self.cor1)
                no.append(self.cor2)
        else:
            self.state[0] = max(self.state[8], 0.0)
            self.state[1] = max(self.state[9], 0.0)
            self.state[2] = max(self.state[10], 0.0)
            self.state[3] = max(self.state[11], 0.0)
            self.state[0] = min(self.state[8], 1.0)
            self.state[1] = min(self.state[9] ,1.0)
            self.state[2] = min(self.state[10] , 1.0)
            self.state[3] = min(self.state[11] , 1.0)
            if self.age > 0:
                choices.append(self.cor2)
                no.append(self.cor1)
            self.res.append([self.id, self.cor2["name"] + "-" + self.cor2["title"],
                                 self.cor1["name"] + "-" + self.cor1["title"], int(self.state[0] * 100),
                                 int(self.state[1] * 100), int(self.state[2] * 100), int(self.state[3] * 100),
                                 self.age])

        data.append([self.state[0],self.state[1],self.state[2],self.state[3]])
        x=random.choice(situations)
        self.cor1=x
        x1=random.choice(situations)
        while x==x1:
            x1 = random.choice(situations)
        self.cor2=x1
        self.state[4] = min(self.state[0] + x['money'] / self.dif1, 1.0)
        self.state[5] = min(self.state[1] + x['popularity'] / self.dif2, 1.0)
        self.state[6] = min(self.state[2] + x['army'] / self.dif3, 1.0)
        self.state[7] = min(self.state[3] + x['land'] / self.dif4, 1.0)
        self.state[8] = min(self.state[0] + x1['money'] / self.dif1, 1.0)
        self.state[9] = min(self.state[1] + x1['popularity'] / self.dif2, 1.0)
        self.state[10] = min(self.state[2] + x1['army'] / self.dif3, 1.0)
        self.state[11] = min(self.state[3] + x1['land'] / self.dif4, 1.0)
        self.state[4] = max(self.state[4], 0.0)
        self.state[5] = max(self.state[5], 0.0)
        self.state[6] = max(self.state[6], 0.0)
        self.state[7] = max(self.state[7], 0.0)
        self.state[8] = max(self.state[8], 0.0)
        self.state[9] = max(self.state[9], 0.0)
        self.state[10] = max(self.state[10], 0.0)
        self.state[11] = max(self.state[11], 0.0)


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

            # print("\nstate:",self.state,"final-obs:",self.observation_space.sample()[-1],"age:",self.age)
            done = True
            kings.append([choices,data,no])
            self.ages.append(self.age)
            self.id+=1
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


def return_all_card():
    return CARDS_LEARN()

def return_filter_card():
    return CARDS_TEST()

from tensorflow import keras


def build_model(states, actions):
    model = keras.Sequential([
    keras.layers.Dense(256, activation='relu', input_shape=states),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(actions, activation='linear')
    ])
    return model


def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=10000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                  nb_actions=actions, nb_steps_warmup=5, target_model_update=1e-2)
    return dqn


# {id: 1, name: 'Имя', title: 'Бла-Бла', money: 1000, popularity: 0, army: 0, land: -10},

def smooth_data(data, window_size):
    # Создание массива с окнами данных
    window = np.ones(window_size) / window_size
    # Применение скользящего среднего
    smoothed_data = np.convolve(data, window, mode='same').tolist()
    return smoothed_data

def create_model(staps,def_money,def_popularity,def_army,def_land,id):
    kings = []
    choices = []
    data = []
    no = []
    env = StoryEnv_learn()

    env.dif1=def_money
    env.dif2=def_popularity
    env.dif3=def_army
    env.dif4=def_land

    states = env.observation_space.shape
    actions = env.action_space.n

    model = build_model(states, actions)
    dqn = build_agent(model, actions)

    from keras.optimizers import Adam

    dqn.compile(optimizer=Adam(lr=1e-3), metrics=['mae'])
    dqn.fit(env, nb_steps=staps, visualize=False, verbose=1)

    name='model'+str(id)+'.h5'

    dqn.model.save(name)

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot([i for i in range(len(env.ages))], env.ages)

    pt="pic{}.png".format(id)
    fig.savefig("E:\pythonProject3\king_back\main\pic\pic{}.png".format(id))


    env.ages=smooth_data(env.ages,int(staps/10))

    return [statistics.mean(env.ages)/100,pt,''.join(env.res),env.ages,[i for i in range(len(env.ages))]]


def set_model(staps,def_money,def_popularity,def_army,def_land,id):
    kings = []
    choices = []
    data = []
    no = []
    env = StoryEnv_test()

    env.dif1=def_money
    env.dif2=def_popularity
    env.dif3=def_army
    env.dif4=def_land

    states = env.observation_space.shape
    actions = env.action_space.n

    model = build_model(states, actions)
    dqn = build_agent(model, actions)

    from keras.optimizers import Adam

    dqn.compile(optimizer=Adam(lr=1e-3), metrics=['mae'])

    print(type(id.id))
    name='E:\pythonProject3\king_back\model'+str(id.id)+'.h5'
    dqn.model.load_weights(name)
    dqn.test(env, nb_episodes=staps, visualize=False)

    # env = template.StoryEnv()
    #
    # dqn = build_agent(template.model, template.actions)
    # dqn.compile(optimizer=Adam(lr=1e-3), metrics=['mae'])
    #
    # scores = dqn.test(env, nb_episodes=10, visualize=False)
    # print(np.mean(scores.history['episode_reward']))


    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot([i for i in range(len(env.ages))], env.ages)

    pt="pic{}.png".format(id)
    fig.savefig("E:\pythonProject3\king_back\main\pic\pic{}.png".format(id))
    return [statistics.mean(env.ages)/100,pt,env.res,env.ages,[i for i in range(len(env.ages))]]