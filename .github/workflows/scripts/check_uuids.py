import yaml
from pathlib import Path
from collections import defaultdict

def main():
    uuid_map = defaultdict(list)
    base_path = Path("data")

    for file_path in base_path.rglob("*.yaml"):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                content = yaml.safe_load(f)
                if not content or "questions" not in content:
                    continue
                for q in content["questions"]:
                    uuid = q.get("uuid")
                    if uuid:
                        uuid_map[uuid].append(str(file_path))
            except Exception as e:
                print(f"⚠️ Error reading {file_path}: {e}")

    duplicates = {uuid: paths for uuid, paths in uuid_map.items() if len(paths) > 1}

    if duplicates:
        print("❌ Duplicate UUIDs found:")
        for uuid, paths in duplicates.items():
            print(f"- UUID {uuid} found in:")
            for path in paths:
                print(f"  - {path}")
        exit(1)
    else:
        print("✅ All UUIDs are unique.")

if __name__ == "__main__":
    main()
