clean_project() {
    echo -e "Очистка проекта..."
    
    # Удаляем файлы Python кэша
    find . -type f -name "*.pyc" -delete
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
    
    # Удаляем временные файлы
    rm -f .coverage
    rm -rf htmlcov/
    rm -rf .benchmarks/
    
   	echo -e "Очистка завершена"
}

clean_project
