from concurrent.futures import ThreadPoolExecutor
import argparse
import socket

def scan_port(target, port):
    """Tenta conectar em uma porta específica"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Porta {port} está ABERTA")
            try:
                banner = sock.recv(1024).decode().strip()
                print(f"    [!] Serviço identificado: {banner}")
            except:
                print(" [!] Nenhuma identificação de serviço encontrada.")
        
        sock.close()
    except Exception as e:
        pass

def main():
    parser = argparse.ArgumentParser(description="Pynix Port Scanner (PPS) - Ferramenta de Mapeamento de Rede")
    parser.add_argument("-t", "--target", required=True, help="IP ou host alvo")
    parser.add_argument("-p", "--ports", required=True, help="Ex: 80,443 (lista) ou 21-80 (range)")
    args = parser.parse_args()

    if '-' in args.ports:
        start, end = map(int, args.ports.split('-'))
        port_list = range(start, end + 1)
    else:
        port_list = [int(p) for p in args.ports.split(',')]

    print(f"[*] Iniciando PPS contra: {args.target}")

    with ThreadPoolExecutor(max_workers=20) as executor:
        for port in port_list:
            executor.submit(scan_port, args.target, port)
        
        print("[*] Scan finalizado.")

if __name__ == "__main__":
    main()