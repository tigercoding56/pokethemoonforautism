import asyncio, pygame, PIL, time 
import gc
import libraries
#import micropip

#asyncio.run( micropip.install("https://github.com/tigercoding56/pygbag-costum-wheels/blob/main/pygame_gui-0.6.8-py3-none-any.whl?raw=true",deps=False))
# Do init here and load any assets right now to avoid lag at runtime or network errors.
#asyncio.get_event_loop().set_debug(True)

async def main():
    global libraries
    ##workaround for stupid asyncio
    while True:

        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop, maybe less on some mobile devices
        #time.sleep(1/60)
        libraries.main()
        pygame.display.update()
        #gc.collect(2)

        await asyncio.sleep(0)  # Very important, and keep it 0



# This is the program entry point:
asyncio.run(main())
#main()
# Do not add anything from here
# asyncio.run is non-blocking on pygame-wasm
