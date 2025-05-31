import hashlib
import requests

def check_password_leak(password: str) -> bool:
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    try:
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao conectar à API de senhas HIBP: {e}")
        return False

    for line in response.text.splitlines():
        parts = line.strip().split(":")
        if len(parts) != 2:
            continue
        hash_suffix, count = parts
        if hash_suffix == suffix:
            print(f"💥 Senha encontrada {count} vezes em vazamentos!")
            return True

    print("✅ Senha NÃO encontrada em vazamentos.")
    return False

def main():
    password = input("Digite a senha para verificar: ").strip()

    if not password:
        print("❌ A senha é obrigatória.")
        return

    print("🔍 Verificando senha na base do Have I Been Pwned...")
    check_password_leak(password)

if __name__ == "__main__":
    main()

