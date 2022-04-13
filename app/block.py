import json
import os
import hashlib

blocks_dir = os.curdir + '/blocks/'


def get_hash(filename):
    """Генерируем последний блок в хэш"""
    blocks_dir = os.curdir + '/blocks/'
    file = open(blocks_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def get_files():
    return sorted([int(i) for i in os.listdir(blocks_dir)])


def check_integrity():
    """Проверка блоков через сравнение хешей"""

    files = get_files()
    results = []

    for file in files[1:]:
        f = open(blocks_dir + str(file))
        h = json.load(f)['Хеш']
        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)
        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'
        results.append({'block': prev_file, 'result': res})
    return results


def write_block(name, amount, whom_to, prev_hash=''):
    """Для генерации имени нового блока получаем отсортированный список блоков
        и прибавляем единицу к номеру последнего блока."""
    files = get_files()
    prev_file = files[-1]
    filename = str(prev_file + 1)

    """Получаем хэш на основе предыдущего блока и записываем новый блок в JSON."""
    prev_hash = get_hash(str(prev_file))

    data = {"Отправитель": name,
            "Сумма": amount,
            "Получатель": whom_to,
            "Хеш": prev_hash}

    with open(blocks_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block('Marduk', 88, 'Erebus')
    print(check_integrity())


if __name__ == '__main__':
    main()
