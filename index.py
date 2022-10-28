import Xpath_Performance as rpa
import time
import openpyxl

#Abre o navegador
rpa.rpa_site('https://app.omie.com.br/gestao/base-ed6krt/')
rpa.rpa_maximizar_janela()

#Login Omie
rpa.rpa_env_texto('//*[@id="email"]', 'glicio.oliveirajr@gmail.com')
rpa.rpa_click('//*[@id="btn-continue"]')
rpa.rpa_env_texto('//*[@id="current-password"]', 'Glicio@03080308')
rpa.rpa_click('//*[@id="btn-login"]')

#Acessando modulo de vendas
rpa.rpa_click('/html/body/div[2]/div[4]/div[2]/ul/li[2]/a')
rpa.rpa_click('/html/body/div[2]/div[4]/div[1]/div[2]/div/div[3]/div[3]/div/a[4]/span[2]/div/div/div')

#Abre a planilha
planilha = openpyxl.load_workbook('Pasta1.xlsx')
aba = planilha['Planilha1']
linha = 2

#Loop Core
while True:
    codigoProduto = aba[f'A{linha}'].value
    codigoEan = aba[f'B{linha}'].value
    print(f'Codigo do Produto: {codigoProduto} - Codigo EAN: {codigoEan} - Linha: {linha}')

    #Pesquisar produto
    rpa.rpa_sel_texto('/html/body/div[2]/div[6]/div[2]/div[3]/div[2]/div[2]/div/div[3]/table/thead/tr[2]/td[4]/span/input')
    rpa.rpa_env_texto('/html/body/div[2]/div[6]/div[2]/div[3]/div[2]/div[2]/div/div[3]/table/thead/tr[2]/td[4]/span/input', codigoProduto)
    rpa.rpa_enter('/html/body/div[2]/div[6]/div[2]/div[3]/div[2]/div[2]/div/div[3]/table/thead/tr[2]/td[4]/span/input')

    #Verifica o tempo
    rpa.rpa_click('//*[@id="d50480c10000g_CODIGO"]')

    #Verificar o registro + Condição core
    registro = rpa.rpa_texto_xpath('/html/body/div[2]/div[6]/div[2]/div[3]/div[2]/div[2]/div/div[63]/span/span[1]')
    registro = registro[0]
    registro = int(registro)
    if registro >= 1:
        rpa.rpa_click_duplo('//*[@id="d50480c10000g"]/colgroup')
        rpa.rpa_click('//*[@id="d50480c33"]')
        rpa.rpa_env_texto('//*[@id="d50480c33"]', codigoEan)
        rpa.rpa_click('/html/body/div[2]/div[6]/div[2]/div[3]/div[1]/ul/a[1]')
        time.sleep(1)
        rpa.rpa_click('//*[@id="dialog-50480"]/div[1]/button/i')
    linha += 1

        

    






