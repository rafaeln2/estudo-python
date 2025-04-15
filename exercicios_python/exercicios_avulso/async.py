import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulating a network delay
    print("Data fetched!")
    return {"data": "Sample data"}
async def print_data():
    for i in range(5):
        print(f"Printing data {i}...")
        await asyncio.sleep(1)
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_data())
    
    valor1 = await task1
    print(f"Valor 1: {valor1}")
    await task2
    # valor2 =
asyncio.run(main())