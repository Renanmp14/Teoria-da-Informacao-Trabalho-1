"""Configuração dos testes.

Garante que o diretório ``src`` e a raiz do projeto estejam disponíveis no
``sys.path`` para que a CLI e os módulos usados pela GUI funcionem sem depender
de instalação prévia.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

for path in (ROOT, SRC):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)
