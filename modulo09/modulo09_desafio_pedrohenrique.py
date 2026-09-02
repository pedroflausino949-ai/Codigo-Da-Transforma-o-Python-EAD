import dataclasses
import getpass


# ==========================================
# 1. DOMÍNIO E EXCEÇÕES
# ==========================================
class AuthError(Exception):
    """Exceção base para o domínio de autenticação."""
    pass

class CredenciaisInvalidasError(AuthError):
    """Lançado quando usuário ou senha estão incorretos."""
    pass

class LimiteTentativasExcedidoError(AuthError):
    """Lançado quando o limite de falhas é excedido."""
    pass


@dataclasses.dataclass(frozen=True)
class Credencial:
    usuario: str
    senha: str


# ==========================================
# 2. SERVIÇO DE AUTENTICAÇÃO
# ==========================================
class AuthService:
    def __init__(self, credencial_valida: Credencial, max_tentativas: int = 3):
        self._credencial = credencial_valida
        self.max_tentativas = max_tentativas
        self._falhas = 0

    @property
    def bloqueado(self) -> bool:
        return self._falhas >= self.max_tentativas

    def autenticar(self, credencial: Credencial) -> bool:
        if self.bloqueado:
            raise LimiteTentativasExcedidoError("Conta bloqueada temporariamente.")

        if credencial != self._credencial:
            self._falhas += 1
            restantes = self.max_tentativas - self._falhas
            
            if self.bloqueado:
                raise LimiteTentativasExcedidoError("Acesso bloqueado! Limite de tentativas atingido.")
            
            raise CredenciaisInvalidasError(f"Dados incorretos. Tentativas restantes: {restantes}")

        self._falhas = 0
        return True


# ==========================================
# 3. INTERFACE DE USUÁRIO
# ==========================================
def executar_interface_login():
    credencial_master = Credencial(usuario="dev_user", senha="pass123")
    servico = AuthService(credencial_valida=credencial_master, max_tentativas=3)

    print("┌" + "─" * 40 + "┐")
    print("│         AUTENTICAÇÃO DE SISTEMA        │")
    print("└" + "─" * 40 + "┘")

    while True:
        try:
            usr = input("\n👤 Usuário: ").strip()
            
            # getpass oculta a digitação no terminal
            pwd = getpass.getpass("🔑 Senha:   ")

            tentativa = Credencial(usuario=usr, senha=pwd)
            
            if servico.autenticar(tentativa):
                print("\n✨ [SUCESSO] Bem-vindo ao sistema!")
                break

        except CredenciaisInvalidasError as err:
            print(f"⚠️  [ATENÇÃO] {err}")

        except LimiteTentativasExcedidoError as err:
            print(f"\n🛑 [BLOQUEIO] {err}")
            print("Sessão finalizada por segurança.")
            break

        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Operação cancelada pelo usuário.")
            break


# ==========================================
# EXECUÇÃO DO SISTEMA
# ==========================================
if __name__ == "__main__":
    executar_interface_login()