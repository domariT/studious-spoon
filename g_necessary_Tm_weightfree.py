gmol_dict = {}
Tm_dict1={}
Tm_dict2={}
with open("c:\\Users\\oodom\\myapp\\g_necessary\\gmol_Tm.txt") as file:
    for i in file:
        (m, g, Tm) = i.split()
        gmol_dict[m] = float(g)
        Tm_dict1[m] = float(Tm)
        Tm_dict2[float(Tm)] = m

kind_imc = list(input('合成するIMCの種類は？(例:ni 3 sn 1)(多元系も可):').split())

time = int(len(kind_imc)/2)   #time=金属種の数
gmol_tot = 0.0
g_sev_list = []
for i in range(time):
    weight_sev = gmol_dict[kind_imc[i*2]]*int(kind_imc[i*2+1])     #weight_sev=金属種×組成比
    gmol_tot += weight_sev                                         #下準備
    g_sev_list.append(weight_sev)

weight = input('何g合成しますか？')
for i in range(time):
    g = str(int(g_sev_list[i]/gmol_tot*int(weight)*10000)/10000)+' g'     #必要量計算
    print(kind_imc[i*2], g, sep=' ')

Tm_sev=[Tm_dict1[kind_imc[i*2]] for i in range(time)]
Tm_sev.sort()
Tm_sev.reverse()
Tm_m_sort=[Tm_dict2[Tm_sev[i]] for i in range(time)]
print('\n')
print(*Tm_m_sort, sep='\n')
print('↑の順に置いてください')

input()