import asyncio, pygame, PIL
import libraries


# Do init here and load any assets right now to avoid lag at runtime or network errors.


async def main():
    global libraries

    while True:

        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop, maybe less on some mobile devices
        libraries.main()

        await asyncio.sleep(0)  # Very important, and keep it 0



# This is the program entry point:
asyncio.run(main())

# Do not add anything from here
# asyncio.run is non-blocking on pygame-wasm
