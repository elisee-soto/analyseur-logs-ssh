from collections import Counter

def analyze_ssh_logs(file_path):
    failed_attempts = []
    total_failed = 0

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if "Failed password" in line:
                    total_failed += 1
                    parts = line.split()

                    if "from" in parts:
                        ip_index = parts.index("from") + 1

                        if ip_index < len(parts):
                            ip = parts[ip_index]
                            failed_attempts.append(ip)

        ip_counter = Counter(failed_attempts)

        print("=== Analyse des logs SSH ===")
        print("Nombre total d'échecs de connexion :", total_failed)
        print("")
        print("IP suspectes :")

        for ip, count in ip_counter.items():
            if count >= 3:
                print("-", ip, ":", count, "tentatives échouées")

    except FileNotFoundError:
        print("Erreur : fichier introuvable.")

analyze_ssh_logs("sample_auth.log")