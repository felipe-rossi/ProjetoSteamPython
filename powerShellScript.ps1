while ($true) {
    # Executa o arquivo de teste específico
    python -m pytest tests/test_steam.py
    Start-Sleep -Seconds 1  # Opcional: adicione um intervalo entre as execuções
}