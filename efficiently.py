# efficiently calculate our actual public key!
public_key = secret_key * G
print(f"x: {public_key.x}\ny: {public_key.y}")
print("Verify the public key is on the curve: ", (public_key.y**2 - public_key.x**3 - 7) % bitcoin_curve.p == 0)
