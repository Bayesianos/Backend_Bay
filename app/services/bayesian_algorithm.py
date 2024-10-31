import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD

class Algorithm:
  arquivo = 'app/data/german_credit_data.csv'
  temp = 'Age,Sex,Job,Housing,Saving accounts,Checking account,Credit amount,Duration,Purpose,Risk'
  
  
  def Calculate(self):
    colunas = self.temp.split(',')
    dados = pd.read_csv(self.arquivo, names=colunas)
    modelo =  BayesianNetwork([]) #definir array de tuplas com os dados que fazem afeito para aprovação
    modelo.fit(dados)
    inferencia = VariableElimination(modelo)

    dadosCsv = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])

    dadosFinais = TabularCPD(variable='B', variable_card=2,
                              values=[[0.8, 0.1], [0.2, 0.9]],
                              evidence=['A'], evidence_card=[2])

    modelo.add_cpds(dadosCsv, dadosFinais)
    
    # retornar a probabilidade do risco do usuario com base nos dados do csv 