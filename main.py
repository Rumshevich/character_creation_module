from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Функция расчета аттаки персонажей."""
    dmg: int = 0
    if char_class == 'warrior':
        dmg = 5 + randint(3, 5)
    if char_class == 'mage':
        dmg = 5 + randint(5, 10)
    if char_class == 'healer':
        dmg = 5 + randint(-3, -1)
    return (f'{char_name} нанёс урон противнику равный {dmg}')


def defence(char_name: str, char_class: str) -> str:
    """Функция расчета защиты персонажей."""
    blc: int = 0
    if char_class == 'warrior':
        blc = 10 + randint(5, 10)
    if char_class == 'mage':
        blc = 10 + randint(-2, 2)
    if char_class == 'healer':
        blc = 10 + randint(2, 5)
    return (f'{char_name} блокировал {blc} урона')


def special(char_name: str, char_class: str) -> str:
    """Функция расчета специальных умений персонажей."""
    spec: str = ''
    if char_class == 'warrior':
        spec = '«Выносливость 105»'
    if char_class == 'mage':
        spec = '«Атака 45»'
    if char_class == 'healer':
        spec = '«Защита 40»'
    return (f'{char_name} применил специальное умение {spec}')


def start_training(char_name: str, char_class: str) -> str:
    """Функция проведения тренировки."""
    atc: str = 'attack — чтобы атаковать противника'
    dfn: str = 'defence — чтобы блокировать атаку противника'
    spc: str = 'special — чтобы использовать свою суперсилу'
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(f'Введи одну из команд: {atc}, {dfn} или {spc}.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Функция выбора персонажей."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, чтобы '
                               'выбрать другого персонажа: '.lower())
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
