from itertools import permutations 
tot_new_ATM = int(input())
tot_area_loc = int(input())

atm_index = []
area_list = []
area_cost_list = []
tot_sum = 99

for i in range(0,tot_area_loc):
    atm_index.append(i)
    area_list.append(int(input()))
    area_cost_list.append(None)

# get all possible combintions
area_perm_index = permutations(atm_index,tot_new_ATM)

# iterate each combination
for atm_index in area_perm_index:
    # init area cost with not atm to none
    for l in range(0,tot_area_loc):
        area_cost_list[l] = None

    # init area cost with atm to 0
    for k in atm_index:
        area_cost_list[k] = 0
    
    # claculte cost for each area
    for i in range(0,tot_area_loc):
        if area_cost_list[i] != 0 and area_cost_list[i] == None:
            for a in range(0,tot_new_ATM-1):
                if atm_index[a] > i and atm_index[a+1] > i and a == 0:
                    area_cost_list[i] = abs(area_list[atm_index[a]] - area_list[i])
                    break
                elif atm_index[a] < i and i < atm_index[a+1]:
                    if abs(area_list[a] - area_list[i]) > abs(area_list[atm_index[a+1]] - area_list[i]):
                        area_cost_list[i] = abs(area_list[atm_index[a+1]] - area_list[i])
                    else:
                        area_cost_list[i] = abs(area_list[atm_index[a]] - area_list[i])
                    break
                elif atm_index[a] < i and atm_index[a+1] < i and a == tot_new_ATM-2:
                    area_cost_list[i] = abs(area_list[atm_index[a+1]] - area_list[i])
                    break
                else:
                    pass

    temp_tot_sum = 0
    for cost in area_cost_list:
        temp_tot_sum = temp_tot_sum + cost
    if temp_tot_sum < tot_sum:
        tot_sum = temp_tot_sum
        final = atm_index
print(final)      
print(tot_sum)