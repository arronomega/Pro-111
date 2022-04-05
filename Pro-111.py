import pandas as pd 
import csv 
import random as rand
import statistics as st
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
df1 = pd.read_csv("medium_data.csv")
data = df1["claps"].tolist()
fig = ff.create_distplot([data],["claps"],show_hist=False)
mean = st.mean(data)
stdev = st.stdev(data)
mode = st.mode(data)
def random_set_of_data(counter):
    dataset =[]
    for i in range(0,counter):
        index = rand.randint(0,len(data)-1)
        value1 = data[index]
        dataset.append(value1)
        sp_mean = st.mean(dataset)
    return sp_mean
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_data(100)
    mean_list.append(set_of_means)
mean = st.mean(mean_list)
def random_set_of_data(counter):
    dataset =[]
    for i in range(0,counter):
        index = rand.randint(0,len(data)-1)
        value1 = data[index]
        dataset.append(value1)
    sp_mean = st.mean(dataset)
    return sp_mean
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_data(10)
        mean_list.append(set_of_means)
    mean = st.mean(mean_list)
    print("Mean of sampling distribution of Math score :-",mean )
    print("Mean of population distribution of Math score :-",pop_mean)
setup()
def standard_dev():
    mean_list =[]
    for i in range(0,1000):
        set_of_means = random_set_of_data(100)
        mean_list.append(set_of_means)
    std_deviation = st.stdev(mean_list)
    print("Standard deviation of sampling distribution:-",std_deviation)
standard_dev()
def show_fig(mean_list):
    df = mean_list
    mean = st.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode ="lines",name = "MEAN"))
    fig.show()





