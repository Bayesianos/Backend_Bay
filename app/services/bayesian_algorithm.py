import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD

class Algorithm:
  arquivo = 'app/data/dadosCod.csv'
  temp = 'Age,Sex,Job,Housing,Saving accounts,Checking account,Credit amount,Duration,Purpose,Risk'
  
  def Calculate(self, dado):
    emprestimo_valido = False
    colunas_totais = self.temp.split(',')
    dados = pd.read_csv(self.arquivo, names=colunas_totais)
    modelo =  BayesianNetwork([('Age', 'Job'), ('Risk', 'Age'), ('Risk', 'Sex')]) #definir array de tuplas com os dados que fazem afeito para aprovação
    modelo.fit(dados) 

    inferencia = VariableElimination(modelo)
    
    result_dist = inferencia.query(['Risk'], evidence={'Age': dado['age'], 'Job': dado['job'], 'Sex': dado['sex']})
    
    array = result_dist.values
    
    if(array[0] < array[1] and array[1] >= 0.7):
      return True
    else:
      return False