while ($true) {
    # Executa o arquivo de teste específico
    python -m unittest Steam.py
    Start-Sleep -Seconds 1  # Opcional: adicione um intervalo entre as execuções
}