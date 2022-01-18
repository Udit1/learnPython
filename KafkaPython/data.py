from faker import Faker
faker = Faker()


def mock_data():
    return {"Name": faker.name(), "address": faker.address()}


if __name__ == "__main__":
    print(mock_data())
