def start() -> None:
    print('-' * 70)
    print(f'{"-" * 26} Microsoft Rewards {"-" * 25}')
    print('-' * 70)
    print('\nEsse bot é responsável por fazer as pesquisa diárias no Microsft Edge,')
    print('para conseguir pontos no Microsoft Rewards.\n')
    input('Pressione ENTER para começar... ')
    print()

def end() -> None:
    input('Pressione ENTER para sair do programa... ')

def exception(msg:str) -> None:
    print(f'Algo deu errado: {msg}')
