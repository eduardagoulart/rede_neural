from csv import reader


def read_file(filename):
    dataset = []
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)

    for i in range(len(dataset)):
        if not dataset[:-2]:
            print(dataset)
            dataset[i] = float(dataset[i])
        # try:
        #     print("ENTRA AQUI")
        #     dataset = float(i)
        # except:
        #     continue

    # for i in dataset:
    #     for j in i:
    #         print(f'dataset: {j}, type: {type(j)}')

read_file('bases/kernel_data_balanced.csv')