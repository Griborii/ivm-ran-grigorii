#!/bin/bash

set -e

check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "Python3 не установлен!"
        echo "Установите Python 3.8 или выше"
        exit 1
    fi
    
    python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    echo -e "Python версия: $python_version"
    
    if [ $(echo "$python_version < 3.8" | bc -l) -eq 1 ]; then
        echo -e "Рекомендуется Python 3.8 или выше"
    fi
}

run_program() {
   echo -e "Запуск программы..."
    echo "=" * 50
    
    python3 test1.py "$@"
    
    local exit_code=$?
    echo "=" * 50
    
    if [ $exit_code -eq 0 ]; then
        echo -e  "Программа завершилась успешно"
    else
        echo -e "Программа завершилась с ошибкой (код: $exit_code)"
        exit $exit_code
    fi
}

check_python

run_program
