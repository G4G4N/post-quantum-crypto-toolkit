# benchmarks.py

import time
import numpy as np
from pqct.toolkit import PostQuantumCryptoToolkit

def benchmark_kyber():
    toolkit = PostQuantumCryptoToolkit()
    plaintext = np.random.randint(0, 3329, 256)

    start = time.time()
    public_key, private_key = toolkit.supported_algorithms['kyber'].generate_keypair()
    ciphertext = toolkit.encrypt('kyber', plaintext)
    decrypted = toolkit.decrypt('kyber', ciphertext, private_key)
    end = time.time()

    print(f"Kyber encryption and decryption took {end - start:.6f} seconds")

def benchmark_dilithium():
    toolkit = PostQuantumCryptoToolkit()
    message = b"Benchmarking Dilithium signature scheme"

    start = time.time()
    public_key, private_key = toolkit.supported_algorithms['dilithium'].generate_keypair()
    signature = toolkit.sign('dilithium', message)
    verification = toolkit.verify('dilithium', message, signature, public_key)
    end = time.time()

    print(f"Dilithium signing and verification took {end - start:.6f} seconds")

if __name__ == '__main__':
    benchmark_kyber()
    benchmark_dilithium()
