# if our secret key was the integer 1, then our public key would just be G:
sk = 1
pk = G
print(f" secret key: {sk}\n public key: {(pk.x, pk.y)}")
print("Verify the public key is on the curve: ", (pk.y**2 - pk.x**3 - 7) % bitcoin_curve.p == 0)
# if it was 2, the public key is G + G:
sk = 2
pk = G + G
print(f" secret key: {sk}\n public key: {(pk.x, pk.y)}")
print("Verify the public key is on the curve: ", (pk.y**2 - pk.x**3 - 7) % bitcoin_curve.p == 0)
# etc.:
sk = 3
pk = G + G + G
print(f" secret key: {sk}\n public key: {(pk.x, pk.y)}")
print("Verify the public key is on the curve: ", (pk.y**2 - pk.x**3 - 7) % bitcoin_curve.p == 0)
