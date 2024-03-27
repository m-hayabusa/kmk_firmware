try:
    from keyboard.base import keyboard

    keyboard.go()

except Exception as e:
    print(
        """
=========================
- Error -----------------
========================="""
    )
    print(e)
    print("=========================\n")

    from keyboard.fallback import keyboard

    keyboard.go()
