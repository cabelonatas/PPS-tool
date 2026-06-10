import requests
import argparse

class HeaderAnalyzer:
    def __init__(self, target):
        if not target.startswith("http"):
            self.target = "https://" + target
        else:
            self.target = target
            
        self.headers_to_check = [
            'Content-Security-Policy',
            'Strict-Transport-Security',
            'X-Frame-Options',
            'X-Content-Type-Options'
        ]
   
    def exportar_relatorio(self, resultados):
        with open("relatorio_seguranca.txt", "w") as f:
            f.write(f"Relatório de Segurança para: {self.target}\n")
            f.write("-" * 30 + "\n")
            for linha in resultados:
                f.write(linha + "\n")
        print("[*] Relatório salvo como 'relatorio_seguranca.txt'")

    def check_headers(self):
        print(f"[*] Analisando headers de: {self.target}")
        resultados = [] 
        try:
            response = requests.get(self.target)
            for header in self.headers_to_check:
                status = f"{header}: {'PRESENTE' if header in response.headers else 'AUSENTE'}"
                print(f"[+] {status}")
                resultados.append(status)
            
            self.exportar_relatorio(resultados)
            
        except Exception as e:
            print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Security Header Checker (SHC)")
    parser.add_argument("-u", "--url", required=True, help="URL alvo (ex: https://google.com)")
    args = parser.parse_args()
    analyzer = HeaderAnalyzer(args.url)
    analyzer.check_headers()