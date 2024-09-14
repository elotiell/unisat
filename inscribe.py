import random
import string
from api import create_inscribe, mint_inscribe
from wallet import load_wallets

def generate_random_name(min_length=6, max_length=12):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    wallets = load_wallets('./wallets.json')
    
    for wallet in wallets:
      inscribe_name = generate_random_name()

        
        content = f"Inscribe: {inscribe_name}"
        inscribe_response = create_inscribe(wallet['address'], content)
        print(f'Inscribe response for {wallet["address"]}: {inscribe_response}')
        
       
        inscribe_id = inscribe_response.get('id')
        if inscribe_id:
            mint_response = mint_inscribe(wallet['address'], inscribe_id)
            print(f'Mint response: {mint_response}')
        else:
            print(f"Failed to create inscribe for {wallet['address']}")

if __name__ == '__main__':
    main()
