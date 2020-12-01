import zipfile38, time, os
# Путь и имя архива
path0 = 'D:\\Study\\Backup'
path1 = 'D:\\Study\\Backup\\' + time.strftime('%d%m%Y')
name = time.strftime('%H%M %d%m%Y') + '.zip'

if not os.path.exists(path0):
    os.mkdir(path0)
    print('Каталог успешно создан', path0)
if not os.path.exists(path1):
    os.mkdir(path1)
    print('Каталог успешно создан', path1)
# меняем текущую дерикторию
os.chdir(path1)


# создание архива
zf = zipfile38.PyZipFile(name, 'w')

# Исключения для добавления в архив
def notests(s):
    fn = os.path.basename(s)
    return ( not (fn == 'test' or fn.startswith('test_') ) )

# запись
zf.writepy(path1, filterfunc=notests)


