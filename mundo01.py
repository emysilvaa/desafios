import math
import random
from random import randint
from datetime import date

def desafio001():
  print('Olá, mundo!')


def desafio002(name):
  print(f'Bem vindo, {name}')


def desafio003():
 n1 = int(input('digite um número:')) 
 n2 = int(input('digite outro número:')) 
 s = n1+n2
 print(f'A soma de {n1} e {n2} é igual a:{n1+n2}') 


def desafio004():
  a = (input('digite algo:'))
  print('o tipo primitivo deste valor é:', type(a))
  print('ele é numérico?', a.isnumeric()) 
  print('ele é alfabatico?', a.isalpha()) 
  print('ele é alfanumérico?', a.isalnum()) 
  print('está em maiúscula?', a.isupper())
  print('está em minúscula?', a.islower()) 
  print('pode ser impresso?', a.isprintable()) 
  print('é um espaço?', a.isspace()) 
  print('está cripitalizado?', a.istitle()) 

  
def desafio005():
  n1 = int(input('digite um número:'))
  s = n1+1
  a = n1 - 1
  print(f'o sucesor de {n1} é {s} e o seu antecessor é {a}')


def desafio006():
  n1 = int(input('digite um número:'))
  d = n1 * 2
  t = n1 * 3
  r = n1 ** (1/2)
  print(f'o dobro de {n1} é {d}.')
  print(f'o triplo de {n1} é {t}.')
  print(f'e a raiz quadrada de {n1} é {r}.')
  

def desafio007():
  n1 = float(input('primeira nota do aluno:'))
  n2 = float(input('segunda nota do aluno:'))
  m = (n1 + n2) / 2
  print(f' A média da nota é:{m}')


def desafio008():
  valor = int(input('digite uma distancia em metros:'))
  cm = valor * 100
  mm = valor * 1000
  print(f'o centimetro de {valor} é {cm} cm.')
  print(f'e o milimetro de {valor} é {mm} mm.')

def desafio009():
  n = int(input('digite um número para saber a sua tabuada:'))
  print('{} X {} = {}' .format(n, 1 , n * 1))
  print("{} X {} = {}" .format(n, 2 , n * 2))
  print("{} X {} = {}" .format(n, 3 , n * 3))
  print("{} X {} = {}" .format(n, 4 , n * 4))
  print("{} X {} = {}" .format(n, 5 , n * 5)) 
  print("{} X {} = {}" .format(n, 6 , n * 6))
  print("{} X {} = {}" .format(n, 7 , n * 7))
  print("{} X {} = {}" .format(n, 8 , n * 8))
  print("{} X {} = {}" .format(n, 9 , n * 9))
  print("{} X {} = {}" .format(n, 10 , n * 10))

def desafio010():
  real = float(input('quanto você tem de dinheiro na sua carteira? R$'))
  dolar = real / 5 #arrendondei para 5 reais 
  print(f'com R${real} você pode comprar:US$ {dolar}')

def desafio011():
  l = float(input('qual a largura da sua parede?'))
  a = float(input('qual a altura da sua parede?'))
  
  área = l * a
  print(f'sua parde tem a dimensão de {l} X {a} e a sua área é de: {área}m².')
  tinta = área / 2
  print(f'para pintar essa parede, você vai precisar de {tinta}L de tinta.')

def desafio012():
  preço = float(input('digite o preço de algum produto:'))
  desconto = preço * (1 - 5/100)
  print('o seu desconto é de 5%')
  print(f'o valor final da sua compra com o desconto é de R${desconto}')

def desafio013():
  sálario = float(input('difite o seu sálario:'))
  aumento = sálario * (1 + 15/100)
  print(f'o aumento do seu sálario foi de 15% sendo assim, o seu sálario agora é: R${aumento}')
  
def desafio014():
  c = float(input('digite a temperatura do dia:'))
  f =((9 * c)/5)+32 
  print(f'a temperantura {c}C° corresponde a {f}F°.')

def desafio015():
  dias = int(float(input('quantos dias alugados?')))
  km = int(float(input('quantos km foi percorrido?')))
  pago = (dias * 60) + (km * 0.15)
  print(f'o total a pagar é de: R${pago}')

def desafio016():
  n = float(input('digite um número real:'))
  pi = math.trunc(n)
  print(f' A porção inteira de {n} é: {pi}')

def desafio017():
  co = float(input('comprimento do cateto oposto:'))
  ca = float(input('comprimento do cateto adjecente:'))
  hi = math.hypot(co , ca)
  print('a hipotenusa vai médir:{:.2f}'.format(hi))
  
def desafio018():
  ângulo = float(input('digite o ângulo desejado:'))
  seno = math.sin(math.radians(ângulo))
  print('o ângulo de {} tem o Seno de: {:.2f}'.format(ângulo, seno))
  cosseno = math.cos(math.radians(ângulo))
  print('o ângulo de {} tem o Cosseno de {:.2f}'. format(ângulo,cosseno))
  tangente = math.tan(math.radians(ângulo))
  print('o ãngulo de {} tem o Tangente de {:.2f}'.format(ângulo,tangente))

