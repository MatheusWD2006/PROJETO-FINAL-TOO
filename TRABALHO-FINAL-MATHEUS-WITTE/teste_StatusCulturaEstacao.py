from model.cultura_estacao import CulturaEstacao
from model.StatusCulturaEstacao import StatusCulturaEstacao
from teste_CulturaEstacao import milho 


milho_status = StatusCulturaEstacao(
    cultura_estacao=milho,
    data_plantio="15-09-2025",
    status="PLANTADO"
)

print(milho_status.exibir_dados())
milho.concluir()
milho_status.concluir()
print()
print(milho_status.exibir_dados())
print()
milho_status.concluir()
print(milho_status.exibir_dados())