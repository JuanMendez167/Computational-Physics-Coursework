import numpy as np
import matplotlib.animation as ani
import matplotlib.pyplot as plt

class person():
    
    def __init__(self, box, sick, velocity):
        self.rng = np.random.default_rng()
        self.box = box
        #sick = 0 means healthy, sick>0 counts the sick days
        self.sick = sick
        self.immune = False
        self.velocity = velocity *  self.rng.uniform(-1,1,size=2)
        self.pos = self.rng.random(size=2)
        
    def move(self, dt):
        self.pos += self.velocity * dt
        for direction in range(2):
            if self.pos[direction] < 0 \
                or self.pos[direction] > box[direction]:
                self.velocity[direction] = -self.velocity[direction]
        if self.sick > 0:
            self.sick += 1
                
    def get_sick(self, pop_sick, safe_radius):
        for person in pop_sick:
            if abs(self.pos[0]-person.pos[0]) < safe_radius \
                and abs(self.pos[1]-person.pos[1]) < safe_radius :
                self.sick = 1
                    
    def get_immune(self,time):
        if self.sick > sick_time:
            self.immune = True
    
dt=0.02
box=np.array([1,1])
velocity=1.
nhealthy=200
nsick=1
safe_radius=0.006
sick_time=300

pop_healthy=[ person(box,0,velocity) for i in range(nhealthy) ]
pop_sick=[ person(box,1,velocity) for i in range(nsick)]
pop_immune=[]
pop_healthy = np.array(pop_healthy) 
pop_sick = np.array(pop_sick)
pop_immune = np.array(pop_immune)

fig, axes = plt.subplots(2, figsize=(4, 10))
axes[0].set_xlim(0, box[0])
axes[0].set_ylim(0, box[1])
axes[1].set_xlim(0,3000*dt)
axes[1].set_ylim(0,len(pop_healthy)*1.1)


a,=axes[0].plot([],[],'ko')
b,=axes[0].plot([],[],'ro')
c,=axes[0].plot([],[],'go')
pa,=axes[1].plot([],[],'k-')
pb,=axes[1].plot([],[],'r-')
pc,=axes[1].plot([],[],'g-')

time=[0]
traj_healthy = [nhealthy]
traj_sick = [1]
traj_immune = [0]

def animate(i):
    global pop_sick
    global pop_healthy
    global pop_immune
    
    #advance time
    time.append(time[-1]+dt)
    for person in pop_healthy:
        person.get_sick(pop_sick,safe_radius)
        person.move(dt)
        
    for person in pop_sick:
        person.get_immune(sick_time)
        person.move(dt)
        
    for person in pop_immune:
        person.move(dt)
            
    #update each population
    idx = np.array([pop_healthy[i].sick  for i in range(len(pop_healthy))]) == 0
    pop_healthynew = pop_healthy[idx]
    pop_sicknew =  pop_healthy[ np.invert(idx) ]
    pop_healthy = pop_healthynew
    pop_sick = np.append( pop_sick, pop_sicknew)
    
    idx = np.array([pop_sick[i].immune  for i in range(len(pop_sick))]) == False
    pop_sicknew = pop_sick[idx]
    pop_immunenew = pop_sick[ np.invert(idx)]
    pop_sick = pop_sicknew
    pop_immune = np.append( pop_immune, pop_immunenew)

    #plotting
    traj_healthy.append(len(pop_healthy))
    traj_sick.append(len(pop_sick))
    traj_immune.append(len(pop_immune))

    #plotting
    a.set_data([person.pos[0] for person in pop_healthy],[person.pos[1] for person in pop_healthy])
    b.set_data([person.pos[0] for person in pop_sick],[person.pos[1] for person in pop_sick])
    c.set_data([person.pos[0] for person in pop_immune],[person.pos[1] for person in pop_immune])
    pa.set_data( time, traj_healthy )
    pb.set_data( time, traj_sick )
    pc.set_data( time, traj_immune )

    return a,b,c,pa, pb,pc

anim = ani.FuncAnimation(fig, animate, frames=1000, interval=1, blit=True)
