import dns.resolver


def main(domain):
    records = ['A', 'NS', 'MX']

    for record in records:
        try:
            responses = dns.resolver.resolve(domain, record)
            print(f"\nRegistros {record} : ")
            print("-----------------------------------")
            for response in responses:
                print(response)
        except Exception as exception:
            print("Cannot resolve query for record:", record)
            print("Error obtaining record information:", exception)


if __name__ == '__main__':
    try:
        main('example.com')
    except KeyboardInterrupt:
        exit()
