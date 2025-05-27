from importlib.resources import files, as_file
from linkml_runtime.utils.schemaview import SchemaView


def load_runtime_metamodel() -> SchemaView:
    resource = files("linkml_runtime.linkml_model.model.schema").joinpath("meta.yaml")
    with as_file(resource) as path:
        return SchemaView(path)


def main():
    sv = load_runtime_metamodel()
    # print(sv.get_class("slot_definition"))

    class_name = "slot_definition"

    # Get all slots (including inherited ones)
    applicable_slots = sv.class_induced_slots(class_name)

    # Print name and range of each
    for slot in applicable_slots:
        print(f"{slot.name}: {slot.range}  {slot.multivalued = }")


if __name__ == "__main__":
    main()
