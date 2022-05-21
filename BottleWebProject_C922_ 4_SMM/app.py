"""
Этот скрипт запускает приложение с использованием сервера разработки.
"""

import bottle
import os
import sys

# routes и repository содержат HTTP-обработчики дл¤ сервера и должны быть импортированы.
import routes
import repository

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Режим отладки включает более подробный вывод в консоль
    bottle.debug(True)


# Настройка сервера
if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
    # Обработчик статических файлов, используемый с сервером разработки.
        return bottle.static_file(filepath, root=STATIC_ROOT)

    # Запускает локальный сервер.
    bottle.run(server='wsgiref', host=HOST, port=PORT)
