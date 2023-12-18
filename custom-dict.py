class CustomDict(dict):
    def __getitem__(self, key):
        return super().get(key, 'N/A')

    def __missing__(self, key):
        backup_values = { 'name': 'N/A', 'age': 0, 'favorite_color': 'Unknown' }
        return backup_values.get(key, 'That is not a valid key')

d1 = CustomDict(
    name="Shaun",
    hair_color="brown"
)

print(d1['blah'])
