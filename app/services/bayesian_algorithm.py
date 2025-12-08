import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

class Algorithm:
  arquivo = 'app/data/dadosCod.csv'
  temp = 'Age,Sex,Job,Housing,Saving_accounts,Checking_account,Credit_amount,Duration,Purpose,Risk'
  
  def Calculate(self, dado):
    colunas_totais = self.temp.split(',')
    dados = pd.read_csv(self.arquivo, names=colunas_totais)
    
    modelo =  BayesianNetwork([('Risk', 'Age'), 
                               ('Risk', 'Sex'), 
                               ('Risk', 'Job'),
                               ('Risk', 'Housing'),
                               ('Risk', 'Saving_accounts'),
                              #  ('Risk', 'Checking_account'),
                              #  ('Risk', 'Credit_amount'),
                              #  ('Risk', 'Duration'),
                               ('Risk', 'Purpose')]) 
    modelo.fit(dados) 

    inferencia = VariableElimination(modelo)
    
    result_dist = inferencia.query(['Risk'], evidence={'Age': dado['age'], 
                                                       'Sex': dado['sex'],
                                                       'Job': dado['job'], 
                                                       'Housing': dado['housing'], 
                                                       'Saving_accounts': dado['saving_accounts'], 
                                                      #  'Checking_account': dado['checking_account'], 
                                                      #  'Credit_amount': dado['credit_amount'],
                                                      #  'Duration': dado['duration'],
                                                       'Purpose': dado['purpose']})
    
    array = result_dist.values
    
    print(result_dist)
    
    if(array[0] < array[1] and array[1] >= 0.7):
      return True
    else:
      return False