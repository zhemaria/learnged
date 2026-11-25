"""Se conserva para que las instrucciones anteriores sigan funcionando: los índices ahora los construye tools/build_indices.py."""
import runpy, os
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_indices.py"), run_name="__main__")
