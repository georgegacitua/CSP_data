import numpy as np
import matplotlib.pyplot as plt

#%%  Sensitivity analysis: #ONCE THROUGH

var = ['-25%', '-20%', '-15%', '-10%', '-5%', '0%', '5%', '10%', '15%', '20%', '25%']
capex =np.array([53791084, 48564150, 43337216, 38110282, 32883348, 27656414, 22429480, 17202546, 11975612, 6748678, 1521744])
opex = np.array([32136359, 31240370, 30344381, 29448392, 28552403, 27656414, 26760425, 25864436, 24968447, 24072458, 23176468])
revenue = np.array([-9872305, -2366561, 5139183, 12644926, 20150670, 27656414, 35162158, 42667901, 50173645, 57679389, 65185133])
energy = np.array([-8541382, -1301823, 5937736, 13177295, 20416855, 27656414, 34895973, 42135532, 49375091, 56614651, 63854210])

#Graph
plt.figure(figsize=(12, 6)) #Image Size
plt.plot(var, capex/1000000, ls= '-', lw= 2, marker= '^', ms= 10, label= 'CAPEX')
plt.plot(var, opex/1000000, ls= '-', lw= 2, marker= 's', ms= 10, label= 'OPEX')
plt.plot(var, revenue/1000000, ls= '-', lw= 2, marker= '*', ms= 10, label= 'PPA')
plt.plot(var, energy/1000000, ls= '-', lw= 2, marker= 'o', ms= 10, label= 'Net Energy')
plt.plot([-1, 11], [0, 0], color= 'k', ls= '-', lw= 1)
plt.yticks(np.arange(-20, 70, 10), fontsize= 14)
plt.xticks(fontsize= 14)
plt.xlabel(r'Variation', fontsize=16)
plt.ylabel(r'NPV [M USD]', fontsize=16)
plt.xlim(-.3, 10.3)
plt.ylim(-15, 67)
plt.legend(fontsize= 14)
plt.grid()

#Save figure
plt.savefig('graphs/van_ot.png', format='png', bbox_inches='tight')
plt.show()

#%%  Sensitivity analysis: #MED Energy
var = ['-25%', '-20%', '-15%', '-10%', '-5%', '0%', '5%', '10%', '15%', '20%', '25%']
capex = np.array([48690321, 43479318, 38268315, 33057312, 27846309, 22635306, 17424303,
                  12213300, 7002297, 1791294, -3419708])
opex = np.array([28134686, 27034810, 25934934, 24835058, 23735182, 22635306, 21535430,
                 20435554, 19335678, 18235803, 17135927])
revenue = np.array([424133, 4866368, 9308602, 13750837, 18193072, 22635306, 27077541,
                    31519775, 35962010, 40404245, 44846479])
energy = np.array([5923513, 9265872, 12608230, 15950589, 19292948, 22635306, 25977665,
                   29320024, 32662382, 36004741, 39347100])
w_capex = np.array([24589644, 24198777, 23807909, 23417041, 23026174, 22635306,
                  22244439, 21853571, 21462703, 21071836, 20680968])
w_revenue = np.array([5678920, 9070198, 12461475, 15852752, 19244029, 22635306,
                    26026583, 29417861, 32809138, 36200415, 39591692])
#Graph
plt.figure(figsize=(12, 6)) #Image Size
plt.plot(var, capex/1000000, ls= '-', lw= 2, marker= '^', ms= 10, label= 'CAPEX CSP')
plt.plot(var,w_capex/1000000, ls= '-', lw= 2, marker= 'X', ms= 10, label= 'CAPEX MED')
plt.plot(var, opex/1000000, ls= '-', lw= 2, marker= 's', ms= 10, label= 'OPEX')
plt.plot(var, revenue/1000000, ls= '-', lw= 2, marker= 'h', ms= 10, label= 'PPA')
plt.plot(var, w_revenue/1000000, ls= '-', lw= 2, marker= '*', ms= 10, label= 'Water Revenue')
plt.plot(var, energy/1000000, ls= '-', lw= 2, marker= 'o', ms= 10, label= 'Net Energy')

plt.plot([-1, 11], [0, 0], color= 'k', ls= '-', lw= 1)
plt.yticks(np.arange(-20, 70, 10), fontsize= 14)
plt.xticks(fontsize= 14)
plt.xlabel(r'Variation', fontsize=16)
plt.ylabel(r'NPV [M USD]', fontsize=16)

plt.xlim(-.3, 10.3)
plt.ylim(-15, 67)
plt.legend(fontsize= 14)
plt.grid()

#Save figure
plt.savefig('graphs/van_med.png', format='png', bbox_inches='tight')
plt.show()

#%%  Sensitivity analysis: #LCOE CAPEX

