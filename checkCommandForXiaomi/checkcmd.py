import os
import sys
import pandas as pd
from pandas import Series,DataFrame

def txt2df(filename):
    file = open(filename, 'r')
    file = file.readlines()
    cmd_id_list = []
    cmd_str_list = []
    
    cmd = {}
    for i in file:
        i = i.strip()
        if 'public static final int CMDID' in i and '=' in i:
            # print(i)
            cmd_id = i.split('=')[1].strip()[:-1]
            cmd_str = i.split('=')[0].strip().split(' ')[-1]
            # print (cmd_id, cmd_str)
            # print (cnt)
            cmd_id_list.append(cmd_id)
            cmd_str_list.append(cmd_str)

    cmd['cmd_str'] = cmd_str_list
    cmd['cmd_id'] = cmd_id_list
    cmd_df = DataFrame(cmd)
    return cmd_df

cmd_df_standard = txt2df(str(sys.argv[1]))
cmd_df_process = txt2df(str(sys.argv[2]))

cmd_df_common_str = cmd_df_standard.merge(cmd_df_process, left_on='cmd_str', right_on='cmd_str', how='outer')
cmd_df_common_id = cmd_df_standard.merge(cmd_df_process, left_on='cmd_id', right_on='cmd_id', how='outer')

res_df_common_str = cmd_df_common_str.loc[cmd_df_common_str['cmd_id_x'] != cmd_df_common_str['cmd_id_y']]
print(res_df_common_str)
res_df_common_str.to_csv('res_df_common_str_' + str(sys.argv[1])[:-4] + '_' + str(sys.argv[2])[:-4] + '.csv')

res_df_common_id = cmd_df_common_id.loc[cmd_df_common_id['cmd_str_x'] != cmd_df_common_id['cmd_str_y']]
print(res_df_common_id)
res_df_common_id.to_csv('res_df_common_id_' + str(sys.argv[1])[:-4] + '_' + str(sys.argv[2])[:-4] + '.csv')
