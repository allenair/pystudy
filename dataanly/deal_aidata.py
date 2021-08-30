import numpy as np


def fetch_data(file_name):
    all_state = []
    with open('d:/all-state-code.csv', 'r', encoding='utf-8') as fstate:
        for line in fstate.readlines():
            all_state.append(line.strip())

    type_sym_map = {}
    with open(file_name, 'r', encoding='utf-8') as fin:
        for line in fin.readlines():
            line = line.strip()
            if len(line) == 0:
                continue

            case_code, type_code, sym_code = line.split(',')
            if (case_code + '#' + type_code) not in type_sym_map:
                type_sym_map[case_code + '#' + type_code] = []

            type_sym_map[case_code + '#' + type_code].append(sym_code)

    res_map = {}
    for key, val in type_sym_map.items():
        x_arr = np.zeros(len(all_state), dtype=np.uint8)
        for sc in val:
            index = all_state.index(sc)
            x_arr[index]=1
        res_map[key]=x_arr


    return res_map


map = fetch_data('d:/医案证型症状-1.csv')
for key, val in map.items():
    print('key: {}, val: {}'.format(key, val))
