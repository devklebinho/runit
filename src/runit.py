import psutil
import subprocess
import time

def is_program_running(program_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == program_name:
            return True
    return False

def main():
    program_name = 'CScliente.exe'
    while True:
        try:
            if is_program_running(program_name):
                print(f'O programa "{program_name}" está em execução.')
                
            else:
                print(f'O programa "{program_name}" não está em execução.')
                time.sleep(3)
                program_path = r"reiniciar.bat"  
                print("Reiniciando o Sistema...")
                subprocess.run(program_path)
            time.sleep(3)
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')
            break

if __name__ == "__main__":
    main()