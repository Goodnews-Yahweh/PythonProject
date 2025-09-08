import hashlib

def dictionary_attack(target_hash, dictionary_file, hash_type='sha256'):
    """
    Perform a dictionary attack against a target hash.
    
    Args:
        target_hash (str): The hash to crack
        dictionary_file (str): Path to dictionary file
        hash_type (str): Type of hash algorithm (default: sha256)
    
    Returns:
        str: The found password or None if not found
    """
    # Supported hash algorithms
    hash_functions = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512
    }
    
    if hash_type not in hash_functions:
        raise ValueError(f"Unsupported hash type: {hash_type}")
    
    hash_func = hash_functions[hash_type]
    
    try:
        with open(dictionary_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue
                
                # Hash the password
                hashed_password = hash_func(password.encode()).hexdigest()
                
                # Compare with target hash
                if hashed_password == target_hash.lower():
                    return password
                    
    except FileNotFoundError:
        print(f"Error: Dictionary file not found: {dictionary_file}")
    except Exception as e:
        print(f"Error: {e}")
    
    return None

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Dictionary Password Cracker')
    parser.add_argument('hash', help='Target hash to crack')
    parser.add_argument('dictionary', help='Path to dictionary file')
    parser.add_argument('--hash-type', default='sha256', 
                       help='Hash algorithm (default: sha256)')
    
    args = parser.parse_args()
    
    print(f"Attempting to crack hash: {args.hash}")
    print(f"Using dictionary: {args.dictionary}")
    print(f"Hash algorithm: {args.hash_type}")
    print("Starting attack...")
    
    password = dictionary_attack(args.hash, args.dictionary, args.hash_type)
    
    if password:
        print(f"\nSuccess! Password found: {password}")
    else:
        print("\nPassword not found in dictionary.")
