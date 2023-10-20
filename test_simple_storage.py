from brownie import SimpleStorage, accounts
import brownie.network as network

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_Storage = SimpleStorage.deploy({"fom": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected 


def tes_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"form": account})
    #Act
    expected = 15
    txn = simple_storage.store(expected, {"from": account})
    txn.wait(1)
    # Assert
    assert expected == simple_storage.retrieve()

