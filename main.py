import asyncio

from curtain import Curtain



async def main():
    curtain = Curtain()

    while True:
        try:
            await curtain.send("cycle")
            print(curtain.current_state)

        except Exception as e:
            print(e)


if __name__ == "__main__": 
    asyncio.run(main())