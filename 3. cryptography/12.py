#!/usr/bin/env python3
"""
auth_demo.py

Demo of a simple digital-signature authentication flow.

Usage examples:
  # generate keys (creates alice_private.pem and alice_public.pem)
  python auth_demo.py generate --name alice

  # sign a message file
  python auth_demo.py sign --key alice_private.pem --message message.txt --out sig.bin

  # verify a signature
  python auth_demo.py verify --key alice_public.pem --message message.txt --sig sig.bin
"""

import argparse
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from pathlib import Path

# -------- Configuration (defaults) --------
RSA_KEY_SIZE = 4096  # secure default
PUBLIC_EXPONENT = 65537

# -------- Helpers: Key generation, (de)serialization --------
def generate_rsa_keypair(name: str, out_dir: Path = Path(".")):
    """
    Generates RSA keypair and writes them as PEM files:
      - {name}_private.pem  (unencrypted PEM)
      - {name}_public.pem   (SubjectPublicKeyInfo PEM)
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    priv_path = out_dir / f"{name}_private.pem"
    pub_path = out_dir / f"{name}_public.pem"

    private_key = rsa.generate_private_key(
        public_exponent=PUBLIC_EXPONENT,
        key_size=RSA_KEY_SIZE,
        backend=default_backend(),
    )

    # Private key PEM (no encryption for demo; in production use a passphrase!)
    priv_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    priv_path.write_bytes(priv_pem)

    # Public key PEM (SubjectPublicKeyInfo)
    public_key = private_key.public_key()
    pub_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    pub_path.write_bytes(pub_pem)

    print(f"Generated keys:\n  Private: {priv_path}\n  Public:  {pub_path}")
    return priv_path, pub_path

def load_private_key(path: Path):
    data = path.read_bytes()
    return serialization.load_pem_private_key(data, password=None, backend=default_backend())

def load_public_key(path: Path):
    data = path.read_bytes()
    return serialization.load_pem_public_key(data, backend=default_backend())

# -------- Signing & Verification --------
def sign_message(private_key_path: Path, message_path: Path, signature_out: Path):
    """
    Steps matching the slide:
    1. H = hash(M)  -- we use SHA-256
    2. Sign H with private key (RSA-PSS)
    3. Output signature (binary) to a file
    """
    priv = load_private_key(private_key_path)
    message = message_path.read_bytes()

    # Hash-then-sign is done inside the sign() call by specifying the hash algorithm.
    signature = priv.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )

    signature_out.write_bytes(signature)
    print(f"Message signed -> signature written to: {signature_out}")

def verify_signature(public_key_path: Path, message_path: Path, signature_path: Path) -> bool:
    """
    Verification steps (receiver):
    1. Compute H(M)
    2. Decrypt/verify signature with sender's public key (RSA-PSS verify)
    3. If verify succeeds -> signature valid
    """
    pub = load_public_key(public_key_path)
    message = message_path.read_bytes()
    signature = signature_path.read_bytes()

    try:
        pub.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        print("Signature is VALID ✅")
        return True
    except Exception as e:
        print("Signature is INVALID ❌")
        return False

# -------- CLI --------
def main():
    p = argparse.ArgumentParser(prog="auth_demo", description="Simple RSA signature demo")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("generate", help="Generate RSA keypair")
    g.add_argument("--name", "-n", required=True, help="Name/prefix for key files")
    g.add_argument("--out", "-o", default=".", help="Output directory for keys")

    s = sub.add_parser("sign", help="Sign a message")
    s.add_argument("--key", "-k", required=True, help="Private key PEM file")
    s.add_argument("--message", "-m", required=True, help="Message file to sign")
    s.add_argument("--out", "-o", default="signature.bin", help="Output signature file")

    v = sub.add_parser("verify", help="Verify a signature")
    v.add_argument("--key", "-k", required=True, help="Public key PEM file")
    v.add_argument("--message", "-m", required=True, help="Message file to verify")
    v.add_argument("--sig", "-s", required=True, help="Signature file produced earlier")

    args = p.parse_args()

    if args.cmd == "generate":
        generate_rsa_keypair(args.name, Path(args.out))
    elif args.cmd == "sign":
        sign_message(Path(args.key), Path(args.message), Path(args.out))
    elif args.cmd == "verify":
        verify_signature(Path(args.key), Path(args.message), Path(args.sig))

if __name__ == "__main__":
    main()


# echo "hello world" > message.txt

# python 12.py generate --name alice

# python 12.py sign --key alice_private.pem --message message.txt --out sig.bin

# python 12.py verify --key alice_public.pem --message message.txt --sig sig.bin