v_full = 130 * 2560 * 1440 * 30
v_compressed = 130 * 1920 * 1080 * 28
print((v_full - v_compressed) // 2 ** 13)
