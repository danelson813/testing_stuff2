from typing import TypeVar, Type, List
import json
import os

# Define a generic type T
T = TypeVar("T")


class GenericRepository:
    def __init__(self, entity_class: Type[T], filename: str = "generic_database.json"):
        self._items = {}
        self._entity_class = entity_class
        self._filename = filename

        self.load_from_file()

    def get(self, item_id: str) -> T:
        return self._items.get(item_id)

    def get_all(self) -> List[T]:
        return list(self._items.values())

    def save(self, item: T) -> None:
        if hasattr(item, "id"):
            if item.id in self._items:
                raise ValueError(f"Item with id {item.id} already exists!")
            self._items[item.id] = item

        self.store_to_file()

    def update(self, item_id: str, new_item: T) -> T:
        if item_id not in self._items:
            raise ValueError(f"Item with id {item_id} does not exist!")

        self._items[item_id] = new_item

        self.store_to_file()

        return self._items[item_id]

    def delete(self, item_id: str) -> T:
        if item_id not in self._items:
            raise ValueError(f"Item with id {item_id} does not exist!")

        removed_item = self._items[item_id]
        del self._items[item_id]

        self.store_to_file()

        return removed_item

    def store_to_file(self) -> None:
        items_to_save = [vars(item) for _, item in self._items.items()]

        with open(self._filename, "w") as file:
            json.dump(items_to_save, file)

    def load_from_file(self) -> None:
        if os.path.exists(self._filename):
            with open(self._filename, "r") as file:
                items_data = json.load(file)

            for data in items_data:
                item = self._entity_class(**data)
                self.save(item)
