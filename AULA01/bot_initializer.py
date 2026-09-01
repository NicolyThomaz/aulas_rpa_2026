BOT_NAME: str = "RPA_FINANCEIRO_01"
MAX_RETRIES: int = 3
EXECUTION_TIMEOUT: float = 60.0
IS_PRODUCTION: bool = True

print(f"Nome do Bot: {BOT_NAME} | Tipo: {type(BOT_NAME)}")
print(f"Maximo de Tentativas: {MAX_RETRIES} | Tipo: {type(MAX_RETRIES)}")
print(f"Tempo Limite: {EXECUTION_TIMEOUT} segundos | Tipo: {type(EXECUTION_TIMEOUT)}")
print(f"É Produção: {IS_PRODUCTION} | Tipo: {type(IS_PRODUCTION)}")