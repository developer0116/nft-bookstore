from brownie import Bookstore,accounts,network,config

def main():

    dev=accounts.add(config['wallets']['from_key'])
    print(network.show_active())
    publish_source=False
    Bookstore.deploy({'from': dev},publish_source=publish_source)