from collections import Counter


LOG_FILE = "sample_auth.log"
ALERT_THRESHOLD = 3


def extract_ip_from_failed_line(line):
    """
    Extrait l'adresse IP depuis une ligne contenant 'Failed password'.
    Retourne None si rien n'est trouvé.
    """
    parts = line.split()

    if "from" not in parts:
        return None

    try:
        ip_index = parts.index("from") + 1
        return parts[ip_index]
    except IndexError:
        return None


def analyze_ssh_logs(file_path):
    failed_ips = []
    total_failed = 0

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if "Failed password" not in line:
                    continue

                total_failed += 1
                ip = extract_ip_from_failed_line(line)

                if ip:
                    failed_ips.append(ip)

        ip_counter = Counter(failed_ips)
        suspicious_ips = {
            ip: count
            for ip, count in ip_counter.items()
            if count >= ALERT_THRESHOLD
        }

        print("=== Analyse des logs SSH ===")
        print(f"Nombre total d'échecs : {total_failed}")
        print()

        if suspicious_ips:
            print("Adresses IP à surveiller :")
            for ip, count in sorted(
                suspicious_ips.items(),
                key=lambda item: item[1],
                reverse=True
            ):
                print(f"- {ip} : {count} échecs")
        else:
            print("Aucune IP n'a dépassé le seuil d'alerte.")

    except FileNotFoundError:
        print(f"Erreur : le fichier '{file_path}' est introuvable.")
    except OSError as error:
        print(f"Erreur lors de la lecture du fichier : {error}")


if __name__ == "__main__":
    analyze_ssh_logs(LOG_FILE)