def desafio019():
  n1 = str(input('Primeiro aluno(a): '))
  n2 = str(input('Segundo aluno(a): '))
  n3 = str(input('Terceiro aluno(a): '))
  n4 = str(input('Quarto aluno:(a) '))
  lista = [n1, n2, n3, n4]
  escolhido = random.choice(lista)
  print(f'O aluno(a) escolhido foi: {escolhido}')

def desafio020():
  n1 = str(input('primeiro aluno(a): '))
  n2 = str(input('segundo aluno(a): '))
  n3 = str(input('terceiro aluno(a): '))
  n4 = str(input('quarto aluno(a): '))
  lista = [n1, n2, n3, n4]
  random.shuffle(lista)
  print('A ordem da apresentação será:')
  print(lista)

''''''''''def desafio021():
  pygame.init()
  pygame.mixer.music.load(' Best_Friend')
  pygame.mixer.music.play()
  pygame.event.wait()'''''''''''''''

def desafio022():
  nome = str(input('digite o seu nome completo: ')).strip()
  print('analisando o seu nome...')
  
  print(f'Seu nome em maiscula é: {nome.upper()}')
  print(f'Seu nome em minuscula é: {nome.lower()}')
  print(f'Seu nome tem ao todo: {len(nome)-nome.count(" ")}')
  print(f'Seu primeiro nome tem {nome.find(" ")} letras')

def desafio023():
  n = int(input('infome um número: '))
  
  u = n // 1 % 10
  d = n // 10 % 10
  c = n // 100 % 10
  m = n // 1000 % 10
  
  print(f'Analisando o número {n}')
  print(f'Unidade: {u} ')
  print(f'Dezena: {d}')
  print(f'Centena: {c}')
  print(f'Milhar: {m}')

def desafio024():
  cidade = str(input('Digite um nome de uma cidade: ')).strip()
  print('Santo' in cidade)

def desafio025():
  nome = str(input('digite o seu nome completo: ')).strip()
  print('Seu nome tem  silva? ' , 'silva' in nome.lower() )

def desafio026():
  frase = str(input('digite uma frase: ')).upper()
  a = frase.count('A')
  p1 = frase.find('A')+1
  p2 = frase.rfind('A')+1
  print(f'A letra A aparece {a} vezes')
  print(f'A primeira letra A apareceu na posição: {p1}')
  print(f'A ultima letra A apareceu na posição: {p2}')

def desafio027():
  nome = str(input('digite o seu nome  completo: ')).strip()
  n = nome.split()
  print(f'seu primeiro nome é: {n[0]}')
  print('Seu último nome é: {}'.format(n[len(n)-1]))

def desafio028():
  computador = randint(0, 5)
  print('=-='* 20)
  print('vou pensar em número entre 0 e 5 tente adivinhar....')
  print('=-=' * 20)
  jogador = int(input('Em que número eu pensei? '))
  if jogador == computador:
    print('PARABÉNS VOCÊ ACERTOU!')
  else:
    print(f'GANHEI! eu pensei no número {computador} e não no {jogador}')

def desafio029():
  velocidade = float(input('digite a velocidade de um carro: '))
  m = (velocidade - 80) * 7
  if velocidade < 80:
    print('Tenha um Bom dia, dirija com segurança!')
  elif velocidade > 80:
    print('Você foi MULTADO! por utrapassar a velocidade limite de 80km/h')
  print(f'sua multa é de: {m} reais')

def desafio030():
  n = int(input('Me diga um número qualquer: '))
  resultado = n % 2
  if resultado == 0:
    print(f'o número {n} é PAR!')
  else:
    print(f'o número {n} é IMPAR!')

def desafio031():
  distancia = float(input('qual a distância da sua viagem? '))
  print(f'Você está prestes a começar uma viagem de {distancia} Km.')
  preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
  print(f'o preço da sua passagem será de {preço} reais.')

def desafio032():
  ano = int(input('Digite o ano: '))
  if ano == 0:
    ano = date.today().year
  if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto')
  else:
    print(f'{ano} Não é um ano bissexto')

def desafio033():
  n1 = int(input('digite o 1° número: '))
  n2 = int(input('digite o 3° número: '))
  n3 = int(input('digite o 3° número: '))

  menor = n1
  if n2 < n1 and n2 < n3:
    menor = n2
  if n3 < n1 and n3 < n2:
    menor = n3

  maior = n1
  if n2 > n1 and n2 > n3:
    maior = n2
  if n3 > n1 and n3 > n2:
    maior = n3
  print(f'o número maior é: {maior}')
  print(f'o número menor é: {menor}')

def desafio034():
  salario = float(input('qual é o sálario do funcionario? '))
  if salario <=1250:
    novo = salario + (salario * 15 / 100)
  else:
    novo = salario + (salario * 10 / 100)
    print(f'Quem recebia R${salario:.2f} agora com o almento passa a receber R${novo:.2f}')

def desafio035():
  print('==' * 20)
  print('Analisador de triangulo')
  print('==' * 20)
  r1 = float(input('Primeiro segmento: '))
  r2 = float(input('Segundo segmento: '))
  r3 = float(input('Terceiro segmento: '))
  if r1 < r2 + r3 and r2 < r1 + r3  and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
  else:
    print('Os segmentos acima NÃO podem formar um triângulo')
    
  

  
  
  
  
  
  