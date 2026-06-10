class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda.upper()
        self.saldo = saldo

    def converter_para_yuan(self):
        if self.moeda == "USD":
            return self.saldo / 0.14
        elif self.moeda == "BRL":
            return self.saldo / 0.85
        return self.saldo  # já está em CNY

    def __add__(self, valor_yuan):
        saldo_yuan = self.converter_para_yuan()
        novo_saldo_yuan = saldo_yuan + valor_yuan

        if self.moeda == "USD":
            return novo_saldo_yuan * 0.14
        elif self.moeda == "BRL":
            return novo_saldo_yuan * 0.85
        return novo_saldo_yuan

    def __sub__(self, valor_yuan):
        saldo_yuan = self.converter_para_yuan()
        novo_saldo_yuan = saldo_yuan - valor_yuan

        if self.moeda == "USD":
            return novo_saldo_yuan * 0.14
        elif self.moeda == "BRL":
            return novo_saldo_yuan * 0.85
        return novo_saldo_yuan

carteira_usd = Carteira("USD", 10.0)

print("Saldo após somar 50 yuan:", carteira_usd + 50.0)
print("Saldo após subtrair 20 yuan:", carteira_usd - 20.0)