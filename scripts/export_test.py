import os
import shutil

from export import export


def test_export_with_folder():
    export_folder = "./tmp"
    export_file = f"{export_folder}/todos.json"

    export(export_folder)

    assert os.path.exists(export_folder)
    assert os.path.exists(export_file)

    os.remove(export_file)
    os.rmdir(export_folder)


def test_export_with_folder_and_file():
    export_folder = "./tmp2_created_by_a_test"
    export_file = "data_exported.json"

    file_path = export(export_folder, export_file)

    assert os.path.exists(file_path)

    shutil.rmtree(export_folder)
