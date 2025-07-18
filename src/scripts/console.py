def start() -> None:
    print('-' * 99)
    print(f'{"-" * 40} Microsoft Rewards {"-" * 40}') # Caracteres no título = 19
    print('-' * 99)
    print('\n-> Esse bot é responsável por fazer as pesquisa diárias para conseguir pontos no Microsoft Rewards.\n')
    # print('-> Pressione "S" para parar o bot\n')
    input('Pressione ENTER para começar... ')
    print()

def end() -> None:
    input('Pressione ENTER para sair do programa... ')

def exception(msg:str) -> None:
    print(f'Algo deu errado: {msg}')
