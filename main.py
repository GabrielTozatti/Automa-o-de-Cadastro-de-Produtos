# IMPORTS
import pyautogui
import pandas as pd
from time import sleep

# URL DO LOCAL DO CADASTRO
url = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'cadastro@gmail.com'
senha = '@123456@'

# TEMPO ENTRE CADA AÇÃO A SER EXECUTADA
pyautogui.PAUSE = 0.5

# ABRIR GOOGLE
pyautogui.press('win')
pyautogui.write('google')
pyautogui.press('enter')

# CARREGAR URL
pyautogui.write(url)
pyautogui.press('enter')
sleep(2)

# REALIZAR LOGIN NO PAINEL
pyautogui.click(x=759, y=405)
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.click(x=954, y=567, button='left', clicks=2)
sleep(2)

# IMPORTANDO A BASE DE DADOS
data = pd.read_csv('produtos.csv')

# CADASTRAR PRODUTO
for linha in data.index:
    pyautogui.click(x=814, y=282)
    pyautogui.write(data.loc[linha, 'codigo'])
    pyautogui.press('tab')
    pyautogui.write(data.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(data.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(str(data.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(data.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(data.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = data.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(data.loc[linha, 'obs'])
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(99999)