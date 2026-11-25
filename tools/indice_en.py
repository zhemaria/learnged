"""Kept so old instructions still work: the indexes are now built by tools/build_indices.py."""
import runpy, os
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_indices.py"), run_name="__main__")
