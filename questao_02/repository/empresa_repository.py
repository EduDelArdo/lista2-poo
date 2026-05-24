from typing import List
from questao_02.models.funcionario import Funcionario

class EmpresaRepository:
    def __init__(self, nome_empresa: str):
        self.nome_empresa = nome_empresa
        self._funcionarios: List[Funcionario] = []

    def cadastrar_funcionario(self, funcionario: Funcionario) -> None:
        self._funcionarios.append(funcionario)

    def obter_todos_os_funcionarios(self) -> List[Funcionario]:
        return self._funcionarios