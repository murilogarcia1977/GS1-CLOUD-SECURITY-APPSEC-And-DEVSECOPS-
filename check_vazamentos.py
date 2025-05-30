import hashlib
import requests

def check_password_leak(password: str) -> bool:
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro na API de senhas HIBP: {response.status_code}")
        return False

    hashes = response.text.splitlines()
    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            print(f"💥 Senha encontrada {count} vezes em vazamentos!")
            return True

    print("✅ Senha NÃO encontrada em vazamentos.")
    return False

def main():
    email = input("Digite o e-mail para verificar: ").strip()
    password = input("Digite a senha para verificar: ").strip()

    if not email or not password:
        print("E-mail e senha são obrigatórios.")
        return

    print(f"\n🔍 Resultado da verificação para: {email}")

    print("\n⚠️ Consulta manual usando os links abaixo para e-mail:\n")
    print(f"1. Mozilla Monitor:")
    print(f"   https://monitor.firefox.com/?email={email}\n")
    print(f"2. F-Secure Identity Theft Checker:")
    print(f"   https://www.f-secure.com/en/identity-theft-checker/email/{email}\n")

    print("🔍 Verificando senha na base do Have I Been Pwned (API pública gratuita)...")
    check_password_leak(password)

    print(f"\n🔍 Consulta de senha no Cybernews:")
    print(f"https://cybernews.com/breaches/search/?q={password}")

if __name__ == "__main__":
    main()
