from manim import *
import colour as clr
import networkx as nx 
import numpy 
import scipy 
class Net:
    def __init__(self,Adj,n,k,dt,var,mean):
        self.Adj = Adj#Adjacency with weighted and dircetional couplings
        self.n = n
        self.dt = dt
        self.k = float(k)
        self.nat_hist = []
        self.noise_A = 0.1
        self.space = [] #3 dimensional vectors in node based vector. 
        # NEEDS GENERATOR
        self.state = 0 + self.noise_A*np.random.randn(self.n,1) #  np.random.uniform(-2*np.pi,2*np.pi,(n,1))  # nx1 vector of current oscillator  states
        self.state_init = self.state
        #print('init state = {}'.format(self.state))
        self.nats = np.zeros((n,1)) + self.noise_A*0.01*np.random.randn(self.n,1) # 2*np.pi*dt*np.random.normal(mean,var,(n,1)) # Vector of natural freqs, currently all unity for simplicity. 
        self.state_nats = self.nats 
        #print('init nats = {}'.format(self.nats))
        self.I = np.zeros((n,1))
        self.Iw = np.zeros((n,1))
        self.graph = nx.from_numpy_array(self.Adj)
        self.pos = nx.kamada_kawai_layout(self.graph)
        self.nat_hist = self.nats
def colourfunc(val):
    
    RGB = clr.HSV_to_RGB([val,1,1])
    return RGB

N = 14
k = 1
connectivity = 1
var,mean = 0.7, 0

Qnat = True
Qup = False

T = 100
res = 10000
time = np.linspace(0,T,res)
dt = T/res
results = np.zeros((res,N))
evo_adj = np.zeros((N,N,res))
graph_nx = nx.erdos_renyi_graph(n=N, p=connectivity) # p=1 -> all-to-all connectivity
graph = nx.to_numpy_array(graph_nx)*k




testnet = Net(graph,N,k,dt,var,mean)
coords = np.zeros((3,N))
print(np.shape(coords))
for i in range(N):
    coords[0][i] = testnet.pos[i][0]*5
    coords[1][i] = testnet.pos[i][1]*5
print(np.shape(coords))
print([coords[0,1],coords[1,1],coords[2,1]])   

class test4(Scene):
    def construct(self):
        angle = ValueTracker(0.2)
    
        dots = [always_redraw(lambda:Dot([coords[0,i],coords[1,i],coords[2,i]],color=rgb_to_color(colourfunc(angle.get_value())))) for i in range(N)]
        
        #
       # red_dot = always_redraw(lambda: Dot(color=colourfunc(angle.get_value())).move_to(0,0))
        
       # self.play(FadeIn(written))
       
    
        # self.play(FadeIn(red_dot))
        self.play(FadeIn(*dots))
        self.wait(2)
        self.play(angle.animate.set_value(2), run_time=2)
        self.wait(2)
        # self.play(angle.animate.set_value(2), run_time=2)
       

