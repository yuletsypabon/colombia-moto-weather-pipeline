import sys
import subprocess

checks = []

version = sys.version_info
checks.append(("Python >= 3.10", version.major == 3 and version.minor >= 10))

libs = ["requests", "pandas", "psycopg2", "dotenv"]
for lib in libs:
    try:
        __import__(lib)
        checks.append((f"Librería: {lib}", True))
    except ImportError:
        checks.append((f"Librería: {lib}", False))

result = subprocess.run(["docker", "info"], capture_output=True)
checks.append(("Docker corriendo", result.returncode == 0))

print("\n--- Verificación del entorno ---\n")
all_ok = True
for name, ok in checks:
    status = "✓" if ok else "✗"
    print(f"  {status}  {name}")
    if not ok:
        all_ok = False

print()
if all_ok:
    print("Todo listo. Puedes empezar la Semana 1.\n")
else:
    print("Hay elementos pendientes. Revisa los marcados con ✗\n")
