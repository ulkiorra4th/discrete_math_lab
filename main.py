SECOND_PART = False


def is_adsorbed(absorber, absorbing):
    return len(absorber) < len(absorbing) \
        and all(absorbing.count(absorber[i]) == 1 for i in range(len(absorber)))


def represent_graph_as_equation(input_graph):
    equation = ''
    for first_node in input_graph:
        for second_node in input_graph[first_node]:
            equation += f'({first_node}+{second_node})*'
    return equation[:-1]


def get_unique_list(input_list):
    unique = []
    for item in input_list:
        if item not in unique:
            unique.append(item)
    return unique


def remove_absorbed_monomials(input_monomials):
    adsorbed_monomials = [second for second in input_monomials for first in input_monomials if is_adsorbed(first, second)]
    return [monomial for monomial in input_monomials if monomial not in adsorbed_monomials]


def get_nodes(input_graph):
    graph_nodes = set(node for x in input_graph for node in input_graph[x])
    for node in input_graph: graph_nodes.add(node)
    return list(graph_nodes)


def multiply_parentheses(input_monomials):
    monomials_copy = input_monomials.copy()

    for i in range(len(monomials_copy) - 1):
        monomial = []
        for j in range(len(monomials_copy[0])):
            for k in range(len(monomials_copy[1])):
                b = [x for x in monomials_copy[0][j]]
                for x in monomials_copy[1][k]: b.append(x)
                monomial.append(sorted(list(set(b))))
        monomials_copy.append(monomial)
        monomials_copy = monomials_copy[2:]

    monomials_copy = monomials_copy[0]
    return monomials_copy


# Сюда вписать свой граф в виде словаря, ключ - узел, значение - смежные узлы (без дубликатов)
graph = {'a': ['b', 'd', 'g'], 'b': ['d', 'f'], 'c': ['d'], 'd': ['e', 'f', 'g']}
nodes = get_nodes(graph)

print(f'\nИсходный граф: {graph}\n')
print('------------------------------------------------------')
print(f'П={represent_graph_as_equation(graph)}')
print('------------------------------------------------------\n')

# first step
monomials = [[node, graph[node]] for node in graph]
second_eq = 'П`= ' + '*'.join(f'({monomial[0]}+{"*".join(monomial[1])})' for monomial in monomials)

# second step
monomials = multiply_parentheses(monomials)
polynomial = '+'.join(sorted(list(set('*'.join(monomial) for monomial in monomials))))
second_eq += f" = {polynomial}"

# third step
monomials = remove_absorbed_monomials(monomials)
monomials = get_unique_list(monomials)
result = '+'.join(sorted(list(set('*'.join(monomial) for monomial in monomials))))
second_eq += f" = {result}"

inner_sets = [sorted(list(set(nodes) - set(monomial))) for monomial in monomials]

print('------------------------------------------------------')
print(second_eq)
print(f'П`={result}')
print('------------------------------------------------------\n')
print('------------------ANSWER------------------')
print('МАКСИМАЛЬНОЕ ВУМ\t\t\tМОЩНОСТЬ ВУМ')
print(*['\t\t\t'.join(['-'.join(inner_set), '|', str(len(inner_set)), '\n']) for inner_set in inner_sets])
print(f'КОЛИЧЕСТВО МАКСИМАЛЬНЫХ ВУМ: {len(monomials)}')
print(f'НАИБОЛЬШЕЕ ВУМ: {max(len(inner_set) for inner_set in inner_sets)}')
print('------------------------------------------')

# для решения лабораторной "Алгоритм минимальной раскраски графа на основе метода Магу"
if SECOND_PART:
    print('\nSECOND_PART\n')

    # сюда вписать выражение. Например, для F1*(F3+F5+F6)*(F2+F1)*F2 вписать [['1'], ['3', '5', '6'], ['2', '1'], '2']
    f_monomials = [['4', '5'], ['2', '3'], ['1'], ['1', '3', '5'], ['4'], ['2', '4'], ['4']]

    f_monomials = multiply_parentheses(f_monomials)
    f_monomials = remove_absorbed_monomials(f_monomials)
    f_monomials = get_unique_list(f_monomials)

    third_eq = f"П(G) = {'+'.join(sorted(list(set('*'.join(monomial) for monomial in f_monomials))))}"

    print('------------------')
    print(third_eq)
    print('------------------')