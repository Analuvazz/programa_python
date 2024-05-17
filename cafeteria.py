class Cafe:
    menu = {
        "Café Preto": 2.50,
        "Café com Leite": 3.00,
        "Cappuccino": 3.50,
        "Expresso": 2.00,
        "Chá": 2.00
    }

    def __init__(self):
        self.pedido = {}

    def fazer_pedido(self, item, quantidade):
        if item in self.menu:
            if item in self.pedido:
                self.pedido[item] += quantidade
            else:
                self.pedido[item] = quantidade
            print(f"{quantidade} {item}(s) adicionado(s) ao pedido.")
        else:
            print("Desculpe, esse item não está no menu.")

    def calcular_conta(self):
        total = 0
        for item, quantidade in self.pedido.items():
            total += self.menu[item] * quantidade
        return total

    def mostrar_menu(self):
        print("=== Menu ===")
        for item, preco in self.menu.items():
            print(f"{item}: R${preco:.2f}")
        print("============")

# Exemplo de uso:
cafeteria = Cafe()
cafeteria.mostrar_menu()

cafeteria.fazer_pedido("Café Preto", 2)
cafeteria.fazer_pedido("Cappuccino", 1)
cafeteria.fazer_pedido("Bolo", 1)  # Este item não está no menu

total_conta = cafeteria.calcular_conta()
print(f"Total da conta: R${total_conta:.2f}")