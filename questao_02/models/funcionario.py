from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def obter_dados(self) -> str:
        return f"Nome: {self.nome} | CPF: {self.cpf}"

    @abstractmethod
    def calcular_pagamento(self) -> float:
        """Método abstrato que força as subclasses a calcularem seus salários."""
        pass


class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome: str, cpf: str, salario_mensal: float):
        super().__init__(nome, cpf)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self) -> float:
        return self.salario_mensal


class FuncionarioHorista(Funcionario):
    def __init__(self, nome: str, cpf: str, horas_trabalhadas: float, valor_hora: float):
        super().__init__(nome, cpf)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self) -> float:
        return self.horas_trabalhadas * self.valor_hora


class FuncionarioComissionado(Funcionario):
    def __init__(self, nome: str, cpf: str, total_vendas: float, percentual_comissao: float):
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao  # Ex: 0.05 para 5%

    def calcular_pagamento(self) -> float:
        return self.total_vendas * self.percentual_comissao