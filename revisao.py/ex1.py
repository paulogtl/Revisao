pedidos = [
    {
        "cliente": "Ana",
        "itens": [
            {"prato": "Lasanha", "preco": 30},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
    },
    {
        "cliente": "Bruno",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Refrigerante", "preco": 6},
            {"prato": "Sobremesa", "preco": 12}
        ]
    },
    {
        "cliente": "Carla",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
    }
]
def total_gasto_por_cliente(nome_cliente, pedidos):
    total = 0
    for pedido in pedidos:
        if pedido["cliente"] == nome_cliente:
            total += sum(item["preco"] for item in pedido["itens"])
    return total

print(total_gasto_por_cliente("Bruno", pedidos))  # Saída: 58

from collections import Counter

def prato_mais_vendido(pedidos):
    contador = Counter()
    for pedido in pedidos:
        for item in pedido["itens"]:
            contador[item["prato"]] += 1
    return contador.most_common(1)[0]  # Retorna (prato, quantidade)

print(prato_mais_vendido(pedidos))  # Saída: ('Pizza', 2)

def ranking_clientes(pedidos):
    gastos = {}
    for pedido in pedidos:
        cliente = pedido["cliente"]
        total = sum(item["preco"] for item in pedido["itens"])
        gastos[cliente] = gastos.get(cliente, 0) + total
    ranking = sorted(gastos.items(), key=lambda x: x[1], reverse=True)
    return ranking[:3]

print(ranking_clientes(pedidos))
# Saída: [('Bruno', 58), ('Carla', 48), ('Ana', 38)]
