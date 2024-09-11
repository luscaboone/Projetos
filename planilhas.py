import openpyxl

planilha_clientes = openpyxl.load_workbook('planilha.xlsx')
pagina_clientes = planilha_clientes['Sheet1']


for linha in pagina_clientes.iter_rows(min_row=2,values_only=True):
    nome,cpf,valor = linha
  
