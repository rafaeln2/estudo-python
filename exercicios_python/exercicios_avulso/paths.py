from pathlib import Path
# lib só funciona rodando no terminal ¯\_(ツ)_/¯
# caminho = Path(__file__).parent.parent
caminho = Path()
for item in caminho.glob("*.*"):
    print(item)

# caminho.mkdir()
# caminho.rmdir()