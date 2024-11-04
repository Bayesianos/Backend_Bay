import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

class Algorithm:
  arquivo = 'app/data/dadosCod.csv'
  temp = 'Age,Sex,Job,Housing,Saving_accounts,Checking_account,Credit_amount,Duration,Purpose,Risk'
  
  def define_bins(self, df, column_name, bins, labels):
    """Classifica os dados de acordo com as faixas definidas."""
    df[column_name] = pd.cut(df[column_name], bins=bins, labels=labels, right=False)
    return df
  
  def Calculate(self, dado):
    colunas_totais = self.temp.split(',')
    dados = pd.read_csv(self.arquivo, names=colunas_totais)
    
    # dados = self.define_bins(dados, 'Age', bins=[0, 18, 30, 40, 50, 60, 100], labels=['0', '1', '2', '3', '4', '5'])
    # dados = self.define_bins(dados, 'Credit_amount', bins=[0, 1000, 5000, 10000, 15000], labels=['0', '1', '2', '3'])
    
    # dados.to_csv(self.arquivo, index=False, header=False)
    
    modelo =  BayesianNetwork([('Risk', 'Age'), 
                               ('Risk', 'Sex'), 
                               ('Risk', 'Job'),
                               ('Risk', 'Housing'),
                               ('Risk', 'Saving_accounts'),
                               ('Risk', 'Checking_account'),
                               ('Risk', 'Credit_amount'),
                               ('Risk', 'Duration'),
                               ('Risk', 'Purpose')]) 
    modelo.fit(dados) 

    inferencia = VariableElimination(modelo)
    
    result_dist = inferencia.query(['Risk'], evidence={'Age': dado['age'], 
                                                       'Sex': dado['sex'],
                                                       'Job': dado['job'], 
                                                       'Housing': dado['housing'], 
                                                       'Saving_accounts': dado['saving_accounts'], 
                                                       'Checking_account': dado['checking_account'], 
                                                       'Credit_amount': dado['credit_amount'],
                                                       'Duration': dado['duration'],
                                                       'Purpose': dado['purpose']})
    
    array = result_dist.values
    
    print(result_dist)
    
    if(array[0] < array[1] and array[1] >= 0.7):
      return True
    else:
      return False