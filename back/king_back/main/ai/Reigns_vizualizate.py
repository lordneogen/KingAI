import tkinter as tk
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from keras.optimizers import Adam
from template import *

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=1000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                  nb_actions=actions, nb_steps_warmup=5, target_model_update=1e-2)
    return dqn

def init_env():
    env = StoryEnv_learn()
    env.reset()
    dqn = build_agent(model, actions)
    dqn.compile(optimizer=Adam(lr=1e-3), metrics=['mae'])

    scores = dqn.test(env, nb_episodes=100, visualize=False)
    print(np.mean(scores.history['episode_reward']))

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot([i for i in range(len(ages))], ages)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=7, column=0, columnspan=3)
    canvas.draw()
    data1=kings[0][0]
    data2=kings[0][1]
    data3=kings[0][2]
    res = tk.StringVar()
    result=""
    print(data1[0])
    for x in range(len(data2)):
        '''
        деньги|популярность|сила|земля
        '''
        r1="деньги:"+str(int(data2[x][0]*100))+" популярность:"+str(int(data2[x][1]*100))+" армия:"+str(int(data2[x][2]*100))+" земля:"+str(data2[x][3]*100)
        result=result+r1+"\n"
    a=open("king.txt","w")
    a.write(str(data1))
    print(result)
    a.close()


# Создание окна
root = tk.Tk()

# Создание ползунков и полей текста
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()
var6 = tk.StringVar()

button = tk.Button(root, text="График", command=init_env)

slider1 = tk.Scale(root, from_=0, to=100000, orient=tk.HORIZONTAL, variable=var1)
slider2 = tk.Scale(root, from_=0, to=100000, orient=tk.HORIZONTAL, variable=var2)
slider3 = tk.Scale(root, from_=0, to=100000, orient=tk.HORIZONTAL, variable=var3)
slider4 = tk.Scale(root, from_=0, to=100000, orient=tk.HORIZONTAL, variable=var4)

text1 = tk.Entry(root, textvariable=var1)
text2 = tk.Entry(root, textvariable=var2)
text3 = tk.Entry(root, textvariable=var3)
text4 = tk.Entry(root, textvariable=var4)
text5 = tk.Entry(root, textvariable=var5,width=120,font=20)
text6 = tk.Entry(root, textvariable=var6,width=120,font=20)
# Создание поля изображения
image_path = "card1.jpg"
image = Image.open(image_path)
image = image.resize((300, 300), Image.ANTIALIAS)
image_tk = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=image_tk)
image_label.image = image_tk

# Размещение элементов в окне с помощью grid
slider1.grid(row=0, column=0)
text1.grid(row=0, column=1)
slider2.grid(row=1, column=0)
text2.grid(row=1, column=1)
slider3.grid(row=2, column=0)
text3.grid(row=2, column=1)
slider4.grid(row=3, column=0)
text4.grid(row=3, column=1)
image_label.grid(row=0, column=2, rowspan=4)
button.grid(row=6,column=1)
# Создание графика


# Запуск главного цикла
root.mainloop()
