import numpy as np
import matplotlib.pyplot as plt

#%%

cases_data = np.genfromtxt("sources/cases_comparation.csv", delimiter = ',', skip_header = 1)[:, 1:] / 1000000
cases = ['GEMASOLAR', 'Base Case', 'Evaporative Cooling', 'Dry Cooling', 'Once Through Cooling',
         'MED Cooling']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Agu', 'Sep', 'Oct', 'Nov', 'Dec']
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 2),  # 2 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize= 16)
        
    
#%%
def autolabel_2(rects,bar_label):
    for idx,rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
                bar_label[idx],
                ha='center', va='bottom', rotation=0,fontsize=16)


#%%
width = 0.5

Gross   = [127.18, 127.18, 120.79, 132.56, 103.81]
Net    = [127.18 - 1.5, 127.18 - 5, 120.79 - 3.81, 132.56 - 4.3, 103.81 - 27.9]

Cap_Factor = [72.1, 70.1, 67.1, 73.6, 51.9]

indices = np.arange(len(cases[1:])) 

fig, ax = plt.subplots(figsize=(12.5, 6))

twin=ax.twinx()

BAR_G=ax.bar(indices, Gross, width=width, color='tab:blue',
             label='Gross Energy')
BAR_N=ax.bar([i+0.15*width for i in indices], Net, width=0.7*width,
             color='tab:olive', hatch ='//', alpha=0.5, edgecolor='w',
             label='Net Energy')
C_F=twin.plot(indices, Cap_Factor, '-', marker='o', ms= 10, color='tab:orange')

ax.set_ylabel('Energy [GWh]', fontsize= 16)
ax.set_xlabel('Cooling Scenarios', fontsize= 16)
ax.set_xticks(indices)
ax.set_yticks(np.arange(0, 160, 20))
ax.set_ylim(0, 160)
ax.set_xlim(-0.5, 4.5)
ax.set_xticklabels(cases[1:],fontsize= 14)
ax.tick_params(axis='y', which='major', labelsize=14)
ax.grid(axis= 'y')
ax.legend(loc=1, fontsize= '15')

twin.set_ylim(0, 100)
twin.set_ylabel('Capacity Factor [%]', fontsize=16, color='tab:orange')

autolabel(BAR_G)
autolabel_2(BAR_N,Net)

fig.tight_layout()
plt.savefig('graphs/annual_energy.png', format='png', bbox_inches='tight')

plt.show()

#%%
def autolabel_1(rects,bar_label):
    for idx,rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.04*height,
                bar_label[idx].astype(int),
                ha='center', va='bottom', rotation=0,fontsize= 11)
        
#%%
def autolabel_3(rects,bar_label):
    for idx,rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
                bar_label[idx].astype(int),
                ha='center', va='bottom', rotation=0,fontsize= 11)
        
#%%

r_salt_water = np.round(np.array([0, 591300, 0, 7782518, 7064064])/1000, 0)
sea_water_r = np.round(np.array([0, 212115, 0 , 7782518, 4221474])/1000, 0)
consumed_water = np.round(np.array([379185, 379185, 14005, 14004, 13811])/1000, 0)
produced_water = np.round(np.array([0, 0, 0, 0, 2842590])/1000, 0)

x = np.arange(len(cases[1:]))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width, r_salt_water, width, color='tab:blue',
                label= 'Sea Water Requirement')
rects0 = ax.bar([i-0.85*width for i in x], sea_water_r, width=0.7*width,
                color='tab:olive', hatch ='//', alpha=0.5, edgecolor='w',
                label='Sea Water Returned')
rects2 = ax.bar(x, consumed_water, width, color='tab:orange',
                label= 'Fresh Water Consumption')
rects3 = ax.bar(x + width, produced_water, width, color='tab:green',
                label= 'Fresh Water Production')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Water Volume [k m$^3$]', fontsize= 16)
ax.set_xlabel('Cooling Scenarios', fontsize= 16)
ax.set_xticks(x)
ax.set_xticklabels(cases[1:], fontsize= 14)
ax.grid(axis= 'y')
ax.legend(loc= 2, fontsize= '15')
ax.set_ylim(0, 8700)
ax.tick_params(axis='y', which='major', labelsize=14)

autolabel_1(rects1,r_salt_water)
autolabel_3(rects0,sea_water_r)
autolabel_1(rects2,consumed_water)
autolabel_1(rects3,produced_water)

fig.tight_layout()
plt.savefig('graphs/annual_water_utilization.png', format='png', bbox_inches='tight')
plt.show()

#%%

npv = np.array([17.806, 22.441, 17.106, 27.656, 22.635])
lcoe_real = np.array([89.7, 86.0, 89.3, 83.3, 76.0])
IRR = np.array([8.8 , 9.2 , 8.7, 9.7, 9.1 ])

x = np.arange(len(cases[1:]))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots(figsize=(14, 7))
fig.subplots_adjust(right=0.75)

twin1=ax.twinx()
twin2=ax.twinx()

twin2.spines['right'].set_position(("axes",1.1))

p1 = ax.bar(x , lcoe_real, width, color='tab:blue', label= 'LCOE')
p2, = twin1.plot(x, npv, ls='-',lw= 2, marker= 's', ms= 10,
                 color='tab:orange',label= 'NPV')
p3, = twin2.plot(x, IRR, ls='--',lw= 2, marker= '^', ms= 10,
                 color='tab:green',label= 'IRR')


ax.set_xlim(-0.5, 4.5)
twin1.set_ylim(0, 31.5)
twin2.set_ylim(0, 12)

ax.set_ylabel('LCOE [USD/MWh]', fontsize=16)
ax.set_xlabel('Cooling Scenarios', fontsize=18)
twin1.set_ylabel('NPV [M USD]', fontsize=16)
twin2.set_ylabel('IRR [%]', fontsize=16)

ax.yaxis.label.set_color('tab:blue')
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())

ax.set_xticks(x)
ax.set_yticks(np.arange(0, 120, 10))
ax.set_xticklabels(cases[1:], fontsize= 14)

ax.grid(axis= 'y')

tkw=dict(size=4,width=1.5)

ax.tick_params(axis='y',colors='tab:blue',**tkw, labelsize=14)
twin1.tick_params(axis='y',colors=p2.get_color(),**tkw, labelsize=14)
twin2.tick_params(axis='y', colors=p3.get_color(),**tkw, labelsize=14)
ax.tick_params(axis='x',**tkw)

autolabel_2(p1,lcoe_real)

ax.legend(handles=[p1,p2,p3], fontsize=14)

fig.tight_layout()
plt.savefig('graphs/lcoe_cases.png', format='png', bbox_inches='tight')
plt.show()





