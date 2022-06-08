
import pyautogui


# pyautogui.sleep(3)
# pyautogui.press('winleft')
# pyautogui.sleep(1)
# pyautogui.write('\\\\172.16.0.4\chaves')
# pyautogui.sleep(1)
# pyautogui.press('enter')
#
# pyautogui.sleep(3)
# pyautogui.write('dto')
# pyautogui.write('2022')
# pyautogui.sleep(1)
# pyautogui.press(['tab', 'tab'])
# pyautogui.press('enter')

# Entra no diretório c: para realizar a busca pelos e-mails.
pyautogui.alert( '***Atenção***\n'
                'Clique em [ok] para inicializar o programa.')
pyautogui.press('winleft')
pyautogui.sleep(3)
pyautogui.write('C:')
pyautogui.sleep(3)
pyautogui.press('enter')

#pesquisa e entra na pasta desejada.
pyautogui.sleep(3)
pyautogui.hotkey('ctrl', 'f')
pyautogui.sleep(3)
pyautogui.write('PV 59117')
pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(3)
pyautogui.press('tab')
pyautogui.sleep(3)
pyautogui.press('space')
pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(3)

#pesquisa e entra no bloco de notas que contém os e-mais do office.
pyautogui.hotkey('ctrl', 'f')
pyautogui.sleep(3)
pyautogui.write('EMAILOFICE')
pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(3)
pyautogui.press('tab')
pyautogui.sleep(3)
pyautogui.press('space')
pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(3)
#realiza a copia dos e-mails
pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')
pyautogui.press('right', presses=1)
pyautogui.keyUp('ctrl')
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
pyautogui.sleep(3)
pyautogui.press('backspace')
pyautogui.sleep(3)
pyautogui.press('down')
pyautogui.sleep(3)
pyautogui.press('backspace', presses=2)
pyautogui.hotkey('ctrl','s')
#entrando no ofice para criação do email
pyautogui.press('winleft')
pyautogui.sleep(3)
pyautogui.write('word')
pyautogui.sleep(5)
pyautogui.press('enter')
pyautogui.sleep(6)
pyautogui.press('tab')
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(16)
pyautogui.press('tab')
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.sleep(1)
#entrando no bloco de nota para copiar a senha pré definida
pyautogui.keyDown('alt')
pyautogui.press('tab', presses=2)
pyautogui.keyUp('alt')
pyautogui.sleep(1)
pyautogui.keyDown('shift')
pyautogui.keyDown('ctrl')
pyautogui.keyDown('capslock')
pyautogui.press('right', presses=1)
pyautogui.keyUp('capslock')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('shift')
pyautogui.sleep(1)
pyautogui.hotkey('ctrl','c')
pyautogui.sleep(1)
#voltando no ofice para colar a senha
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
pyautogui.sleep(1)
pyautogui.hotkey('tab', presses=5)
pyautogui.press('enter')
pyautogui.sleep(2)








#pyautogui.sleep(3)
#pyautogui.hotkey('ctrl', 's')

#pyautogui.sleep(3)
#pyautogui.hotkey('alt','tab')



#pyautogui.press('winleft')
#pyautogui.sleep(3)
#pyautogui.write('slui')
#pyautogui.sleep(1)
#pyautogui.press('right')
#pyautogui.press('down')
#pyautogui.sleep(3)
#pyautogui.press('enter')
#pyautogui.sleep(5)
#pyautogui.press('enter')
#pyautogui.sleep(5)
