class CountedInt(int):
    __number_of_instances = 0

    def __new__(cls, value):
        super().__new__(cls, value)
        cls.__number_of_instances += 1

    @classmethod
    def get_instance_count(cls):
        return cls.__number_of_instances

x = CountedInt(10)
y = CountedInt(10)
z = CountedInt(10)

print(f'There are {CountedInt.get_instance_count()} instances of CountedInt')