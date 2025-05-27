from importlib.resources import files, as_file
from linkml_runtime.utils.schemaview import SchemaView


def load_runtime_metamodel() -> SchemaView:
    resource = files("linkml_runtime.linkml_model.model.schema").joinpath("meta.yaml")
    with as_file(resource) as path:
        return SchemaView(path)


def main():
    sv = load_runtime_metamodel()
    print(sv.get_class("slot_definition"))


if __name__ == "__main__":
    main()
