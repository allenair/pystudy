
def fetch_data(file_name):
    all_state = []
    with open('d:/all-state-code.csv', 'r', encoding='utf-8') as fstate:
        for line in fstate.readlines():
            all_state.append(line.strip())

    with open(file_name, 'r', encoding='utf-8') as fin:
        for line in fin.readlines():
            line = line.strip()
            if len(line)==0:
                continue
            
            case_code, type_code, sym_code = line.split(',')

fetch_data('e:/医案证型症状.csv')