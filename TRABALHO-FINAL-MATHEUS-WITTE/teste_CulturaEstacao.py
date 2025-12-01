from model.cultura_estacao import CulturaEstacao
from model.tipocultura_enum import TipoCultura
from model.classificacao_enum import ClassificacaoCultura
from teste_estacao import verao, inverno, outono, primavera;


milho = CulturaEstacao(
    nome="Milho",
    nome_cientifico="Zea mays",
    descricao="Cultura comum no verão.",
    tipo=TipoCultura.GRAO,
    classificacao=ClassificacaoCultura.ANGIOSPERMA,
    estacao=verao,
    nota_produtividade=7.5,
    nota_resistencia=8.0,
)
             
if __name__ == "__main__":
 print(milho.exibir_dados())    
 milho.concluir()

 print()

 print(milho.exibir_dados())   
 print()