var = ['-25%', '-20%', '-15%', '-10%', '-5%', '0%', '5%', '10%', '15%', '20%', '25%']
base = np.array([71.9, 75.5, 79.0, 82.6, 86.1, 89.7, 93.2, 96.8, 100.3, 103.8, 107.4])
evap = np.array([67.7, 71.3, 75.0, 78.7, 82.3, 86.0, 89.7, 93.3, 97.0, 100.7, 104.3])
dry = np.array([70.2, 74.0, 77.8, 81.6, 85.4, 89.3, 93.1, 96.9, 100.7, 104.5, 108.3])
ot = np.array([65.5, 69.0, 72.6, 76.1, 79.7, 83.2, 86.8, 90.3, 93.9, 97.4, 101.0])
med = np.array([46.1, 52.1, 58.1, 64.0, 70.0, 76.0, 82.0, 88.0, 94.0, 99.9, 105.9])
w_med = np.array([73.8, 74.2, 74.7, 75.1, 75.6, 76.0, 76.5, 76.9, 77.4, 77.8, 78.3])

#Graph
plt.figure(figsize=(12, 6)) #Image Size
plt.plot(var, base, ls= '-', lw= 2, marker= '^', ms= 10, label= 'Base Case')
plt.plot(var, evap, ls= '-', lw= 2, marker= 's', ms= 10, label= 'Evaporative Cooling')
plt.plot(var, dry, ls= '-', lw= 2, marker= '*', ms= 10, label= 'Dry Cooling')
plt.plot(var, ot, ls= '-', lw= 2, marker= 'o', ms= 10, label= 'Once Through Cooling')
plt.plot(var, dry, ls= '-', lw= 2, marker= 'h', ms= 10, label= 'Dry Cooling')
plt.plot(var, ot, ls= '-', lw= 2, marker= 'D', ms= 10, label= 'Once Through Cooling')
plt.plot(var, med, ls= '-', lw= 2, marker= 'X', ms= 10, label= 'MED Case \n(CSP CAPEX)')
plt.plot(var, w_med, ls= '-', lw= 2, marker= 'o', ms= 10, label= 'MED Case \n(MED CAPEX)')

plt.plot([-1, 11], [0, 0], color= 'k', ls= '-', lw= 1)
plt.yticks(np.arange(0, 120, 10), fontsize= 14)
plt.xticks(fontsize= 14)
plt.xlabel(r'CAPEX Variation', fontsize=16)
plt.ylabel(r'LCOE [USD/MWh]', fontsize=16)
plt.xlim(-.3, 10.3)
plt.ylim(0, 120)
plt.legend(fontsize= 14)
plt.grid()

#Save figure
plt.savefig('graphs/lcoe_capex.png', format='png', bbox_inches='tight')
plt.show()

#%%  Sensitivity analysis: #LCOE GENERATION

var = ['-25%', '-20%', '-15%', '-10%', '-5%', '0%', '5%', '10%', '15%', '20%', '25%']
base = np.array([118.4, 111.2, 104.8, 99.2, 94.2, 89.7, 85.6, 81.8, 78.4, 75.3, 72.4])
evap = np.array([113.4, 106.6, 100.5, 95.1, 90.3, 86.0, 82.1, 78.5, 75.3, 72.3, 69.5])
dry = np.array([117.8, 110.7, 104.4, 98.8, 93.8, 89.3, 85.2, 81.5, 78.1, 75.0, 72.1])
ot = np.array([109.7, 103.1, 97.3, 92.1, 87.4, 83.2, 79.4, 76.0, 72.8, 69.9, 67.3])
med = np.array([99.8, 93.8, 88.6, 83.9, 79.8, 76.0, 72.6, 69.5, 66.7, 64.1, 61.8])
w_med = np.array([95.5, 91.6, 87.7, 83.8, 79.9, 76.0, 72.1, 68.2, 64.3, 60.4, 56.5])

#Graph
plt.figure(figsize=(12, 6)) #Image Size
plt.plot(var, base, ls= '-', lw= 2, marker= '^', ms= 10, label= 'Base Case')
plt.plot(var, evap, ls= '-', lw= 2, marker= 's', ms= 10, label= 'Evaporative Cooling')
plt.plot(var, dry, ls= '-', lw= 2, marker= '*', ms= 10, label= 'Dry Cooling')
plt.plot(var, ot, ls= '-', lw= 2, marker= 'o', ms= 10, label= 'Once Through Cooling')
plt.plot(var, dry, ls= '-', lw= 2, marker= 'h', ms= 10, label= 'Dry Cooling')
plt.plot(var, ot, ls= '-', lw= 2, marker= 'D', ms= 10, label= 'Once Through Cooling')
plt.plot(var, med, ls= '-', lw= 2, marker= 'X', ms= 10, label= 'MED Case \n(Energy Generation)')
plt.plot(var, w_med, ls= '-', lw= 2, marker= 'o', ms= 10, label= 'MED Case \n(MED Generation)')

plt.plot([-1, 11], [0, 0], color= 'k', ls= '-', lw= 1)
plt.yticks(np.arange(0, 130, 10), fontsize= 14)
plt.xticks(fontsize= 14)
plt.xlabel(r'Generation Variation', fontsize=16)
plt.ylabel(r'LCOE [USD/MWh]', fontsize=16)
plt.xlim(-.3, 10.3)
plt.ylim(0, 120)
plt.legend(fontsize= 14)
plt.grid()

#Save figure
plt.savefig('graphs/lcoe_gen.png', format='png', bbox_inches='tight')
plt.show()